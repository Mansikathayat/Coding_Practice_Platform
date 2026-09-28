# Run this in Django shell: python manage.py shell
# Then copy and paste this code

from problems.models import Problem

# Add examples to problems that don't have them
problems_data = [
    {
        'title': 'Reverse String',
        'example': 'Input: "hello"\nOutput: "olleh"\n\nInput: "world"\nOutput: "dlrow"'
    },
    {
        'title': 'Palindrome Check',
        'example': 'Input: "racecar"\nOutput: True\n\nInput: "hello"\nOutput: False'
    },
    {
        'title': 'FizzBuzz',
        'example': 'Input: 15\nOutput: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]'
    },
    {
        'title': 'Find Maximum',
        'example': 'Input: [3, 1, 4, 1, 5, 9, 2, 6]\nOutput: 9\n\nInput: [-1, -5, -2]\nOutput: -1'
    },
    {
        'title': 'Count Vowels',
        'example': 'Input: "hello world"\nOutput: 3\n\nInput: "programming"\nOutput: 3'
    },
    {
        'title': 'Sum of Digits',
        'example': 'Input: 12345\nOutput: 15\n\nInput: 999\nOutput: 27'
    },
    {
        'title': 'Factorial',
        'example': 'Input: 5\nOutput: 120\n\nInput: 0\nOutput: 1'
    },
    {
        'title': 'Prime Check',
        'example': 'Input: 17\nOutput: True\n\nInput: 15\nOutput: False'
    },
    {
        'title': 'Fibonacci Sequence',
        'example': 'Input: 7\nOutput: [0, 1, 1, 2, 3, 5, 8]\n\nInput: 5\nOutput: [0, 1, 1, 2, 3]'
    },
    {
        'title': 'Remove Duplicates',
        'example': 'Input: [1, 2, 2, 3, 4, 4, 5]\nOutput: [1, 2, 3, 4, 5]\n\nInput: ["a", "b", "a", "c"]\nOutput: ["a", "b", "c"]'
    },
    {
        'title': 'Two Sum',
        'example': 'Input: nums = [2, 7, 11, 15], target = 9\nOutput: [0, 1]\n\nInput: nums = [3, 2, 4], target = 6\nOutput: [1, 2]'
    },
    {
        'title': 'Valid Parentheses',
        'example': 'Input: "()"\nOutput: True\n\nInput: "([)]"\nOutput: False\n\nInput: "{[]}"\nOutput: True'
    },
    {
        'title': 'Merge Two Sorted Lists',
        'example': 'Input: list1 = [1, 2, 4], list2 = [1, 3, 4]\nOutput: [1, 1, 2, 3, 4, 4]\n\nInput: list1 = [], list2 = [0]\nOutput: [0]'
    },
    {
        'title': 'Binary Search',
        'example': 'Input: nums = [-1, 0, 3, 5, 9, 12], target = 9\nOutput: 4\n\nInput: nums = [-1, 0, 3, 5, 9, 12], target = 2\nOutput: -1'
    },
    {
        'title': 'Longest Common Prefix',
        'example': 'Input: ["flower", "flow", "flight"]\nOutput: "fl"\n\nInput: ["dog", "racecar", "car"]\nOutput: ""'
    },
    {
        'title': 'Maximum Subarray',
        'example': 'Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]\nOutput: 6\n\nInput: [1]\nOutput: 1'
    },
    {
        'title': 'Contains Duplicate',
        'example': 'Input: [1, 2, 3, 1]\nOutput: True\n\nInput: [1, 2, 3, 4]\nOutput: False'
    },
    {
        'title': 'Missing Number',
        'example': 'Input: [3, 0, 1]\nOutput: 2\n\nInput: [0, 1]\nOutput: 2'
    },
    {
        'title': 'Single Number',
        'example': 'Input: [2, 2, 1]\nOutput: 1\n\nInput: [4, 1, 2, 1, 2]\nOutput: 4'
    },
    {
        'title': 'Climbing Stairs',
        'example': 'Input: 2\nOutput: 2\n\nInput: 3\nOutput: 3'
    }
]

print("Starting to add examples to problems...")
updated_count = 0
not_found_count = 0

for data in problems_data:
    try:
        problem = Problem.objects.get(title=data['title'])
        
        # Check if example already exists
        if 'Example:' not in problem.description and '**Example:**' not in problem.description:
            # Add example to description
            problem.description += f"\n\n**Example:**\n{data['example']}"
            problem.save()
            print(f"✅ Updated '{problem.title}' with example")
            updated_count += 1
        else:
            print(f"⏭️  '{problem.title}' already has examples")
            
    except Problem.DoesNotExist:
        print(f"❌ Problem '{data['title']}' not found")
        not_found_count += 1
    except Exception as e:
        print(f"❌ Error updating '{data['title']}': {str(e)}")

print(f"\n📊 Summary:")
print(f"✅ Updated: {updated_count} problems")
print(f"❌ Not found: {not_found_count} problems")
print(f"🎉 Examples added successfully!")