from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from submissions.models import Submission
from problems.models import Problem
from .models import UserProfile, MiniProject
from django.db.models import Count, Q
from datetime import date, timedelta

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')[:10]
    total_problems = Problem.objects.count()
    solved_problems = Submission.objects.filter(user=request.user, status='accepted').values('problem').distinct().count()
    
    stats = {
        'total_submissions': user_submissions.count(),
        'solved_problems': solved_problems,
        'total_problems': total_problems,
        'success_rate': round((solved_problems / total_problems * 100), 1) if total_problems > 0 else 0,
        'current_streak': profile.current_streak,
        'longest_streak': profile.longest_streak
    }
    
    return render(request, 'users/profile.html', {
        'submissions': user_submissions,
        'stats': stats,
        'profile': profile
    })

@login_required
def progress(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    submissions = Submission.objects.filter(user=user).order_by('-submitted_at')
    
    # Problem difficulty stats
    easy_solved = submissions.filter(status='accepted', problem__difficulty='easy').values('problem').distinct().count()
    medium_solved = submissions.filter(status='accepted', problem__difficulty='medium').values('problem').distinct().count()
    hard_solved = submissions.filter(status='accepted', problem__difficulty='hard').values('problem').distinct().count()
    
    easy_total = Problem.objects.filter(difficulty='easy').count()
    medium_total = Problem.objects.filter(difficulty='medium').count()
    hard_total = Problem.objects.filter(difficulty='hard').count()
    
    progress_data = {
        'easy': {'solved': easy_solved, 'total': easy_total},
        'medium': {'solved': medium_solved, 'total': medium_total},
        'hard': {'solved': hard_solved, 'total': hard_total},
        'total_solved': easy_solved + medium_solved + hard_solved,
        'recent_submissions': submissions[:5],
        'streak': profile.current_streak,
        'longest_streak': profile.longest_streak
    }
    
    return render(request, 'users/progress.html', {'progress': progress_data})

@login_required
def leaderboard(request):
    # Get user stats with profiles
    users_stats = []
    for user in User.objects.all():
        profile, created = UserProfile.objects.get_or_create(user=user)
        solved_count = Submission.objects.filter(
            user=user, 
            status='accepted'
        ).values('problem').distinct().count()
        
        total_submissions = Submission.objects.filter(user=user).count()
        
        if total_submissions > 0:
            users_stats.append({
                'user': user,
                'solved_count': solved_count,
                'total_submissions': total_submissions,
                'success_rate': round((solved_count / total_submissions * 100), 1),
                'current_streak': profile.current_streak,
                'longest_streak': profile.longest_streak
            })
    
    # Sort by solved count, then by streak
    users_stats.sort(key=lambda x: (x['solved_count'], x['current_streak']), reverse=True)
    
    return render(request, 'users/leaderboard.html', {'users_stats': users_stats})

@login_required
def mini_projects(request):
    projects = MiniProject.objects.all().order_by('-created_at')
    return render(request, 'users/mini_projects.html', {'projects': projects})