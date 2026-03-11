from django.contrib import admin
from .models import Problem, TestCase, ProblemTemplate


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1


class ProblemTemplateInline(admin.TabularInline):
    model = ProblemTemplate
    extra = 1


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'category', 'created_at']
    list_filter = ['difficulty', 'category', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TestCaseInline, ProblemTemplateInline]


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['problem', 'is_sample']
    list_filter = ['is_sample', 'problem__difficulty']