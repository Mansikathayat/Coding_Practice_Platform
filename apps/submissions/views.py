from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Submission


@login_required
def submission_list(request):
    submissions = Submission.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'submissions/list.html', {'submissions': submissions})


@login_required
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk, user=request.user)
    return render(request, 'submissions/detail.html', {'submission': submission})