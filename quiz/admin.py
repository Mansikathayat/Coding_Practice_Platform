from django.contrib import admin
from .models import Quiz, Question, Choice, QuizAttempt, UserAnswer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'time_limit', 'is_active', 'created_at']
    list_filter = ['category', 'difficulty', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'question_type', 'points', 'order']
    list_filter = ['question_type', 'quiz__category']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'total_questions', 'time_taken', 'completed_at']
    list_filter = ['quiz', 'completed_at']
    search_fields = ['user__username', 'quiz__title']
    readonly_fields = ['completed_at']