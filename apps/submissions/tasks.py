from celery import shared_task
from django.conf import settings
import subprocess
import tempfile
import os
import time
from .models import Submission, TestCaseResult


@shared_task
def execute_code(submission_id):
    try:
        submission = Submission.objects.get(id=submission_id)
        submission.status = 'running'
        submission.save()
        
        problem = submission.problem
        test_cases = problem.test_cases.all()
        
        all_passed = True
        total_time = 0
        
        for test_case in test_cases:
            result = run_test_case(submission, test_case)
            if not result['passed']:
                all_passed = False
                submission.status = result['status']
                submission.error_message = result.get('error', '')
                break
            total_time += result.get('execution_time', 0)
        
        if all_passed:
            submission.status = 'accepted'
        
        submission.execution_time = total_time
        submission.save()
        
    except Exception as e:
        submission.status = 'runtime_error'
        submission.error_message = str(e)
        submission.save()


def run_test_case(submission, test_case):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            if submission.language == 'python':
                return run_python_code(submission.code, test_case, temp_dir)
            elif submission.language == 'java':
                return run_java_code(submission.code, test_case, temp_dir)
            elif submission.language == 'javascript':
                return run_javascript_code(submission.code, test_case, temp_dir)
    except Exception as e:
        return {
            'passed': False,
            'status': 'runtime_error',
            'error': str(e)
        }


def run_python_code(code, test_case, temp_dir):
    file_path = os.path.join(temp_dir, 'solution.py')
    
    with open(file_path, 'w') as f:
        f.write(code)
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ['python', file_path],
            input=test_case.input_data,
            capture_output=True,
            text=True,
            timeout=settings.CODE_EXECUTION_TIMEOUT
        )
        
        execution_time = time.time() - start_time
        
        if result.returncode != 0:
            return {
                'passed': False,
                'status': 'runtime_error',
                'error': result.stderr,
                'execution_time': execution_time
            }
        
        actual_output = result.stdout.strip()
        expected_output = test_case.expected_output.strip()
        
        TestCaseResult.objects.create(
            submission_id=submission.id,
            test_case=test_case,
            passed=actual_output == expected_output,
            actual_output=actual_output,
            execution_time=execution_time
        )
        
        return {
            'passed': actual_output == expected_output,
            'status': 'accepted' if actual_output == expected_output else 'wrong_answer',
            'execution_time': execution_time
        }
        
    except subprocess.TimeoutExpired:
        return {
            'passed': False,
            'status': 'time_limit_exceeded'
        }


def run_java_code(code, test_case, temp_dir):
    # Java implementation
    pass


def run_javascript_code(code, test_case, temp_dir):
    # JavaScript implementation
    pass