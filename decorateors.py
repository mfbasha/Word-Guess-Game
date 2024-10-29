def args_must_be_int(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return func(*args, **kwargs)
        else:
            raise TypeError("All arguments must be integers")
    return wrapper

@args_must_be_int
def add(a, b):
    return a + b

print(add(1, 2))
