from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=100)
    time_limit = models.IntegerField(default=1000)  # milliseconds
    memory_limit = models.IntegerField(default=128)  # MB
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['difficulty']),
            models.Index(fields=['category']),
        ]
    
    def __str__(self):
        return self.title


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.problem.title} - Test Case {self.id}"


class ProblemTemplate(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
    ]
    
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='templates')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    template_code = models.TextField()
    
    class Meta:
        unique_together = ['problem', 'language']
    
    def __str__(self):
        return f"{self.problem.title} - {self.language}"