from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('time_limit_exceeded', 'Time Limit Exceeded'),
        ('runtime_error', 'Runtime Error'),
        ('compilation_error', 'Compilation Error'),
    ]
    
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    runtime = models.FloatField(null=True, blank=True)
    memory_used = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ai_explanation = models.TextField(blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'problem']),
            models.Index(fields=['status']),
        ]
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"