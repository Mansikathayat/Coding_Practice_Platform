from problems.models import Category, Problem, TestCase

# Add more problems
palindrome = Problem.objects.create(
    title="Valid Palindrome",
    slug="valid-palindrome",
    description="""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.""",
    difficulty="easy",
    category=Category.objects.get(name="Strings")
)

TestCase.objects.create(
    problem=palindrome,
    input_data='"A man, a plan, a canal: Panama"',
    expected_output="true",
    is_sample=True
)

TestCase.objects.create(
    problem=palindrome,
    input_data='"race a car"',
    expected_output="false",
    is_sample=True
)

# Add medium problem
three_sum = Problem.objects.create(
    title="3Sum",
    slug="3sum",
    description="""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]""",
    difficulty="medium",
    category=Category.objects.get(name="Arrays")
)

TestCase.objects.create(
    problem=three_sum,
    input_data="[-1,0,1,2,-1,-4]",
    expected_output="[[-1,-1,2],[-1,0,1]]",
    is_sample=True
)

# Add hard problem
median_arrays = Problem.objects.create(
    title="Median of Two Sorted Arrays",
    slug="median-two-sorted-arrays",
    description="""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.""",
    difficulty="hard",
    category=Category.objects.get(name="Arrays")
)

TestCase.objects.create(
    problem=median_arrays,
    input_data="[1,3]\n[2]",
    expected_output="2.0",
    is_sample=True
)

print("Additional problems created!")