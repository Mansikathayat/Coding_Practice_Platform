from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Problem, TestCase, ProblemTemplate
from apps.submissions.models import Submission
import json


def problem_list(request):
    problems = Problem.objects.all()
    difficulty = request.GET.get('difficulty')
    category = request.GET.get('category')
    
    if difficulty:
        problems = problems.filter(difficulty=difficulty)
    if category:
        problems = problems.filter(category=category)
    
    return render(request, 'problems/list.html', {'problems': problems})


def problem_detail(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    sample_test_cases = problem.test_cases.filter(is_sample=True)
    templates = problem.templates.all()
    
    context = {
        'problem': problem,
        'sample_test_cases': sample_test_cases,
        'templates': templates,
    }
    
    if request.user.is_authenticated:
        user_submissions = Submission.objects.filter(
            user=request.user, 
            problem=problem
        ).order_by('-created_at')[:5]
        context['user_submissions'] = user_submissions
    
    return render(request, 'problems/detail.html', context)


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def submit_solution(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    
    try:
        data = json.loads(request.body)
        code = data.get('code')
        language = data.get('language')
        
        if not code or not language:
            return JsonResponse({'error': 'Code and language are required'}, status=400)
        
        # Create submission
        submission = Submission.objects.create(
            user=request.user,
            problem=problem,
            code=code,
            language=language,
            status='pending'
        )
        
        # Execute code asynchronously
        from apps.submissions.tasks import execute_code
        execute_code.delay(submission.id)
        
        return JsonResponse({
            'submission_id': submission.id,
            'status': 'submitted'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)