from problems.models import Problem

problems_data = [
    {
        'title': 'Reverse String',
        'example': 'Input: \"hello\"\\nOutput: \"olleh\"'
    },
    {
        'title': 'Palindrome Check', 
        'example': 'Input: \"racecar\"\\nOutput: True'
    },
    {
        'title': 'FizzBuzz',
        'example': 'Input: 15\\nOutput: [\"1\", \"2\", \"Fizz\", \"4\", \"Buzz\", \"Fizz\", \"7\", \"8\", \"Fizz\", \"Buzz\", \"11\", \"Fizz\", \"13\", \"14\", \"FizzBuzz\"]'
    },
    {
        'title': 'Find Maximum',
        'example': 'Input: [3, 1, 4, 1, 5, 9, 2, 6]\\nOutput: 9'
    },
    {
        'title': 'Count Vowels',
        'example': 'Input: \"hello world\"\\nOutput: 3'
    }
]

for data in problems_data:
    try:
        problem = Problem.objects.get(title=data['title'])
        if 'Example:' not in problem.description:
            problem.description += '\\n\\nExample:\\n' + data['example']
            problem.save()
            print('Updated ' + problem.title)
    except Problem.DoesNotExist:
        print('Problem not found: ' + data['title'])

print('Done!')