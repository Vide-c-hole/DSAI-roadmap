"""
NumPy Basics Exercises
Run with: python 01_basics_exercises.py

Complete each function and run to test.
"""
import numpy as np

# ============================================
# EXERCISE 1: Array Creation
# ============================================

def create_arrays():
    """
    Create the following arrays:
    1. arr1: A 1D array of numbers 0 to 9
    2. arr2: A 3x3 matrix of all zeros
    3. arr3: A 3x3 identity matrix
    4. arr4: A 2x5 matrix of random numbers between 0 and 1

    Return as tuple: (arr1, arr2, arr3, arr4)
    """
    # YOUR CODE HERE
    arr1 = None
    arr2 = None
    arr3 = None
    arr4 = None
    return (arr1, arr2, arr3, arr4)


def test_create_arrays():
    arr1, arr2, arr3, arr4 = create_arrays()
    assert arr1.shape == (10,) and arr1[0] == 0 and arr1[9] == 9
    assert arr2.shape == (3, 3) and np.all(arr2 == 0)
    assert arr3.shape == (3, 3) and arr3[0, 0] == 1 and arr3[1, 0] == 0
    assert arr4.shape == (2, 5) and arr4.min() >= 0 and arr4.max() <= 1
    print("Exercise 1: PASSED")


# ============================================
# EXERCISE 2: Indexing and Slicing
# ============================================

def array_operations():
    """
    Given: arr = np.arange(1, 26).reshape(5, 5)

    Return a tuple of:
    1. The element at row 2, column 3 (0-indexed)
    2. The entire 3rd row
    3. The entire 2nd column
    4. A 2x2 subarray from rows 1-2, columns 2-3
    """
    arr = np.arange(1, 26).reshape(5, 5)

    # YOUR CODE HERE
    element = None
    third_row = None
    second_col = None
    subarray = None

    return (element, third_row, second_col, subarray)


def test_array_operations():
    element, third_row, second_col, subarray = array_operations()
    assert element == 14  # row 2, col 3
    assert np.array_equal(third_row, np.array([11, 12, 13, 14, 15]))
    assert np.array_equal(second_col, np.array([2, 7, 12, 17, 22]))
    assert subarray.shape == (2, 2)
    print("Exercise 2: PASSED")


# ============================================
# EXERCISE 3: Aggregations
# ============================================

def calculate_stats(arr):
    """
    Given a 2D array, return a dictionary with:
    - 'total_sum': sum of all elements
    - 'mean': mean of all elements
    - 'std': standard deviation
    - 'row_sums': sum of each row (1D array)
    - 'col_means': mean of each column (1D array)
    - 'max_value': maximum value
    - 'min_value': minimum value
    """
    # YOUR CODE HERE
    return {
        'total_sum': None,
        'mean': None,
        'std': None,
        'row_sums': None,
        'col_means': None,
        'max_value': None,
        'min_value': None
    }


def test_calculate_stats():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    stats = calculate_stats(arr)
    assert stats['total_sum'] == 21
    assert stats['mean'] == 3.5
    assert np.array_equal(stats['row_sums'], np.array([6, 15]))
    assert np.array_equal(stats['col_means'], np.array([2.5, 3.5, 4.5]))
    print("Exercise 3: PASSED")


# ============================================
# EXERCISE 4: Boolean Masking
# ============================================

def filter_array(arr, threshold):
    """
    Given an array and threshold:
    1. Create a boolean mask for values > threshold
    2. Return only the values that pass the filter

    Example:
        filter_array(np.array([1, 5, 3, 8, 2]), 3) -> array([5, 8])
    """
    # YOUR CODE HERE
    pass


def test_filter_array():
    arr = np.array([1, 5, 3, 8, 2])
    result = filter_array(arr, 3)
    assert np.array_equal(result, np.array([5, 8]))
    print("Exercise 4: PASSED")


# ============================================
# EXERCISE 5: Broadcasting
# ============================================

def normalize_rows(arr):
    """
    Normalize each row to have mean 0 and std 1.
    (Subtract row mean, divide by row std)

    Handle the case where std is 0 (return 0s for that row).
    """
    # YOUR CODE HERE
    pass


def test_normalize_rows():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    result = normalize_rows(arr)
    # Each row should have mean ≈ 0 and std ≈ 1
    assert np.allclose(result.mean(axis=1), [0, 0])
    assert np.allclose(result.std(axis=1), [1, 1])
    print("Exercise 5: PASSED")


# ============================================
# EXERCISE 6: Reshaping
# ============================================

def reshape_exercises():
    """
    Given: arr = np.arange(24)

    Return a tuple of:
    1. Reshape to 4x6
    2. Reshape to 2x3x4
    3. Flatten back to 1D
    4. Transpose the 4x6 version (should be 6x4)
    """
    arr = np.arange(24)

    # YOUR CODE HERE
    shape_4x6 = None
    shape_2x3x4 = None
    flattened = None
    transposed = None

    return (shape_4x6, shape_2x3x4, flattened, transposed)


def test_reshape():
    shape_4x6, shape_2x3x4, flattened, transposed = reshape_exercises()
    assert shape_4x6.shape == (4, 6)
    assert shape_2x3x4.shape == (2, 3, 4)
    assert flattened.shape == (24,)
    assert transposed.shape == (6, 4)
    print("Exercise 6: PASSED")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("Running NumPy Basics Tests...\n")

    tests = [
        ("Exercise 1", test_create_arrays),
        ("Exercise 2", test_array_operations),
        ("Exercise 3", test_calculate_stats),
        ("Exercise 4", test_filter_array),
        ("Exercise 5", test_normalize_rows),
        ("Exercise 6", test_reshape),
    ]

    for name, test_func in tests:
        try:
            test_func()
        except Exception as e:
            print(f"{name}: FAILED - {e}")

    print("\nDone! Fix the failing tests and run again.")
