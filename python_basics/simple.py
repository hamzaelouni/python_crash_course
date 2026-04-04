def simple_decorator(func):
    """
    The nested wrapper() function adds new actions before and after calling the passed function.

    The parameters *args and **kwargs are referred to as variable-length arguments.
    They allow functions to accept any number of positional and keyword arguments, respectively.
    This allows decorators to be flexible and able to handle functions with varying parameters.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}...")
        results = func(*args, **kwargs)
        print(f"Additional functionality")
        return results
    return wrapper

@simple_decorator
def example_function():
    print("Function executed.")

example_function()