from problems.models import Problem

examples = {
    'Two Sum': '''
**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Input: nums = [3,2,4], target = 6
Output: [1,2]
```''',
    
    'Reverse String': '''
**Example:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```''',
    
    'Valid Palindrome': '''
**Example:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
```''',
    
    'Remove Duplicates from Sorted Array': '''
**Example:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```''',
    
    'Best Time to Buy and Sell Stock': '''
**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
```''',
    
    'Valid Parentheses': '''
**Example:**
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```''',
    
    'Maximum Subarray': '''
**Example:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1
```''',
    
    'Climbing Stairs': '''
**Example:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
```''',
    
    'Binary Tree Inorder Traversal': '''
**Example:**
```
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```''',
    
    'Same Tree': '''
**Example:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false
```'''
}

count = 0
for title, example in examples.items():
    try:
        problem = Problem.objects.get(title=title)
        if 'Example:' not in problem.description:
            problem.description += example
            problem.save()
            count += 1
            print(f'Added example to: {title}')
    except Problem.DoesNotExist:
        print(f'Problem not found: {title}')

print(f'Updated {count} problems with examples!')