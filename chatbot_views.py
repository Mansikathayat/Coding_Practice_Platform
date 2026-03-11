from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import google.generativeai as genai
import os

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyDummy-Replace-With-Your-Key')
genai.configure(api_key=GEMINI_API_KEY)

@login_required
def chatbot_view(request):
    """Render the chatbot interface"""
    return render(request, 'chatbot.html')

@csrf_exempt
def chat_api(request):
    """Handle chat API requests"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Method not allowed'})
    
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'success': False, 'error': 'Message is required'})
        
        # Get AI response from Gemini
        ai_response = get_gemini_response(user_message)
        
        return JsonResponse({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def get_gemini_response(message):
    """Get response from Google Gemini API"""
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-pro')
        
        # Enhanced programming-focused prompt
        prompt = f"""You are an expert programming assistant for CodeMaster, a coding practice platform. 
        
Your role:
        - Answer ANY programming question clearly and concisely
        - Provide complete, working code examples
        - Support Python, Java, and JavaScript
        - Explain algorithms, data structures, and concepts
        - Help with debugging and best practices
        - Give step-by-step solutions
        
User question: {message}
        
Provide a comprehensive, helpful response with code examples when relevant. Format code in markdown blocks."""
        
        # Generate response with higher confidence
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.7,
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': 1000,
            }
        )
        
        if response and response.text:
            return response.text
        else:
            return get_fallback_response(message)
            
    except Exception as e:
        print(f"Gemini API Error: {e}")
        # Try with simpler prompt if main one fails
        try:
            model = genai.GenerativeModel('gemini-pro')
            simple_prompt = f"Answer this programming question with code examples: {message}"
            response = model.generate_content(simple_prompt)
            if response and response.text:
                return response.text
        except:
            pass
        
        return get_fallback_response(message)

def get_fallback_response(message):
    """Enhanced fallback responses for any programming question"""
    message_lower = message.lower()
    
    # Linked List operations
    if 'linked list' in message_lower:
        if 'palindrome' in message_lower:
            return get_linked_list_palindrome_code(message_lower)
        elif 'reverse' in message_lower:
            return get_linked_list_reverse_code(message_lower)
        elif 'cycle' in message_lower or 'loop' in message_lower:
            return get_linked_list_cycle_code(message_lower)
        else:
            return get_linked_list_basic_code(message_lower)
    
    # String operations
    elif 'reverse' in message_lower and ('str' in message_lower or 'string' in message_lower):
        return get_string_reversal_code(message_lower)
    elif 'isomorphic' in message_lower and ('string' in message_lower or 'str' in message_lower):
        return get_isomorphic_strings_code(message_lower)
    elif 'palindrome' in message_lower:
        return get_palindrome_code(message_lower)
    elif 'length' in message_lower and ('str' in message_lower or 'string' in message_lower):
        return get_string_length_code(message_lower)
    
    # Array/List operations
    elif 'sort' in message_lower and ('array' in message_lower or 'list' in message_lower):
        return get_sorting_code(message_lower)
    elif 'search' in message_lower and ('array' in message_lower or 'list' in message_lower):
        return get_search_code(message_lower)
    elif 'max' in message_lower or 'min' in message_lower:
        return get_max_min_code(message_lower)
    
    # Mathematical operations
    elif 'factorial' in message_lower:
        return get_factorial_code(message_lower)
    elif 'fibonacci' in message_lower:
        return get_fibonacci_code(message_lower)
    elif 'prime' in message_lower:
        return get_prime_code(message_lower)
    elif 'sum' in message_lower or 'add' in message_lower:
        return get_sum_code(message_lower)
    
    # Control structures
    elif 'loop' in message_lower or 'for' in message_lower or 'while' in message_lower:
        return get_loop_examples(message_lower)
    elif 'if' in message_lower or 'condition' in message_lower:
        return get_conditional_examples(message_lower)
    
    # Data structures
    elif 'class' in message_lower or 'object' in message_lower:
        return get_class_examples(message_lower)
    elif 'function' in message_lower or 'method' in message_lower:
        return get_function_examples(message_lower)
    
    # File operations
    elif 'file' in message_lower and ('read' in message_lower or 'write' in message_lower):
        return get_file_operations(message_lower)
    
    # Hello World and basic programs
    elif 'hello' in message_lower:
        return get_hello_programs(message_lower)
    
    # General programming help
    else:
        return get_general_programming_help(message)

def get_isomorphic_strings_code(msg):
    if 'java' in msg:
        return """☕ **Java - Check if Strings are Isomorphic:**

