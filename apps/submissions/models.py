from django.db import models
from django.contrib.auth.models import User
from apps.problems.models import Problem


class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('time_limit_exceeded', 'Time Limit Exceeded'),
        ('memory_limit_exceeded', 'Memory Limit Exceeded'),
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
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    execution_time = models.FloatField(null=True, blank=True)
    memory_used = models.FloatField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'problem']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"


class TestCaseResult(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='test_results')
    test_case = models.ForeignKey('problems.TestCase', on_delete=models.CASCADE)
    passed = models.BooleanField()
    actual_output = models.TextField(blank=True)
    execution_time = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.submission} - Test Case {self.test_case.id} - {'Passed' if self.passed else 'Failed'}"