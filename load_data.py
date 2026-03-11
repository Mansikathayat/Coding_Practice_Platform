from problems.models import Category, Problem, TestCase
from django.contrib.auth.models import User

# Create categories
arrays_cat = Category.objects.create(name="Arrays", description="Array manipulation problems")
strings_cat = Category.objects.create(name="Strings", description="String processing problems")
math_cat = Category.objects.create(name="Math", description="Mathematical problems")

# Create problems
two_sum = Problem.objects.create(
    title="Two Sum",
    slug="two-sum",
    description="""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].""",
    difficulty="easy",
    category=arrays_cat
)

# Add test cases
TestCase.objects.create(
    problem=two_sum,
    input_data="[2,7,11,15]\n9",
    expected_output="[0,1]",
    is_sample=True
)

reverse_string = Problem.objects.create(
    title="Reverse String",
    slug="reverse-string",
    description="""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]""",
    difficulty="easy",
    category=strings_cat
)

TestCase.objects.create(
    problem=reverse_string,
    input_data='["h","e","l","l","o"]',
    expected_output='["o","l","l","e","h"]',
    is_sample=True
)

print("Sample data created successfully!")