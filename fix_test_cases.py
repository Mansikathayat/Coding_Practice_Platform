from problems.models import Problem, TestCase

# Update Two Sum test case
try:
    two_sum = Problem.objects.get(slug='two-sum')
    test_case = two_sum.test_cases.first()
    if test_case:
        test_case.expected_output = '[0,1]'
        test_case.save()
        print("Updated Two Sum test case")
except:
    print("Two Sum problem not found")

# Update Reverse String test case  
try:
    reverse_string = Problem.objects.get(slug='reverse-string')
    test_case = reverse_string.test_cases.first()
    if test_case:
        test_case.expected_output = '["o","l","l","e","h"]'
        test_case.save()
        print("Updated Reverse String test case")
except:
    print("Reverse String problem not found")

print("Test cases updated!")