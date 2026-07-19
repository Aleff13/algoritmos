#static class with static methods for timing

class Timer:
    """"
    A static class that provides methods for timing the execution of functions.

    Example usage:
    result, elapsed_time = Timer.time_function(some_function, arg1, arg2)

    """
    @staticmethod
    def time_function(func, *args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    
#Decorator for timing functions
def time_function_decorator(func):
    """
    A decorator that measures the execution time of a function.

    Example usage:
    @time_function_decorator
    def some_function(arg1, arg2):
        # Function implementation

    """
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result
    return wrapper

#Decorator for timing functions create a global variable to store the time taken for the function to execute,
#keyed by input size so scaling behavior (e.g. O(log n) vs O(n)) can be plotted across repeated calls
elapsed_times = {}
def time_function_decorator_global(func):
    """
    A decorator that measures the execution time of a function and appends
    (input_size, elapsed_time) to a global variable, so a single function can
    be called many times with different input sizes and later plotted as a
    scaling curve.

    Input size is inferred from the first argument that has a length
    (e.g. the list being searched); falls back to a call counter otherwise.

    Example usage:
    @time_function_decorator_global
    def some_function(arg1, arg2):
        # Function implementation

    """
    import time

    def wrapper(*args, **kwargs):
        size = None
        for arg in args:
            try:
                size = len(arg)
                break
            except TypeError:
                continue
        if size is None:
            size = len(elapsed_times.get(func.__name__, []))

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        elapsed_times.setdefault(func.__name__, []).append((size, elapsed_time))
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds (n={size}).")
        return result
    return wrapper

#function to plot the time taken for the function to execute using matplotlib
def plot_elapsed_times(log_scale=True):
    """
    Plot the execution times of functions stored in the global variable 'elapsed_times'
    as a line per function, execution time vs. input size, so growth rates
    (e.g. binary search vs. linear search) are visually comparable.

    Parameters:
    log_scale (bool): Use a log-log scale, useful when input sizes/times span
    several orders of magnitude.

    Example usage:
    plot_elapsed_times()

    """
    import matplotlib.pyplot as plt

    if not elapsed_times:
        print("No elapsed times to plot.")
        return

    fig, ax = plt.subplots()

    for func_name, points in elapsed_times.items():
        sorted_points = sorted(points, key=lambda p: p[0])
        sizes = [p[0] for p in sorted_points]
        times = [p[1] for p in sorted_points]
        ax.plot(sizes, times, marker='o', label=func_name)

    if log_scale:
        ax.set_xscale('log')
        ax.set_yscale('log')

    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Function Execution Time vs. Input Size')
    ax.legend()
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()