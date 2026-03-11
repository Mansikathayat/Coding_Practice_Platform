from quiz.models import Quiz, Question, Choice

# Create Python Basics Quiz
python_quiz = Quiz.objects.create(
    title="Python Fundamentals",
    description="Test your knowledge of Python basics including variables, data types, and control structures.",
    category="python",
    difficulty="easy",
    time_limit=600
)

# Question 1
q1 = Question.objects.create(
    quiz=python_quiz,
    question_text="What is the output of the following Python code?",
    question_type="code",
    code_snippet="x = [1, 2, 3]\nprint(len(x))",
    points=10,
    order=1
)

Choice.objects.create(question=q1, choice_text="1", is_correct=False)
Choice.objects.create(question=q1, choice_text="2", is_correct=False)
Choice.objects.create(question=q1, choice_text="3", is_correct=True)
Choice.objects.create(question=q1, choice_text="4", is_correct=False)

# Question 2
q2 = Question.objects.create(
    quiz=python_quiz,
    question_text="Which of the following is a mutable data type in Python?",
    question_type="mcq",
    points=10,
    order=2
)

Choice.objects.create(question=q2, choice_text="String", is_correct=False)
Choice.objects.create(question=q2, choice_text="Tuple", is_correct=False)
Choice.objects.create(question=q2, choice_text="List", is_correct=True)
Choice.objects.create(question=q2, choice_text="Integer", is_correct=False)

# Question 3
q3 = Question.objects.create(
    quiz=python_quiz,
    question_text="What will this code print?",
    question_type="code",
    code_snippet="for i in range(3):\n    print(i, end=' ')",
    points=10,
    order=3
)

Choice.objects.create(question=q3, choice_text="1 2 3", is_correct=False)
Choice.objects.create(question=q3, choice_text="0 1 2", is_correct=True)
Choice.objects.create(question=q3, choice_text="0 1 2 3", is_correct=False)
Choice.objects.create(question=q3, choice_text="Error", is_correct=False)

# Create JavaScript Quiz
js_quiz = Quiz.objects.create(
    title="JavaScript Essentials",
    description="Test your JavaScript knowledge including variables, functions, and DOM manipulation.",
    category="javascript",
    difficulty="medium",
    time_limit=900
)

# JS Question 1
js_q1 = Question.objects.create(
    quiz=js_quiz,
    question_text="What is the output of this JavaScript code?",
    question_type="code",
    code_snippet="console.log(typeof null);",
    points=15,
    order=1
)

Choice.objects.create(question=js_q1, choice_text="null", is_correct=False)
Choice.objects.create(question=js_q1, choice_text="undefined", is_correct=False)
Choice.objects.create(question=js_q1, choice_text="object", is_correct=True)
Choice.objects.create(question=js_q1, choice_text="string", is_correct=False)

# JS Question 2
js_q2 = Question.objects.create(
    quiz=js_quiz,
    question_text="Which method is used to add an element to the end of an array?",
    question_type="mcq",
    points=15,
    order=2
)

Choice.objects.create(question=js_q2, choice_text="push()", is_correct=True)
Choice.objects.create(question=js_q2, choice_text="pop()", is_correct=False)
Choice.objects.create(question=js_q2, choice_text="shift()", is_correct=False)
Choice.objects.create(question=js_q2, choice_text="unshift()", is_correct=False)

# Create Algorithms Quiz
algo_quiz = Quiz.objects.create(
    title="Algorithm Fundamentals",
    description="Test your understanding of basic algorithms and data structures.",
    category="algorithms",
    difficulty="hard",
    time_limit=1200
)

# Algo Question 1
algo_q1 = Question.objects.create(
    quiz=algo_quiz,
    question_text="What is the time complexity of binary search?",
    question_type="mcq",
    points=20,
    order=1
)

Choice.objects.create(question=algo_q1, choice_text="O(n)", is_correct=False)
Choice.objects.create(question=algo_q1, choice_text="O(log n)", is_correct=True)
Choice.objects.create(question=algo_q1, choice_text="O(n log n)", is_correct=False)
Choice.objects.create(question=algo_q1, choice_text="O(n²)", is_correct=False)

print("Sample quizzes created successfully!")
print("- Python Fundamentals (Easy)")
print("- JavaScript Essentials (Medium)")  
print("- Algorithm Fundamentals (Hard)")