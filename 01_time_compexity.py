import time

def time_function(func, *args, **kwargs):
    """
    Measures the execution time of a given function.

    Parameters:
    func (callable): The function to be timed.
    *args: Positional arguments to pass to the function.
    **kwargs: Keyword arguments to pass to the function.

    Returns:
    tuple: A tuple containing the result of the function and the time taken in seconds.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    time_taken = end_time - start_time
    return result, time_taken

# Example usage:
if __name__ == "__main__":
    def example_function(n):
        total = 0
        for i in range(n):
            total += i
        return total

    n = 1000000
    result, duration = time_function(example_function, n)
    print(f"Result: {result}, Time taken: {duration:.6f} seconds")