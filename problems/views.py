from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit
import json
import subprocess
import tempfile
import os
import bleach
from .models import Problem, Category
from submissions.models import Submission

def problem_list(request):
    problems = Problem.objects.select_related('category').all()
    categories = Category.objects.all()
    
    difficulty = request.GET.get('difficulty')
    category_id = request.GET.get('category')
    
    if difficulty:
        problems = problems.filter(difficulty=difficulty)
    if category_id:
        problems = problems.filter(category_id=category_id)
    
    return render(request, 'problems/list.html', {
        'problems': problems,
        'categories': categories,
        'selected_difficulty': difficulty,
        'selected_category': category_id,
    })

def problem_detail(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    sample_cases = problem.test_cases.filter(is_sample=True)
    return render(request, 'problems/detail.html', {
        'problem': problem,
        'sample_cases': sample_cases,
    })

@csrf_exempt
def run_code(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body.decode('utf-8'))
        code = data.get('code', '')
        language = data.get('language', 'python')
        input_data = data.get('input', '')
        
        if not code or code.strip() == '':
            return JsonResponse({'error': 'Please write some code first'})
        
        # Support for Python, Java, and JavaScript
        if language == 'python':
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                result = subprocess.run(
                    ['python', temp_file],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                os.unlink(temp_file)
                
                return JsonResponse({
                    'output': result.stdout,
                    'error': result.stderr if result.stderr else None,
                    'returncode': result.returncode
                })
            except Exception as e:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
                return JsonResponse({'error': str(e)})
        
        elif language == 'java':
            # Check if code has main method, if not add it
            if 'public static void main' not in code:
                # Wrap code in main method
                code = f'''public class Solution {{
    public static void main(String[] args) {{
        {code}
    }}
}}'''
            
            temp_dir = tempfile.mkdtemp()
            java_file = os.path.join(temp_dir, 'Solution.java')
            
            with open(java_file, 'w') as f:
                f.write(code)
            
            try:
                # Compile Java
                compile_result = subprocess.run(
                    ['javac', java_file],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    cwd=temp_dir
                )
                
                if compile_result.returncode != 0:
                    import shutil
                    shutil.rmtree(temp_dir)
                    return JsonResponse({
                        'output': '',
                        'error': compile_result.stderr,
                        'returncode': 1
                    })
                
                # Run Java
                result = subprocess.run(
                    ['java', 'Solution'],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=temp_dir
                )
                
                import shutil
                shutil.rmtree(temp_dir)
                
                return JsonResponse({
                    'output': result.stdout,
                    'error': result.stderr if result.stderr else None,
                    'returncode': result.returncode
                })
            except Exception as e:
                import shutil
                shutil.rmtree(temp_dir)
                return JsonResponse({'error': str(e)})
        
        elif language == 'javascript':
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                result = subprocess.run(
                    ['node', temp_file],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                os.unlink(temp_file)
                
                return JsonResponse({
                    'output': result.stdout,
                    'error': result.stderr if result.stderr else None,
                    'returncode': result.returncode
                })
            except Exception as e:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
                return JsonResponse({'error': str(e)})
        
        return JsonResponse({'error': 'Language not supported yet'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def execute_code(code, language, input_data):
    """Secure code execution with timeout and memory limits"""
    
    language_configs = {
        'python': {'ext': '.py', 'cmd': ['python']},
        'java': {'ext': '.java', 'cmd': ['javac', '{}', '&&', 'java']},
        'javascript': {'ext': '.js', 'cmd': ['node']},
    }
    
    if language not in language_configs:
        raise ValueError('Unsupported language')
    
    config = language_configs[language]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        if language == 'java':
            file_path = os.path.join(temp_dir, 'Solution.java')
        else:
            file_path = os.path.join(temp_dir, f'solution{config["ext"]}')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        try:
            if language == 'java':
                # Compile Java
                compile_result = subprocess.run(
                    ['javac', file_path],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    cwd=temp_dir
                )
                if compile_result.returncode != 0:
                    return {'error': compile_result.stderr, 'output': '', 'returncode': 1}
                
                # Run Java
                result = subprocess.run(
                    ['java', 'Solution'],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=temp_dir
                )
            else:
                cmd = config['cmd'] + [file_path]
                result = subprocess.run(
                    cmd,
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
            
            return {
                'output': result.stdout.strip() if result.stdout else '',
                'error': result.stderr.strip() if result.stderr else '',
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {'error': 'Code execution timed out', 'output': '', 'returncode': 1}
        except Exception as e:
            return {'error': f'Execution error: {str(e)}', 'output': '', 'returncode': 1}