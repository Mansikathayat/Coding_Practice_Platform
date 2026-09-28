from quiz.models import Quiz, Question, Choice

# Java Easy Quiz
java_easy = Quiz.objects.create(
    title="Java Basics - Easy",
    description="Test your basic Java knowledge including syntax, data types, and simple OOP concepts.",
    category="java",
    difficulty="easy",
    time_limit=100
)

java_easy_questions = [
    {
        "text": "What is the output?",
        "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello\".length());\n    }\n}",
        "choices": [
            ("4", False),
            ("5", True),
            ("6", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which keyword is used to create a class in Java?",
        "code": "",
        "choices": [
            ("create", False),
            ("class", True),
            ("new", False),
            ("object", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "int x = 10;\nint y = 3;\nSystem.out.println(x / y);",
        "choices": [
            ("3.33", False),
            ("3", True),
            ("4", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which method is the entry point of a Java program?",
        "code": "",
        "choices": [
            ("start()", False),
            ("main()", True),
            ("run()", False),
            ("begin()", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "String str = \"Java\";\nSystem.out.println(str.charAt(1));",
        "choices": [
            ("J", False),
            ("a", True),
            ("v", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which data type is used to store a single character?",
        "code": "",
        "choices": [
            ("String", False),
            ("char", True),
            ("character", False),
            ("text", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "boolean flag = true;\nif (flag) {\n    System.out.println(\"True\");\n} else {\n    System.out.println(\"False\");\n}",
        "choices": [
            ("True", True),
            ("False", False),
            ("true", False),
            ("Error", False)
        ]
    },
    {
        "text": "How do you create an array in Java?",
        "code": "",
        "choices": [
            ("int[] arr = new int[5];", True),
            ("int arr[] = [5];", False),
            ("array int arr = new int[5];", False),
            ("int arr = new array[5];", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "for (int i = 0; i < 3; i++) {\n    System.out.print(i + \" \");\n}",
        "choices": [
            ("1 2 3", False),
            ("0 1 2", True),
            ("0 1 2 3", False),
            ("Error", False)
        ]
    },
    {
        "text": "Which keyword is used for inheritance in Java?",
        "code": "",
        "choices": [
            ("inherits", False),
            ("extends", True),
            ("implements", False),
            ("super", False)
        ]
    }
]

for i, q_data in enumerate(java_easy_questions):
    question = Question.objects.create(
        quiz=java_easy,
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

# Java Medium Quiz
java_medium = Quiz.objects.create(
    title="Java Intermediate - Medium",
    description="Test your intermediate Java skills including collections, exceptions, and advanced OOP.",
    category="java",
    difficulty="medium",
    time_limit=100
)

java_medium_questions = [
    {
        "text": "What is the output?",
        "code": "List<String> list = new ArrayList<>();\nlist.add(\"Java\");\nlist.add(\"Python\");\nSystem.out.println(list.get(0));",
        "choices": [
            ("Java", True),
            ("Python", False),
            ("0", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this code do?",
        "code": "try {\n    int result = 10 / 0;\n} catch (ArithmeticException e) {\n    System.out.println(\"Division by zero\");\n}",
        "choices": [
            ("Prints the result", False),
            ("Prints 'Division by zero'", True),
            ("Throws an exception", False),
            ("Compilation error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "class Animal {\n    void sound() { System.out.println(\"Animal sound\"); }\n}\nclass Dog extends Animal {\n    void sound() { System.out.println(\"Bark\"); }\n}\nAnimal a = new Dog();\na.sound();",
        "choices": [
            ("Animal sound", False),
            ("Bark", True),
            ("Error", False),
            ("Both", False)
        ]
    },
    {
        "text": "What does HashMap store?",
        "code": "HashMap<String, Integer> map = new HashMap<>();\nmap.put(\"Java\", 8);\nmap.put(\"Python\", 3);",
        "choices": [
            ("Only keys", False),
            ("Only values", False),
            ("Key-value pairs", True),
            ("Arrays", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "String s1 = \"Hello\";\nString s2 = \"Hello\";\nSystem.out.println(s1 == s2);",
        "choices": [
            ("true", True),
            ("false", False),
            ("Error", False),
            ("null", False)
        ]
    },
    {
        "text": "What does the 'final' keyword do?",
        "code": "final int x = 10;\n// x = 20; // This line",
        "choices": [
            ("Makes variable mutable", False),
            ("Makes variable immutable", True),
            ("Creates a constant class", False),
            ("Nothing special", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "interface Drawable {\n    void draw();\n}\nclass Circle implements Drawable {\n    public void draw() {\n        System.out.println(\"Drawing Circle\");\n    }\n}\nDrawable d = new Circle();\nd.draw();",
        "choices": [
            ("Drawing Circle", True),
            ("Error", False),
            ("Nothing", False),
            ("Compilation error", False)
        ]
    },
    {
        "text": "What does this lambda expression do?",
        "code": "List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\nnumbers.stream().filter(n -> n % 2 == 0).forEach(System.out::println);",
        "choices": [
            ("Prints all numbers", False),
            ("Prints even numbers", True),
            ("Prints odd numbers", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "class Outer {\n    class Inner {\n        void display() {\n            System.out.println(\"Inner class\");\n        }\n    }\n}\nOuter.Inner inner = new Outer().new Inner();\ninner.display();",
        "choices": [
            ("Inner class", True),
            ("Outer class", False),
            ("Error", False),
            ("Nothing", False)
        ]
    },
    {
        "text": "What does Collections.sort() do?",
        "code": "List<Integer> list = Arrays.asList(3, 1, 4, 1, 5);\nCollections.sort(list);\nSystem.out.println(list);",
        "choices": [
            ("Sorts in descending order", False),
            ("Sorts in ascending order", True),
            ("Reverses the list", False),
            ("Error", False)
        ]
    }
]

for i, q_data in enumerate(java_medium_questions):
    question = Question.objects.create(
        quiz=java_medium,
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

# Java Hard Quiz
java_hard = Quiz.objects.create(
    title="Java Advanced - Hard",
    description="Challenge yourself with advanced Java concepts including concurrency, generics, and JVM internals.",
    category="java",
    difficulty="hard",
    time_limit=100
)

java_hard_questions = [
    {
        "text": "What is the output?",
        "code": "class Test {\n    static {\n        System.out.println(\"Static block\");\n    }\n    {\n        System.out.println(\"Instance block\");\n    }\n    Test() {\n        System.out.println(\"Constructor\");\n    }\n}\nTest t = new Test();",
        "choices": [
            ("Constructor, Instance block, Static block", False),
            ("Static block, Instance block, Constructor", True),
            ("Instance block, Static block, Constructor", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this generic method do?",
        "code": "public static <T extends Comparable<T>> T max(T a, T b) {\n    return a.compareTo(b) > 0 ? a : b;\n}",
        "choices": [
            ("Returns minimum value", False),
            ("Returns maximum value", True),
            ("Compares objects", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the time complexity of HashMap get() operation?",
        "code": "HashMap<String, Integer> map = new HashMap<>();\nmap.put(\"key\", 100);\nint value = map.get(\"key\");",
        "choices": [
            ("O(1) average case", True),
            ("O(log n)", False),
            ("O(n)", False),
            ("O(n²)", False)
        ]
    },
    {
        "text": "What does this thread code do?",
        "code": "class MyThread extends Thread {\n    public void run() {\n        for (int i = 0; i < 5; i++) {\n            System.out.println(Thread.currentThread().getName() + \": \" + i);\n            try { Thread.sleep(100); } catch (Exception e) {}\n        }\n    }\n}",
        "choices": [
            ("Runs in main thread", False),
            ("Creates a new thread", True),
            ("Blocks the main thread", False),
            ("Error", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "String s1 = new String(\"Hello\");\nString s2 = new String(\"Hello\");\nSystem.out.println(s1 == s2);\nSystem.out.println(s1.equals(s2));",
        "choices": [
            ("true true", False),
            ("false true", True),
            ("true false", False),
            ("false false", False)
        ]
    },
    {
        "text": "What does this annotation do?",
        "code": "@Override\npublic String toString() {\n    return \"Custom toString\";\n}",
        "choices": [
            ("Creates a new method", False),
            ("Overrides parent method", True),
            ("Implements interface", False),
            ("Nothing", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "enum Day { MONDAY, TUESDAY, WEDNESDAY }\nDay day = Day.MONDAY;\nswitch (day) {\n    case MONDAY:\n        System.out.println(\"Start of week\");\n        break;\n    default:\n        System.out.println(\"Other day\");\n}",
        "choices": [
            ("Start of week", True),
            ("Other day", False),
            ("MONDAY", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does synchronized keyword do?",
        "code": "synchronized void method() {\n    // Critical section\n}",
        "choices": [
            ("Makes method faster", False),
            ("Prevents concurrent access", True),
            ("Makes method static", False),
            ("Nothing", False)
        ]
    },
    {
        "text": "What is the output?",
        "code": "Optional<String> opt = Optional.of(\"Hello\");\nopt.ifPresent(System.out::println);\nopt.orElse(\"Default\");",
        "choices": [
            ("Hello", True),
            ("Default", False),
            ("Optional[Hello]", False),
            ("Error", False)
        ]
    },
    {
        "text": "What does this reflection code do?",
        "code": "Class<?> clazz = String.class;\nMethod[] methods = clazz.getDeclaredMethods();\nSystem.out.println(methods.length > 0);",
        "choices": [
            ("false", False),
            ("true", True),
            ("Error", False),
            ("0", False)
        ]
    }
]

for i, q_data in enumerate(java_hard_questions):
    question = Question.objects.create(
        quiz=java_hard,
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

print("Java quizzes created successfully!")
print("- Java Basics - Easy (10 questions)")
print("- Java Intermediate - Medium (10 questions)")
print("- Java Advanced - Hard (10 questions)")