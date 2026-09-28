def generate_ai_explanation(code, language):
    """Generate AI explanation for code"""
    explanations = {
        'python': {
            'print': 'This code uses print() to display output to the console.',
            'def': 'This code defines a function using the def keyword.',
            'for': 'This code uses a for loop to iterate through elements.',
            'if': 'This code uses conditional statements to make decisions.',
            'return': 'This code returns a value from the function.',
        },
        'java': {
            'System.out.println': 'This code prints output to the console using System.out.println().',
            'public static void main': 'This is the main method where program execution begins.',
            'public class': 'This defines a public class in Java.',
            'for': 'This code uses a for loop for iteration.',
            'if': 'This code uses if-else statements for conditional logic.',
        },
        'javascript': {
            'console.log': 'This code outputs to the browser console using console.log().',
            'function': 'This code defines a JavaScript function.',
            'for': 'This code uses a for loop to iterate.',
            'if': 'This code uses conditional statements.',
            'return': 'This code returns a value from the function.',
        }
    }
    
    explanation_parts = []
    lang_explanations = explanations.get(language, {})
    
    for keyword, explanation in lang_explanations.items():
        if keyword in code:
            explanation_parts.append(explanation)
    
    if not explanation_parts:
        return f"This {language} code implements a solution using basic programming concepts."
    
    return " ".join(explanation_parts[:3])  # Limit to 3 explanations