```java
import java.util.HashMap;
import java.util.Map;

public class IsomorphicStrings {
    
    public boolean areIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Character> mapS = new HashMap<>();
        Map<Character, Character> mapT = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);
            
            // Check mapping from s to t
            if (mapS.containsKey(charS)) {
                if (mapS.get(charS) != charT) {
                    return false;
                }
            } else {
                mapS.put(charS, charT);
            }
            
            // Check mapping from t to s
            if (mapT.containsKey(charT)) {
                if (mapT.get(charT) != charS) {
                    return false;
                }
            } else {
                mapT.put(charT, charS);
            }
        }
        
        return true;
    }
    
    public static void main(String[] args) {
        IsomorphicStrings solution = new IsomorphicStrings();
        
        System.out.println(solution.areIsomorphic("egg", "add"));    // true
        System.out.println(solution.areIsomorphic("foo", "bar"));    // false
        System.out.println(solution.areIsomorphic("paper", "title")); // true
    }
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - at most 256 characters

**Algorithm:**
1. Check if strings have same length
2. Use two HashMaps for bidirectional mapping
3. For each character pair, verify consistent mapping
4. Return true if all mappings are consistent

🚀"""
    else:
        return """🐍 **Python - Check if Strings are Isomorphic:**

```python
def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    # Two dictionaries for bidirectional mapping
    map_s_to_t = {}
    map_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check mapping from s to t
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t
        
        # Check mapping from t to s
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s
    
    return True

# Alternative solution using transformation
def are_isomorphic_v2(s, t):
    def transform(string):
        mapping = {}
        result = []
        next_num = 0
        
        for char in string:
            if char not in mapping:
                mapping[char] = next_num
                next_num += 1
            result.append(mapping[char])
        
        return result
    
    return transform(s) == transform(t)

# Test examples
if __name__ == "__main__":
    test_cases = [
        ("egg", "add"),      # True
        ("foo", "bar"),      # False
        ("paper", "title"),  # True
        ("ab", "aa"),        # False
        ("abc", "def")       # True
    ]
    
    for s, t in test_cases:
        result = are_isomorphic(s, t)
        print(f"'{s}' and '{t}': {result}")
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - at most 256 characters

**What are Isomorphic Strings?**
Two strings are isomorphic if characters in one string can be replaced to get the other string. All occurrences of a character must be replaced with the same character, and no two characters can map to the same character.

**Examples:**
- "egg" and "add" → e→a, g→d ✓
- "foo" and "bar" → f→b, o→a, o→r (o maps to both a and r) ✗

🚀"""

def get_string_reversal_code(msg):
    if 'java' in msg:
        return """☕ **Java String Reversal:**
```java
String str = "hello";
String reversed = new StringBuilder(str).reverse().toString();
System.out.println(reversed); // olleh
```"""
    else:
        return """🐍 **Python String Reversal:**
```python
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # olleh
```"""

def get_sum_code(msg):
    if 'java' in msg:
        return """☕ **Java Sum Program:**
```java
int a = 5, b = 10;
int sum = a + b;
System.out.println("Sum: " + sum);
```"""
    else:
        return """🐍 **Python Sum Program:**
```python
a, b = 5, 10
sum_result = a + b
print(f"Sum: {sum_result}")
```"""

def get_factorial_code(msg):
    if 'java' in msg:
        return """☕ **Java Factorial:**
```java
public static int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```"""
    else:
        return """🐍 **Python Factorial:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```"""

def get_fibonacci_code(msg):
    return """🔢 **Fibonacci Sequence:**

**Python:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Print first 10 numbers
for i in range(10):
    print(fibonacci(i), end=" ")
```

**Java:**
```java
public static int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
```"""

def get_prime_code(msg):
    return """🔍 **Prime Number Check:**

