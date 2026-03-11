from quiz.models import Quiz, Question, Choice

# Delete existing quizzes to start fresh
Quiz.objects.all().delete()

# Python Easy Quiz
python_easy = Quiz.objects.create(
    title="Python Basics - Easy",
    description="Test your basic Python knowledge including variables, data types, and simple operations.",
    category="python",
    difficulty="easy",
    time_limit=100  # 10 questions * 10 seconds
)

questions_data = [
    {
        "text": "What is the output of print(type(5))?",
        "code": "print(type(5))",
        "choices": [
            ("<class 'int'>", True),
            ("<class 'float'>", False),
            ("<class 'str'>", False),
            ("int", False)
        ]
    },
    {
        "text": "Which of the following is used to create a comment in Python?",
        "code": "",
        "choices": [
            ("//", False),
            ("/* */", False),
            ("#", True),
            ("<!-- -->", False)
        ]
    },
    {
        "text": "What will be the output?",
        "code": "x = 'Hello'\nprint(x[1])",
        "choices": [
            ("H", False),
            ("e", True),
            ("l", False),
            ("o", False)
        ]
    },
    {
        "text": "Which method is used to add an element to a list?",
        "code": "",
        "choices": [
            ("add()", False),
            ("append()", True),
            ("insert()", False),
            ("push()", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "print(len('Python'))",
        "choices": [
            ("5", False),
            ("6", True),
            ("7", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which operator is used for exponentiation in Python?",
        "code": "",
        "choices": [
            ("^", False),
            ("**", True),
            ("pow", False),
            ("exp", False)
        ]
    },
    {
        "text": "What will this print?",
        "code": "print(3 + 2 * 4)",
        "choices": [
            ("20", False),
            ("11", True),
            ("14", False),
            ("Error", False)
        ]
    },
    {
        "text": "How do you create an empty list in Python?",
        "code": "",
        "choices": [
            ("list = {}", False),
            ("list = []", True),
            ("list = ()", False),
            ("list = None", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "print('Python'[0:3])",
        "choices": [
            ("Pyt", True),
            ("Pyth", False),
            ("Python", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which keyword is used to define a function in Python?",
        "code": "",
        "choices": [
            ("function", False),
            ("def", True),
            ("func", False),
            ("define", False)
        ]
    }
]

for i, q_data in enumerate(questions_data):
    question = Question.objects.create(
        quiz=python_easy,
        question_text=q_data["text"],
        code_snippet=q_data["code"],
        points=10,
        order=i+1
    )
    for choice_text, is_correct in q_data["choices"]:
        Choice.objects.create(
            question=question,
            choice_text=choice_text,
            is_correct=is_correct
        )

# Python Medium Quiz
python_medium = Quiz.objects.create(
    title="Python Intermediate - Medium",
    description="Test your intermediate Python skills including functions, classes, and data structures.",
    category="python",
    difficulty="medium",
    time_limit=100
)

medium_questions = [
    {
        "text": "What will be the output?",
        "code": "def func(x=[]):\n    x.append(1)\n    return x\nprint(func())\nprint(func())",
        "choices": [
            ("[1] [1]", False),
            ("[1] [1, 1]", True),
            ("Error", False),
            ("[1, 1] [1, 1]", False)
        ]
    },
    {
        "text": "What is the result of list(range(3))?",
        "code": "print(list(range(3)))",
        "choices": [
            ("[1, 2, 3]", False),
            ("[0, 1, 2]", True),
            ("[0, 1, 2, 3]", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this comprehension create?",
        "code": "[x**2 for x in range(5) if x % 2 == 0]",
        "choices": [
            ("[0, 4, 16]", True),
            ("[0, 1, 4, 9, 16]", False),
            ("[1, 9]", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "x = {'a': 1, 'b': 2}\nprint(x.get('c', 'default'))",
        "choices": [
            ("None", False),
            ("Error", False),
            ("default", True),
            ("c", False)
        ]
    },
    {
        "text": "What will this lambda function return?",
        "code": "f = lambda x, y: x + y\nprint(f(2, 3))",
        "choices": [
            ("23", False),
            ("5", True),
            ("Error", False),
            ("None", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "try:\n    print(10/0)\nexcept ZeroDivisionError:\n    print('Error caught')",
        "choices": [
            ("10/0", False),
            ("Error caught", True),
            ("Error", False),
            ("None", False)
        ]
    },
    {
        "text": "What does enumerate() return?",
        "code": "list(enumerate(['a', 'b', 'c']))",
        "choices": [
            ("[(0, 'a'), (1, 'b'), (2, 'c')]", True),
            ("[0, 1, 2]", False),
            ("['a', 'b', 'c']", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "class A:\n    x = 1\na = A()\nb = A()\na.x = 2\nprint(b.x)",
        "choices": [
            ("1", True),
            ("2", False),
            ("Error", False),
            ("None", False)
        ]
    },
    {
        "text": "What does zip() do?",
        "code": "list(zip([1, 2], ['a', 'b']))",
        "choices": [
            ("[(1, 'a'), (2, 'b')]", True),
            ("[1, 2, 'a', 'b']", False),
            ("Error", False),
            ("None", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "def decorator(func):\n    def wrapper():\n        return func() * 2\n    return wrapper\n\n@decorator\ndef get_num():\n    return 5\n\nprint(get_num())",
        "choices": [
            ("5", False),
            ("10", True),
            ("Error", False),
            ("None", False)
        ]
    }
]

for i, q_data in enumerate(medium_questions):
    question = Question.objects.create(
        quiz=python_medium,
        question_text=q_data["text"],
        code_snippet=q_data["code"],
        points=10,
        order=i+1
    )
    for choice_text, is_correct in q_data["choices"]:
        Choice.objects.create(
            question=question,
            choice_text=choice_text,
            is_correct=is_correct
        )

# Python Hard Quiz
python_hard = Quiz.objects.create(
    title="Python Advanced - Hard",
    description="Challenge yourself with advanced Python concepts including metaclasses, generators, and complex algorithms.",
    category="python",
    difficulty="hard",
    time_limit=100
)

hard_questions = [
    {
        "text": "What is the output?",
        "code": "def gen():\n    yield 1\n    yield 2\n    yield 3\n\ng = gen()\nprint(next(g))\nprint(next(g))",
        "choices": [
            ("1 1", False),
            ("1 2", True),
            ("Error", False),
            ("None", False)
        ]
    },
    {
        "text": "What does this metaclass do?",
        "code": "class Meta(type):\n    def __new__(cls, name, bases, attrs):\n        attrs['x'] = 100\n        return super().__new__(cls, name, bases, attrs)\n\nclass A(metaclass=Meta):\n    pass\n\nprint(A.x)",
        "choices": [
            ("Error", False),
            ("100", True),
            ("None", False),
            ("0", False)
        ]
    },
    {
        "text": "What is the time complexity of this algorithm?",
        "code": "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]",
        "choices": [
            ("O(n)", False),
            ("O(n log n)", False),
            ("O(n²)", True),
            ("O(2^n)", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "import sys\nprint(sys.getsizeof([]) < sys.getsizeof(()))",
        "choices": [
            ("True", False),
            ("False", True),
            ("Error", False),
            ("Depends", False)
        ]
    },
    {
        "text": "What does this context manager do?",
        "code": "class CM:\n    def __enter__(self):\n        print('Enter')\n        return self\n    def __exit__(self, *args):\n        print('Exit')\n\nwith CM() as cm:\n    print('Inside')",
        "choices": [
            ("Enter Inside Exit", True),
            ("Inside Enter Exit", False),
            ("Error", False),
            ("Enter Exit", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "def closure():\n    x = 10\n    def inner():\n        nonlocal x\n        x += 1\n        return x\n    return inner\n\nf = closure()\nprint(f())\nprint(f())",
        "choices": [
            ("10 10", False),
            ("11 11", False),
            ("11 12", True),
            ("Error", False)
        ]
    },
    {
        "text": "What is the space complexity of merge sort?",
        "code": "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)",
        "choices": [
            ("O(1)", False),
            ("O(log n)", False),
            ("O(n)", True),
            ("O(n²)", False)
        ]
    },
    {
        "text": "What does this descriptor do?",
        "code": "class Desc:\n    def __get__(self, obj, owner):\n        return 42\n    def __set__(self, obj, value):\n        pass\n\nclass A:\n    x = Desc()\n\na = A()\nprint(a.x)",
        "choices": [
            ("Error", False),
            ("42", True),
            ("None", False),
            ("Desc object", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "def fib(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 2:\n        return 1\n    memo[n] = fib(n-1, memo) + fib(n-2, memo)\n    return memo[n]\n\nprint(fib(5))",
        "choices": [
            ("5", True),
            ("8", False),
            ("Error", False),
            ("13", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "class Singleton(type):\n    _instances = {}\n    def __call__(cls, *args, **kwargs):\n        if cls not in cls._instances:\n            cls._instances[cls] = super().__call__(*args, **kwargs)\n        return cls._instances[cls]\n\nclass A(metaclass=Singleton):\n    pass\n\na1 = A()\na2 = A()\nprint(a1 is a2)",
        "choices": [
            ("True", True),
            ("False", False),
            ("Error", False),
            ("None", False)
        ]
    }
]

for i, q_data in enumerate(hard_questions):
    question = Question.objects.create(
        quiz=python_hard,
        question_text=q_data["text"],
        code_snippet=q_data["code"],
        points=10,
        order=i+1
    )
    for choice_text, is_correct in q_data["choices"]:
        Choice.objects.create(
            question=question,
            choice_text=choice_text,
            is_correct=is_correct
        )

print("Python quizzes created successfully!")
print("- Python Basics - Easy (10 questions)")
print("- Python Intermediate - Medium (10 questions)")
print("- Python Advanced - Hard (10 questions)")