from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Submission
from problems.views import execute_code
from problems.models import Problem, TestCase
import json
import subprocess
import tempfile
import os

def generate_ai_explanation(code, language):
    """Generate AI explanation for code"""
    explanations = {
        'python': {
            'print': 'Uses print() to display output to console.',
            'def': 'Defines a function with def keyword.',
            'for': 'Uses for loop to iterate through elements.',
            'while': 'Uses while loop for conditional repetition.',
            'if': 'Uses conditional statements for decision making.',
            'return': 'Returns a value from the function.',
            'list': 'Works with Python lists for data storage.',
            'len': 'Gets length of sequences using len().',
            'range': 'Generates number sequences with range().',
            'str': 'Manipulates strings and text data.',
        },
        'java': {
            'System.out.println': 'Prints output using System.out.println().',
            'public static void main': 'Main method - program entry point.',
            'public class': 'Defines a public class in Java.',
            'for': 'Uses for loop for iteration.',
            'if': 'Uses if-else for conditional logic.',
            'Scanner': 'Uses Scanner class for input.',
            'String': 'Works with String objects.',
        },
        'javascript': {
            'console.log': 'Outputs to browser console using console.log().',
            'function': 'Defines a JavaScript function.',
            'for': 'Uses for loop to iterate.',
            'if': 'Uses conditional statements.',
            'return': 'Returns value from function.',
            'let': 'Declares block-scoped variables.',
            'const': 'Declares constants.',
        }
    }
    
    explanation_parts = []
    lang_explanations = explanations.get(language, {})
    
    for keyword, explanation in lang_explanations.items():
        if keyword in code:
            explanation_parts.append(explanation)
    
    if not explanation_parts:
        return f"This {language} code implements a solution using basic programming concepts."
    
    return " ".join(explanation_parts[:3])  # Limit to 3 explanations

@login_required
def submission_list(request):
    submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'submissions/list.html', {'submissions': submissions})

@login_required
def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id, user=request.user)
    return render(request, 'submissions/detail.html', {'submission': submission})

@csrf_exempt
@login_required
def submit_solution(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    data = json.loads(request.body)
    problem_slug = data.get('problem_slug')
    code = data.get('code', '')
    language = data.get('language', 'python')
    
    problem = get_object_or_404(Problem, slug=problem_slug)
    
    # Create submission
    submission = Submission.objects.create(
        user=request.user,
        problem=problem,
        code=code,
        language=language,
        status='pending'
    )
    
    # Generate AI explanation
    ai_explanation = generate_ai_explanation(code, language)
    submission.ai_explanation = ai_explanation
    
    # Run tests
    test_cases = problem.test_cases.all()
    passed_tests = 0
    
    for test_case in test_cases:
        try:
            result = execute_code(code, language, test_case.input_data)
            actual_output = result.get('output', '').strip()
            expected_output = test_case.expected_output.strip()
            
            print(f"Debug Submit - Expected: '{expected_output}', Got: '{actual_output}'")
            
            # More flexible comparison
            if (actual_output == expected_output or 
                actual_output.lower() == expected_output.lower() or
                actual_output.replace(' ', '').replace('\n', '') == expected_output.replace(' ', '').replace('\n', '')):
                passed_tests += 1
            else:
                submission.status = 'wrong_answer'
                print(f"Submit Test failed - Expected: '{expected_output}', Got: '{actual_output}'")
                break
        except Exception as e:
            submission.status = 'runtime_error'
            print(f"Submit Runtime error: {str(e)}")
            break
    
    if passed_tests == len(test_cases) and submission.status == 'pending':
        submission.status = 'accepted'
        # Update user streak on successful submission
        from users.models import UserProfile
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.update_streak()
    
    submission.save()
    
    return JsonResponse({
        'status': submission.status,
        'passed_tests': passed_tests,
        'total_tests': len(test_cases),
        'ai_explanation': submission.ai_explanation,
        'debug_info': f'Expected vs Got comparison logged in console'
    })

def execute_code_with_input(code, language, input_data):
    """Execute code with given input"""
    language_configs = {
        'python': {'ext': '.py', 'cmd': ['python']},
        'java': {'ext': '.java', 'cmd': ['javac', '{}', '&&', 'java']},
        'javascript': {'ext': '.js', 'cmd': ['node']},
    }
    
    config = language_configs.get(language)
    if not config:
        raise ValueError('Unsupported language')
    
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, f'solution{config["ext"]}')
        
        with open(file_path, 'w') as f:
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
                    return {'error': compile_result.stderr}
                
                # Run Java
                result = subprocess.run(
                    ['java', 'solution'],
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
                'output': result.stdout,
                'error': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {'error': 'Code execution timed out'}