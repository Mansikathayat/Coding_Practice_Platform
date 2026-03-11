from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_solved_date = models.DateField(null=True, blank=True)
    total_problems_solved = models.IntegerField(default=0)
    
    def update_streak(self):
        today = date.today()
        if self.last_solved_date:
            if self.last_solved_date == today:
                return  # Already solved today
            elif self.last_solved_date == today - timedelta(days=1):
                self.current_streak += 1
            else:
                self.current_streak = 1
        else:
            self.current_streak = 1
        
        self.last_solved_date = today
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
        self.save()

class MiniProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=15, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    tech_stack = models.CharField(max_length=200)
    code_snippet = models.TextField()
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title