from rest_framework import serializers
from .models import Problem, TestCase, ProblemTemplate


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['input_data', 'expected_output']


class ProblemTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTemplate
        fields = ['language', 'template_code']


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'title', 'slug', 'difficulty', 'category']


class ProblemDetailSerializer(serializers.ModelSerializer):
    sample_test_cases = TestCaseSerializer(many=True, read_only=True)
    templates = ProblemTemplateSerializer(many=True, read_only=True)
    
    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'slug', 'description', 'difficulty', 
            'category', 'time_limit', 'memory_limit', 
            'sample_test_cases', 'templates'
        ]