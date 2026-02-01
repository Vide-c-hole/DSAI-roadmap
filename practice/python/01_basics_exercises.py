"""
Python Basics Exercises
Run with: python 01_basics_exercises.py

Instructions:
1. Complete each function
2. Run the file to test your solutions
3. All tests should pass (print "PASSED")
"""

# ============================================
# EXERCISE 1: List Comprehensions
# ============================================

def square_even_numbers(numbers):
    """
    Given a list of numbers, return a new list with
    only the even numbers, squared.

    Example:
        square_even_numbers([1, 2, 3, 4, 5]) -> [4, 16]
    """
    # YOUR CODE HERE
    pass


def test_square_even():
    assert square_even_numbers([1, 2, 3, 4, 5]) == [4, 16]
    assert square_even_numbers([2, 4, 6]) == [4, 16, 36]
    assert square_even_numbers([1, 3, 5]) == []
    print("Exercise 1: PASSED")


# ============================================
# EXERCISE 2: Dictionary Operations
# ============================================

def word_frequency(text):
    """
    Count the frequency of each word in the text.
    Convert to lowercase, ignore punctuation.

    Example:
        word_frequency("Hello hello world") -> {"hello": 2, "world": 1}
    """
    # YOUR CODE HERE
    pass


def test_word_frequency():
    result = word_frequency("Hello hello world")
    assert result == {"hello": 2, "world": 1}
    result2 = word_frequency("The cat and the dog")
    assert result2["the"] == 2
    print("Exercise 2: PASSED")


# ============================================
# EXERCISE 3: Functions with *args
# ============================================

def calculate_average(*args):
    """
    Calculate the average of any number of arguments.
    Return 0 if no arguments provided.

    Example:
        calculate_average(10, 20, 30) -> 20.0
        calculate_average() -> 0
    """
    # YOUR CODE HERE
    pass


def test_average():
    assert calculate_average(10, 20, 30) == 20.0
    assert calculate_average(5) == 5.0
    assert calculate_average() == 0
    print("Exercise 3: PASSED")


# ============================================
# EXERCISE 4: Dictionary with **kwargs
# ============================================

def create_profile(name, **kwargs):
    """
    Create a user profile dictionary.
    Always include 'name', add any other kwargs provided.

    Example:
        create_profile("Alice", age=25, city="NYC")
        -> {"name": "Alice", "age": 25, "city": "NYC"}
    """
    # YOUR CODE HERE
    pass


def test_profile():
    p1 = create_profile("Alice", age=25, city="NYC")
    assert p1 == {"name": "Alice", "age": 25, "city": "NYC"}
    p2 = create_profile("Bob")
    assert p2 == {"name": "Bob"}
    print("Exercise 4: PASSED")


# ============================================
# EXERCISE 5: File Processing
# ============================================

def count_lines_with_word(filepath, word):
    """
    Count how many lines in the file contain the given word.
    Case-insensitive search.

    Returns 0 if file doesn't exist.
    """
    # YOUR CODE HERE
    pass


# ============================================
# EXERCISE 6: Error Handling
# ============================================

def safe_divide(a, b):
    """
    Divide a by b, but handle errors gracefully.
    - Return the result if successful
    - Return None if division by zero
    - Return None if inputs aren't numbers

    Example:
        safe_divide(10, 2) -> 5.0
        safe_divide(10, 0) -> None
        safe_divide("a", 2) -> None
    """
    # YOUR CODE HERE
    pass


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    assert safe_divide("a", 2) is None
    print("Exercise 6: PASSED")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("Running Python Basics Tests...\n")

    try:
        test_square_even()
    except Exception as e:
        print(f"Exercise 1: FAILED - {e}")

    try:
        test_word_frequency()
    except Exception as e:
        print(f"Exercise 2: FAILED - {e}")

    try:
        test_average()
    except Exception as e:
        print(f"Exercise 3: FAILED - {e}")

    try:
        test_profile()
    except Exception as e:
        print(f"Exercise 4: FAILED - {e}")

    try:
        test_safe_divide()
    except Exception as e:
        print(f"Exercise 6: FAILED - {e}")

    print("\nDone! Fix the failing tests and run again.")
