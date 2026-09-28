from quiz.models import Quiz, Question, Choice

# JavaScript Easy Quiz
js_easy = Quiz.objects.create(
    title="JavaScript Basics - Easy",
    description="Test your basic JavaScript knowledge including variables, functions, and DOM basics.",
    category="javascript",
    difficulty="easy",
    time_limit=100
)

js_easy_questions = [
    {
        "text": "What is the output?",
        "code": "console.log(typeof 'Hello');",
        "choices": [
            ("string", True),
            ("String", False),
            ("text", False),
            ("object", False)
        ]
    },
    {
        "text": "How do you declare a variable in JavaScript?",
        "code": "",
        "choices": [
            ("variable x;", False),
            ("var x;", True),
            ("declare x;", False),
            ("x variable;", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "console.log(5 + '5');",
        "choices": [
            ("10", False),
            ("55", True),
            ("Error", False),
            ("NaN", False)
        ]
    },
    {
        "text": "Which method adds an element to the end of an array?",
        "code": "",
        "choices": [
            ("add()", False),
            ("append()", False),
            ("push()", True),
            ("insert()", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "let arr = [1, 2, 3];\nconsole.log(arr.length);",
        "choices": [
            ("2", False),
            ("3", True),
            ("4", False),
            ("undefined", False)
        ]
    },
    {
        "text": "How do you write a single line comment in JavaScript?",
        "code": "",
        "choices": [
            ("# This is a comment", False),
            ("// This is a comment", True),
            ("<!-- This is a comment -->", False),
            ("/* This is a comment", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "console.log(Boolean(0));",
        "choices": [
            ("true", False),
            ("false", True),
            ("0", False),
            ("undefined", False)
        ]
    },
    {
        "text": "Which operator is used for strict equality?",
        "code": "",
        "choices": [
            ("=", False),
            ("==", False),
            ("===", True),
            ("!=", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "let x = 10;\nif (x > 5) {\n    console.log('Greater');\n} else {\n    console.log('Smaller');\n}",
        "choices": [
            ("Greater", True),
            ("Smaller", False),
            ("10", False),
            ("Error", False)
        ]
    },
    {
        "text": "How do you create a function in JavaScript?",
        "code": "",
        "choices": [
            ("function myFunc() {}", True),
            ("def myFunc() {}", False),
            ("create myFunc() {}", False),
            ("func myFunc() {}", False)
        ]
    }
]

for i, q_data in enumerate(js_easy_questions):
    question = Question.objects.create(
        quiz=js_easy,
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

# JavaScript Medium Quiz
js_medium = Quiz.objects.create(
    title="JavaScript Intermediate - Medium",
    description="Test your intermediate JavaScript skills including closures, promises, and ES6 features.",
    category="javascript",
    difficulty="medium",
    time_limit=100
)

js_medium_questions = [
    {
        "text": "What is the output?",
        "code": "console.log(typeof null);",
        "choices": [
            ("null", False),
            ("undefined", False),
            ("object", True),
            ("boolean", False)
        ]
    },
    {
        "text": "What does this arrow function return?",
        "code": "const add = (a, b) => a + b;\nconsole.log(add(2, 3));",
        "choices": [
            ("23", False),
            ("5", True),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "let obj = {a: 1};\nlet obj2 = obj;\nobj2.a = 2;\nconsole.log(obj.a);",
        "choices": [
            ("1", False),
            ("2", True),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does Array.map() return?",
        "code": "let arr = [1, 2, 3];\nlet result = arr.map(x => x * 2);",
        "choices": [
            ("[1, 2, 3]", False),
            ("[2, 4, 6]", True),
            ("6", False),
            ("undefined", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "function outer() {\n    let x = 1;\n    return function inner() {\n        return x++;\n    }\n}\nlet fn = outer();\nconsole.log(fn());\nconsole.log(fn());",
        "choices": [
            ("1 1", False),
            ("1 2", True),
            ("2 2", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does Promise.resolve(5) return?",
        "code": "Promise.resolve(5).then(x => console.log(x));",
        "choices": [
            ("Promise", False),
            ("5", True),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "const {a, b} = {a: 1, b: 2, c: 3};\nconsole.log(a + b);",
        "choices": [
            ("3", True),
            ("6", False),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this spread operator do?",
        "code": "let arr1 = [1, 2];\nlet arr2 = [...arr1, 3, 4];\nconsole.log(arr2);",
        "choices": [
            ("[1, 2, 3, 4]", True),
            ("[[1, 2], 3, 4]", False),
            ("[1, 2]", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "setTimeout(() => console.log('A'), 0);\nconsole.log('B');",
        "choices": [
            ("A B", False),
            ("B A", True),
            ("A", False),
            ("B", False)
        ]
    },
    {
        "text": "What does this template literal produce?",
        "code": "let name = 'World';\nconsole.log(`Hello ${name}!`);",
        "choices": [
            ("Hello World!", True),
            ("Hello ${name}!", False),
            ("Hello name!", False),
            ("Error", False)
        ]
    }
]

for i, q_data in enumerate(js_medium_questions):
    question = Question.objects.create(
        quiz=js_medium,
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

# JavaScript Hard Quiz
js_hard = Quiz.objects.create(
    title="JavaScript Advanced - Hard",
    description="Challenge yourself with advanced JavaScript concepts including prototypes, async/await, and performance optimization.",
    category="javascript",
    difficulty="hard",
    time_limit=100
)

js_hard_questions = [
    {
        "text": "What is the output?",
        "code": "function Person(name) {\n    this.name = name;\n}\nPerson.prototype.greet = function() {\n    return `Hello ${this.name}`;\n}\nlet p = new Person('John');\nconsole.log(p.greet());",
        "choices": [
            ("Hello John", True),
            ("Hello undefined", False),
            ("Error", False),
            ("undefined", False)
        ]
    },
    {
        "text": "What does this async function return?",
        "code": "async function getData() {\n    return 'data';\n}\nconsole.log(typeof getData());",
        "choices": [
            ("string", False),
            ("object", True),
            ("function", False),
            ("undefined", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "let obj = {};\nObject.defineProperty(obj, 'x', {\n    value: 42,\n    writable: false\n});\nobj.x = 100;\nconsole.log(obj.x);",
        "choices": [
            ("42", True),
            ("100", False),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this generator function produce?",
        "code": "function* gen() {\n    yield 1;\n    yield 2;\n    yield 3;\n}\nlet g = gen();\nconsole.log(g.next().value);\nconsole.log(g.next().value);",
        "choices": [
            ("1 1", False),
            ("1 2", True),
            ("undefined undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the time complexity of this algorithm?",
        "code": "function quickSort(arr) {\n    if (arr.length <= 1) return arr;\n    let pivot = arr[0];\n    let left = arr.slice(1).filter(x => x < pivot);\n    let right = arr.slice(1).filter(x => x >= pivot);\n    return [...quickSort(left), pivot, ...quickSort(right)];\n}",
        "choices": [
            ("O(n)", False),
            ("O(n log n)", True),
            ("O(n²)", False),
            ("O(2^n)", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    static getSpecies() {\n        return 'Unknown';\n    }\n}\nlet dog = new Animal('Rex');\nconsole.log(dog.getSpecies());",
        "choices": [
            ("Unknown", False),
            ("Error", True),
            ("Rex", False),
            ("undefined", False)
        ]
    },
    {
        "text": "What does this WeakMap do?",
        "code": "let wm = new WeakMap();\nlet obj = {};\nwm.set(obj, 'value');\nobj = null;\n// What happens to the WeakMap entry?",
        "choices": [
            ("Entry remains", False),
            ("Entry is garbage collected", True),
            ("Error occurs", False),
            ("WeakMap becomes empty", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "let sym1 = Symbol('id');\nlet sym2 = Symbol('id');\nconsole.log(sym1 === sym2);",
        "choices": [
            ("true", False),
            ("false", True),
            ("Error", False),
            ("undefined", False)
        ]
    },
    {
        "text": "What does this Proxy do?",
        "code": "let obj = {a: 1};\nlet proxy = new Proxy(obj, {\n    get(target, prop) {\n        return target[prop] * 2;\n    }\n});\nconsole.log(proxy.a);",
        "choices": [
            ("1", False),
            ("2", True),
            ("undefined", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "Promise.all([\n    Promise.resolve(1),\n    Promise.resolve(2),\n    Promise.reject('error')\n]).catch(err => console.log(err));",
        "choices": [
            ("[1, 2]", False),
            ("error", True),
            ("undefined", False),
            ("Error", False)
        ]
    }
]

for i, q_data in enumerate(js_hard_questions):
    question = Question.objects.create(
        quiz=js_hard,
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

print("JavaScript quizzes created successfully!")
print("- JavaScript Basics - Easy (10 questions)")
print("- JavaScript Intermediate - Medium (10 questions)")
print("- JavaScript Advanced - Hard (10 questions)")