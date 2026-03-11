from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Quiz, Question, QuizAttempt, UserAnswer
import json
import time


def quiz_list(request):
    quizzes = Quiz.objects.filter(is_active=True).order_by('-created_at')
    
    # Get user's quiz attempts for completion status
    user_quiz_data = {}
    if request.user.is_authenticated:
        attempts = QuizAttempt.objects.filter(user=request.user).select_related('quiz')
        for attempt in attempts:
            quiz_id = attempt.quiz.id
            if quiz_id not in user_quiz_data or attempt.score > user_quiz_data[quiz_id]['score']:
                user_quiz_data[quiz_id] = {
                    'completed': True,
                    'score': attempt.score,
                    'total_questions': attempt.total_questions,
                    'percentage': round((attempt.score / attempt.total_questions * 100), 1)
                }
    
    return render(request, 'quiz/list.html', {
        'quizzes': quizzes,
        'user_quiz_data': user_quiz_data
    })


@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    questions = quiz.questions.all()
    
    # Check if user has already attempted
    user_attempts = QuizAttempt.objects.filter(user=request.user, quiz=quiz).order_by('-score')
    best_attempt = user_attempts.first() if user_attempts else None
    
    # Calculate percentage for best attempt
    best_percentage = None
    if best_attempt:
        best_percentage = round((best_attempt.score / best_attempt.total_questions * 100), 1)
    
    return render(request, 'quiz/detail.html', {
        'quiz': quiz,
        'questions_count': questions.count(),
        'best_attempt': best_attempt,
        'best_percentage': best_percentage,
        'total_attempts': user_attempts.count()
    })


@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    questions = quiz.questions.prefetch_related('choices').all()
    
    return render(request, 'quiz/start.html', {
        'quiz': quiz,
        'questions': questions,
        'start_time': int(time.time())
    })


@login_required
@csrf_exempt
def submit_quiz(request, quiz_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    
    try:
        data = json.loads(request.body)
        answers = data.get('answers', {})
        time_taken = data.get('time_taken', 0)
        
        # Create quiz attempt
        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            total_questions=quiz.questions.count(),
            time_taken=time_taken
        )
        
        score = 0
        total_points = 0
        
        # Process answers
        for question_id, choice_id in answers.items():
            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
                total_points += question.points
                
                if choice_id:
                    from .models import Choice
                    choice = Choice.objects.get(id=choice_id, question=question)
                    is_correct = choice.is_correct
                    
                    if is_correct:
                        score += question.points
                    
                    UserAnswer.objects.create(
                        attempt=attempt,
                        question=question,
                        selected_choice=choice,
                        is_correct=is_correct
                    )
                else:
                    # No answer selected
                    UserAnswer.objects.create(
                        attempt=attempt,
                        question=question,
                        selected_choice=None,
                        is_correct=False
                    )
            except (Question.DoesNotExist, Choice.DoesNotExist):
                continue
        
        attempt.score = score
        attempt.save()
        
        return JsonResponse({
            'success': True,
            'score': score,
            'total_points': total_points,
            'percentage': round((score / total_points * 100), 1) if total_points > 0 else 0,
            'attempt_id': attempt.id
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def quiz_result(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    answers = attempt.answers.select_related('question', 'selected_choice').all()
    
    total_points = sum(answer.question.points for answer in answers)
    percentage = round((attempt.score / total_points * 100), 1) if total_points > 0 else 0
    
    return render(request, 'quiz/result.html', {
        'attempt': attempt,
        'answers': answers,
        'percentage': percentage,
        'total_points': total_points
    })


def daily_quiz(request):
    """Get today's daily quiz with completion status"""
    from datetime import date
    today = date.today()
    
    # Simple logic: use day of year to select quiz
    day_of_year = today.timetuple().tm_yday
    quizzes = Quiz.objects.filter(is_active=True).order_by('id')
    
    if not quizzes.exists():
        return redirect('quiz:list')
    
    # Get today's quiz (rotate through available quizzes)
    daily_quiz = quizzes[day_of_year % quizzes.count()]
    
    # Check if user has completed today's quiz
    completed_today = False
    best_score = None
    if request.user.is_authenticated:
        today_attempts = QuizAttempt.objects.filter(
            user=request.user,
            quiz=daily_quiz,
            completed_at__date=today
        ).order_by('-score')
        
        if today_attempts.exists():
            completed_today = True
            best_attempt = today_attempts.first()
            best_score = {
                'score': best_attempt.score,
                'total': best_attempt.total_questions,
                'percentage': round((best_attempt.score / best_attempt.total_questions * 100), 1),
                'time_taken': best_attempt.time_taken
            }
    
    return render(request, 'quiz/daily.html', {
        'daily_quiz': daily_quiz,
        'completed_today': completed_today,
        'best_score': best_score,
        'today': today
    })