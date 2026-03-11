from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.submissions.models import Submission

@login_required
def leaderboard(request):
    # Get user stats
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
    
    # Sort by solved count, then by success rate
    users_stats.sort(key=lambda x: (x['solved_count'], x['success_rate']), reverse=True)
    
    return render(request, 'users/leaderboard.html', {'users_stats': users_stats})