def constant_time_operation(arr):
    """Returns the first element of the array in constant time O(1)."""
    if not arr:
        return None
    return arr[0]

# simple operation where no matter the size of input, time taken remains same is constant respresented as O(1)

def linear_time_operation(arr):
    """Returns the sum of all elements in the array in linear time O(n)."""
    total = 0
    for num in arr:
        total += num
    return total

# operation where time taken grows linearly with input size generaly due to code looping through the input
# is linear represented as O(n)

def quadratic_time_operation(matrix):
    """Returns the sum of all elements in a 2D matrix in quadratic time O(n^2)."""
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

# operation where time taken grows quadratically with input size is quadratic represented as O(n^2)
# generally due to nested loops iterating over the input


def logarithmic_time_operation(arr, target):
    """Performs binary search to find the target in a sorted array in logarithmic time O(log n)."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# operation where time taken grows logarithmically with input size is logarithmic represented as O(log n)
# generally due to halving the input size with each operation

def linearithmic_time_operation(arr):
    """Sorts the array using merge sort in linearithmic time O(n log n)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = linearithmic_time_operation(arr[:mid])
    right_half = linearithmic_time_operation(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """Merges two sorted arrays."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# operation where time taken grows as n log n with input size is linearithmic represented as O(n log n)
# generally due to divide and conquer algorithms like merge sort
# which divide the input and then merge results back together

def factorial_time_operation(n):
    """Calculates the factorial of n in factorial time O(n!)."""
    if n == 0 or n == 1:
        return 1
    result = 0
    for i in range(n):
        result += factorial_time_operation(n - 1)
    return result

# operation where time taken grows factorially with input size is factorial represented as O(n!)
# generally due to algorithms that generate all permutations of the input

def exponential_time_operation(n):
    """Calculates the nth Fibonacci number in exponential time O(2^n)."""
    if n <= 1:
        return n
    return exponential_time_operation(n - 1) + exponential_time_operation(n - 2)

# operation where time taken grows exponentially with input size is exponential represented as O(2^n)
# generally due to algorithms that solve problems by exploring all possible combinations recursively