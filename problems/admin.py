from django.contrib import admin
from .models import Category, Problem, TestCase

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'category', 'created_at']
    list_filter = ['difficulty', 'category']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['problem', 'is_sample']
    list_filter = ['is_sample']