**Python:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
```

**Java:**
```java
public static boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```"""

def get_hello_programs(msg):
    return """🌟 **Hello Programs:**

**Python:** `print("Hello World")`
**Java:** `System.out.println("Hello World");`
**JavaScript:** `console.log("Hello World");`"""

def get_general_programming_help(message):
    return f"""💡 **I can help with programming!**

Your question: "{message}"

**I can help with:**
• 🐍 Python, ☕ Java, ⚡ JavaScript programs
• 🔄 String operations (reverse, palindrome, etc.)
• 🔢 Math problems (factorial, fibonacci, prime)
• 📋 Arrays and sorting algorithms
• 🔄 Loops, conditions, functions
• 📝 File operations and data structures

**Try asking:**
• "Write a Python program to..."
• "How to reverse a string in Java?"
• "Fibonacci sequence code"
• "Sort an array in Python"

Be specific and I'll provide complete code! 🚀"""

# Additional helper functions for other patterns
def get_linked_list_palindrome_code(msg):
    if 'java' in msg:
        return """☕ **Java - Check if Linked List is Palindrome:**

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class LinkedListPalindrome {
    
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        
        // Find middle of linked list
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Reverse second half
        ListNode secondHalf = reverseList(slow);
        ListNode firstHalf = head;
        
        // Compare both halves
        while (secondHalf != null) {
            if (firstHalf.val != secondHalf.val) {
                return false;
            }
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        
        return true;
    }
    
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode nextTemp = current.next;
            current.next = prev;
            prev = current;
            current = nextTemp;
        }
        
        return prev;
    }
    
    // Test method
    public static void main(String[] args) {
        LinkedListPalindrome solution = new LinkedListPalindrome();
        
        // Create palindrome: 1 -> 2 -> 2 -> 1
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(1);
        
        System.out.println(solution.isPalindrome(head)); // true
    }
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Algorithm:**
1. Find middle using slow/fast pointers
2. Reverse second half of list
3. Compare first and second halves
4. Return true if all values match

🚀"""
    else:
        return """🐍 **Python - Check if Linked List is Palindrome:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True
    
    # Find middle of linked list
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        current = node
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev
    
    second_half = reverse_list(slow)
    first_half = head
    
    # Compare both halves
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Test example
if __name__ == "__main__":
    # Create palindrome: 1 -> 2 -> 2 -> 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    
    print(is_palindrome(head))  # True
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🚀"""

def get_linked_list_reverse_code(msg):
    if 'python' in msg:
        return """🐍 **Python - Reverse Linked List:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    # Reverse a linked list iteratively
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # prev is now the new head

# Test example
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    # Reverse the list
    reversed_head = reverse_list(head)
    
    # Print result: 5 -> 4 -> 3 -> 2 -> 1
    current = reversed_head
    while current:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🚀"""
    elif 'java' in msg:
        return """☕ **Java - Reverse Linked List:**

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode current = head;
    
    while (current != null) {
        ListNode nextTemp = current.next;
        current.next = prev;
        prev = current;
        current = nextTemp;
    }
    
    return prev;
}
```"""
    else:
        return """🔄 **Reverse Linked List:**

**Python:**
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

**Java:**
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode current = head;
    
    while (current != null) {
        ListNode nextTemp = current.next;
        current.next = prev;
        prev = current;
        current = nextTemp;
    }
    
    return prev;
}
```

🚀"""

def get_linked_list_cycle_code(msg):
    return """🔄 **Detect Cycle in Linked List:**

```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```"""

def get_linked_list_basic_code(msg):
    return """🔗 **Basic Linked List Operations:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
```"""

def get_palindrome_code(msg):
    return """🔄 **Palindrome Check:**
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
```"""

def get_sorting_code(msg):
    return """📋 **Array Sorting:**
```python
arr = [64, 34, 25, 12, 22, 11, 90]
arr.sort()  # Built-in sort
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```"""

def get_loop_examples(msg):
    return """🔄 **Loop Examples:**
```python
# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
```"""

def get_function_examples(msg):
    return """⚡ **Function Examples:**
```python
def greet(name):
    return f"Hello, {name}!"

result = greet("World")
print(result)  # Hello, World!
```"""

# Placeholder functions for other patterns
def get_string_length_code(msg): return "Length: `len(string)` in Python, `string.length()` in Java"
def get_search_code(msg): return "Search: Use `in` operator in Python, `Arrays.binarySearch()` in Java"
def get_max_min_code(msg): return "Max/Min: `max(list)`, `min(list)` in Python"
def get_conditional_examples(msg): return "Conditions: `if condition:` in Python, `if (condition) {}` in Java"
def get_class_examples(msg): return "Classes: `class MyClass:` in Python, `public class MyClass {}` in Java"
def get_file_operations(msg): return "Files: `open('file.txt', 'r')` in Python, `FileReader` in Java"

# Alternative simple function for testing
def test_gemini_connection():
    """Test function to check if Gemini API is working"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Say hello in a programming context")
        return response.text if response else "API connection failed"
    except Exception as e:
        return f"Error: {e}"