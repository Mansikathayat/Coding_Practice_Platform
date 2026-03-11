from problems.models import Category, Problem, TestCase

# Create more categories
dp_cat, _ = Category.objects.get_or_create(name="Dynamic Programming", defaults={"description": "DP problems"})
tree_cat, _ = Category.objects.get_or_create(name="Trees", defaults={"description": "Tree problems"})
graph_cat, _ = Category.objects.get_or_create(name="Graphs", defaults={"description": "Graph problems"})
sorting_cat, _ = Category.objects.get_or_create(name="Sorting", defaults={"description": "Sorting problems"})
linked_list_cat, _ = Category.objects.get_or_create(name="Linked Lists", defaults={"description": "Linked list problems"})

arrays_cat = Category.objects.get(name="Arrays")
strings_cat = Category.objects.get(name="Strings")
math_cat = Category.objects.get(name="Math")

problems_data = [
    # Easy Problems
    {"title": "Remove Duplicates from Sorted Array", "slug": "remove-duplicates", "difficulty": "easy", "category": arrays_cat, "description": "Remove duplicates from sorted array in-place."},
    {"title": "Best Time to Buy and Sell Stock", "slug": "best-time-buy-sell-stock", "difficulty": "easy", "category": arrays_cat, "description": "Find maximum profit from stock prices."},
    {"title": "Valid Parentheses", "slug": "valid-parentheses", "difficulty": "easy", "category": strings_cat, "description": "Check if parentheses are valid."},
    {"title": "Merge Two Sorted Lists", "slug": "merge-two-sorted-lists", "difficulty": "easy", "category": linked_list_cat, "description": "Merge two sorted linked lists."},
    {"title": "Maximum Subarray", "slug": "maximum-subarray", "difficulty": "easy", "category": arrays_cat, "description": "Find contiguous subarray with largest sum."},
    {"title": "Climbing Stairs", "slug": "climbing-stairs", "difficulty": "easy", "category": dp_cat, "description": "Count ways to climb n stairs."},
    {"title": "Binary Tree Inorder Traversal", "slug": "binary-tree-inorder", "difficulty": "easy", "category": tree_cat, "description": "Inorder traversal of binary tree."},
    {"title": "Symmetric Tree", "slug": "symmetric-tree", "difficulty": "easy", "category": tree_cat, "description": "Check if tree is symmetric."},
    {"title": "Maximum Depth of Binary Tree", "slug": "max-depth-binary-tree", "difficulty": "easy", "category": tree_cat, "description": "Find maximum depth of binary tree."},
    {"title": "Same Tree", "slug": "same-tree", "difficulty": "easy", "category": tree_cat, "description": "Check if two trees are same."},
    {"title": "Reverse Linked List", "slug": "reverse-linked-list", "difficulty": "easy", "category": linked_list_cat, "description": "Reverse a linked list."},
    {"title": "Palindrome Linked List", "slug": "palindrome-linked-list", "difficulty": "easy", "category": linked_list_cat, "description": "Check if linked list is palindrome."},
    {"title": "Contains Duplicate", "slug": "contains-duplicate", "difficulty": "easy", "category": arrays_cat, "description": "Check if array contains duplicates."},
    {"title": "Missing Number", "slug": "missing-number", "difficulty": "easy", "category": arrays_cat, "description": "Find missing number in array."},
    {"title": "Move Zeroes", "slug": "move-zeroes", "difficulty": "easy", "category": arrays_cat, "description": "Move all zeros to end."},
    {"title": "Fizz Buzz", "slug": "fizz-buzz", "difficulty": "easy", "category": math_cat, "description": "Classic FizzBuzz problem."},
    {"title": "Single Number", "slug": "single-number", "difficulty": "easy", "category": arrays_cat, "description": "Find number that appears once."},
    {"title": "Happy Number", "slug": "happy-number", "difficulty": "easy", "category": math_cat, "description": "Determine if number is happy."},
    {"title": "Count Primes", "slug": "count-primes", "difficulty": "easy", "category": math_cat, "description": "Count prime numbers less than n."},
    {"title": "Isomorphic Strings", "slug": "isomorphic-strings", "difficulty": "easy", "category": strings_cat, "description": "Check if strings are isomorphic."},
    
    # Medium Problems
    {"title": "Add Two Numbers", "slug": "add-two-numbers", "difficulty": "medium", "category": linked_list_cat, "description": "Add numbers represented as linked lists."},
    {"title": "Longest Substring Without Repeating Characters", "slug": "longest-substring", "difficulty": "medium", "category": strings_cat, "description": "Find longest substring without repeating characters."},
    {"title": "Container With Most Water", "slug": "container-most-water", "difficulty": "medium", "category": arrays_cat, "description": "Find container that holds most water."},
    {"title": "3Sum Closest", "slug": "3sum-closest", "difficulty": "medium", "category": arrays_cat, "description": "Find three numbers closest to target."},
    {"title": "Remove Nth Node From End", "slug": "remove-nth-node", "difficulty": "medium", "category": linked_list_cat, "description": "Remove nth node from end of list."},
    {"title": "Generate Parentheses", "slug": "generate-parentheses", "difficulty": "medium", "category": strings_cat, "description": "Generate all valid parentheses combinations."},
    {"title": "Swap Nodes in Pairs", "slug": "swap-nodes-pairs", "difficulty": "medium", "category": linked_list_cat, "description": "Swap every two adjacent nodes."},
    {"title": "Next Permutation", "slug": "next-permutation", "difficulty": "medium", "category": arrays_cat, "description": "Find next lexicographical permutation."},
    {"title": "Search in Rotated Sorted Array", "slug": "search-rotated-array", "difficulty": "medium", "category": arrays_cat, "description": "Search in rotated sorted array."},
    {"title": "Find First and Last Position", "slug": "find-first-last-position", "difficulty": "medium", "category": arrays_cat, "description": "Find first and last position of element."},
    {"title": "Combination Sum", "slug": "combination-sum", "difficulty": "medium", "category": arrays_cat, "description": "Find combinations that sum to target."},
    {"title": "Permutations", "slug": "permutations", "difficulty": "medium", "category": arrays_cat, "description": "Generate all permutations."},
    {"title": "Rotate Image", "slug": "rotate-image", "difficulty": "medium", "category": arrays_cat, "description": "Rotate 2D matrix by 90 degrees."},
    {"title": "Group Anagrams", "slug": "group-anagrams", "difficulty": "medium", "category": strings_cat, "description": "Group strings that are anagrams."},
    {"title": "Pow(x, n)", "slug": "pow-x-n", "difficulty": "medium", "category": math_cat, "description": "Implement power function."},
    {"title": "Spiral Matrix", "slug": "spiral-matrix", "difficulty": "medium", "category": arrays_cat, "description": "Return matrix elements in spiral order."},
    {"title": "Jump Game", "slug": "jump-game", "difficulty": "medium", "category": arrays_cat, "description": "Determine if you can reach last index."},
    {"title": "Merge Intervals", "slug": "merge-intervals", "difficulty": "medium", "category": arrays_cat, "description": "Merge overlapping intervals."},
    {"title": "Unique Paths", "slug": "unique-paths", "difficulty": "medium", "category": dp_cat, "description": "Count unique paths in grid."},
    {"title": "Minimum Path Sum", "slug": "minimum-path-sum", "difficulty": "medium", "category": dp_cat, "description": "Find minimum path sum in grid."},
    
    # Hard Problems
    {"title": "Regular Expression Matching", "slug": "regex-matching", "difficulty": "hard", "category": strings_cat, "description": "Implement regular expression matching."},
    {"title": "Merge k Sorted Lists", "slug": "merge-k-sorted-lists", "difficulty": "hard", "category": linked_list_cat, "description": "Merge k sorted linked lists."},
    {"title": "Reverse Nodes in k-Group", "slug": "reverse-nodes-k-group", "difficulty": "hard", "category": linked_list_cat, "description": "Reverse nodes in groups of k."},
    {"title": "Substring with Concatenation", "slug": "substring-concatenation", "difficulty": "hard", "category": strings_cat, "description": "Find substring with concatenation of words."},
    {"title": "Longest Valid Parentheses", "slug": "longest-valid-parentheses", "difficulty": "hard", "category": strings_cat, "description": "Find longest valid parentheses substring."},
    {"title": "Sudoku Solver", "slug": "sudoku-solver", "difficulty": "hard", "category": arrays_cat, "description": "Solve Sudoku puzzle."},
    {"title": "First Missing Positive", "slug": "first-missing-positive", "difficulty": "hard", "category": arrays_cat, "description": "Find first missing positive integer."},
    {"title": "Trapping Rain Water", "slug": "trapping-rain-water", "difficulty": "hard", "category": arrays_cat, "description": "Calculate trapped rainwater."},
    {"title": "Wildcard Matching", "slug": "wildcard-matching", "difficulty": "hard", "category": strings_cat, "description": "Implement wildcard pattern matching."},
    {"title": "Jump Game II", "slug": "jump-game-ii", "difficulty": "hard", "category": arrays_cat, "description": "Find minimum jumps to reach end."},
    {"title": "N-Queens", "slug": "n-queens", "difficulty": "hard", "category": arrays_cat, "description": "Solve N-Queens puzzle."},
    {"title": "Edit Distance", "slug": "edit-distance", "difficulty": "hard", "category": dp_cat, "description": "Find minimum edit distance."},
    {"title": "Largest Rectangle in Histogram", "slug": "largest-rectangle", "difficulty": "hard", "category": arrays_cat, "description": "Find largest rectangle in histogram."},
    {"title": "Maximal Rectangle", "slug": "maximal-rectangle", "difficulty": "hard", "category": arrays_cat, "description": "Find maximal rectangle in matrix."},
    {"title": "Binary Tree Maximum Path Sum", "slug": "binary-tree-max-path", "difficulty": "hard", "category": tree_cat, "description": "Find maximum path sum in binary tree."},
]

for prob_data in problems_data:
    problem, created = Problem.objects.get_or_create(
        slug=prob_data["slug"],
        defaults={
            "title": prob_data["title"],
            "description": prob_data["description"],
            "difficulty": prob_data["difficulty"],
            "category": prob_data["category"]
        }
    )
    if created:
        # Add sample test case
        TestCase.objects.create(
            problem=problem,
            input_data="Sample input",
            expected_output="Sample output",
            is_sample=True
        )

print(f"Added {len(problems_data)} problems! Total problems: {Problem.objects.count()}")