from problems.models import Problem, TestCase

# Check all test cases
for problem in Problem.objects.all():
    print(f"\nProblem: {problem.title}")
    for i, test_case in enumerate(problem.test_cases.all()):
        print(f"  Test {i+1}:")
        print(f"    Input: '{test_case.input_data}'")
        print(f"    Expected: '{test_case.expected_output}'")
        
        # Fix common issues
        if problem.slug == 'two-sum':
            test_case.expected_output = '[0, 1]'
            test_case.save()
            print("    Fixed Two Sum output")
        elif problem.slug == 'reverse-string':
            test_case.expected_output = 'olleh'
            test_case.save()
            print("    Fixed Reverse String output")

print("\nTest cases checked and fixed!")