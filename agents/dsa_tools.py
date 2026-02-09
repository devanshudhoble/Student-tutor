"""
DSA Tools for Google ADK Agent.
Custom tools that the DSA Tutor agent can use.
"""


def explain_dsa_concept(concept: str) -> str:
    """
    Explain a Data Structure or Algorithm concept in simple terms.
    
    Args:
        concept: The DSA concept to explain (e.g., "binary search", "hash table", "dynamic programming")
    
    Returns:
        A detailed explanation of the concept suitable for beginners.
    """
    concepts = {
        "array": "An array is a collection of elements stored at contiguous memory locations. Think of it like a row of lockers - each locker has a number (index) and can store one item.",
        "linked list": "A linked list is a chain of nodes where each node contains data and a pointer to the next node. Like a treasure hunt where each clue points to the next location.",
        "stack": "A stack follows LIFO (Last In, First Out). Like a stack of plates - you add and remove from the top only.",
        "queue": "A queue follows FIFO (First In, First Out). Like a line at a store - first person in line is served first.",
        "hash table": "A hash table uses a hash function to map keys to values for fast lookups. Like a library catalog that tells you exactly where to find a book.",
        "binary search": "Binary search works on sorted data by repeatedly dividing the search space in half. Like guessing a number between 1-100 by always guessing the middle.",
        "recursion": "Recursion is when a function calls itself to solve smaller subproblems. Like Russian nesting dolls - each doll contains a smaller version of itself.",
        "dynamic programming": "DP solves complex problems by breaking them into overlapping subproblems and storing results to avoid redundant work. Like filling a table of solutions bottom-up.",
        "binary tree": "A binary tree is a hierarchical structure where each node has at most two children (left and right). Like a family tree but each person has at most 2 children.",
        "graph": "A graph consists of vertices (nodes) connected by edges. Like a social network where people are vertices and friendships are edges.",
        "two pointers": "Two pointers technique uses two indices to traverse data, often from opposite ends. Like two people walking towards each other on a path.",
        "sliding window": "Sliding window maintains a window of elements that slides through the array. Like looking through a moving frame at a painting.",
    }
    
    concept_lower = concept.lower().strip()
    
    for key, explanation in concepts.items():
        if key in concept_lower or concept_lower in key:
            return f"## {concept.title()}\n\n{explanation}\n\n### Key Points:\n- Commonly used in coding interviews\n- Practice with LeetCode problems to master it"
    
    return f"## {concept.title()}\n\nThis is an important DSA concept. Let me explain it step by step in the main response."


def analyze_complexity(code_description: str) -> str:
    """
    Analyze the time and space complexity of an algorithm.
    
    Args:
        code_description: Description of the algorithm or approach to analyze
    
    Returns:
        Time and space complexity analysis in simple terms.
    """
    return f"""## Complexity Analysis for: {code_description}

### Common Complexity Classes:
| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop through array |
| O(n log n) | Linearithmic | Merge sort, Quick sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |

### Tips:
- Count the number of nested loops
- Recursive calls often multiply complexity
- Hash tables provide O(1) average lookup
- Sorting typically costs O(n log n)
"""


def get_leetcode_hints(problem_name: str, hint_level: int = 1) -> str:
    """
    Provide progressive hints for a LeetCode problem without giving away the solution.
    
    Args:
        problem_name: Name of the LeetCode problem (e.g., "Two Sum", "Valid Parentheses")
        hint_level: Level of hint detail (1=basic, 2=medium, 3=detailed)
    
    Returns:
        A hint appropriate for the specified level.
    """
    hints = {
        "two sum": [
            "Hint 1: Think about what information you need to find a pair that sums to target.",
            "Hint 2: For each number, you need to find if its complement (target - num) exists. How can you check this quickly?",
            "Hint 3: Use a hash map to store numbers you've seen and their indices. For each new number, check if (target - num) is in the map."
        ],
        "valid parentheses": [
            "Hint 1: What data structure follows Last-In-First-Out (LIFO) order?",
            "Hint 2: Push opening brackets onto a stack. When you see a closing bracket, check if it matches the top of the stack.",
            "Hint 3: Use a dictionary to map closing brackets to opening brackets. Pop from stack and verify match."
        ],
        "reverse linked list": [
            "Hint 1: You need to change the direction of all the arrows (next pointers).",
            "Hint 2: Keep track of three nodes: previous, current, and next.",
            "Hint 3: Save next, point current to previous, then move forward. prev=curr, curr=next."
        ],
        "binary search": [
            "Hint 1: Always work with a sorted array. Compare middle element with target.",
            "Hint 2: If target < mid, search left half. If target > mid, search right half.",
            "Hint 3: Use left and right pointers. mid = (left + right) // 2. Update boundaries based on comparison."
        ],
    }
    
    problem_lower = problem_name.lower().strip()
    hint_level = max(1, min(3, hint_level))  # Clamp between 1-3
    
    for key, problem_hints in hints.items():
        if key in problem_lower or problem_lower in key:
            return problem_hints[hint_level - 1]
    
    generic_hints = [
        "Start by understanding the problem: What are the inputs? What output is expected?",
        "Think about the brute force solution first, then optimize. What data structure could help?",
        "Consider edge cases: empty input, single element, duplicates. Write out the algorithm step by step."
    ]
    
    return generic_hints[hint_level - 1]
