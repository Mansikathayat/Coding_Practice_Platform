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
    }
]

for data in problems_data:
    try:
        problem = Problem.objects.get(title=data['title'])
        # Update description to include example
        if 'Example:' not in problem.description:
            problem.description += f"\n\n**Example:**\n{data['example']}"
            problem.save()
            print(f"Updated {problem.title} with example")
    except Problem.DoesNotExist:
        print(f"Problem '{data['title']}' not found")

print("Examples added to problems!")