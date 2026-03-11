from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from apps.submissions.models import Submission


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'users/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Registration successful')
        return redirect('home')
    
    return render(request, 'users/register.html')


@login_required
def profile_view(request):
    user = request.user
    submissions = Submission.objects.filter(user=user).order_by('-created_at')[:10]
    
    solved_count = Submission.objects.filter(
        user=user, 
        status='accepted'
    ).values('problem').distinct().count()
    
    total_submissions = Submission.objects.filter(user=user).count()
    
    context = {
        'user': user,
        'submissions': submissions,
        'solved_count': solved_count,
        'total_submissions': total_submissions,
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def leaderboard(request):
    users_stats = []
    for user in User.objects.all():
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
                'success_rate': round((solved_count / total_submissions * 100), 1)
            })
    
    users_stats.sort(key=lambda x: (x['solved_count'], x['success_rate']), reverse=True)
    
    return render(request, 'users/leaderboard.html', {'users_stats': users_stats})