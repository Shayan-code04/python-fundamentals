from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        print(f"Calling function: {func.__name__}")

        print(f"Positional args: {args}")

        print(f"Keyword args: {kwargs}")

        result = func(*args,**kwargs)

        print(f"Returned: {result}")

        return result

    return wrapper



@logger
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("alex", greeting="Yo"))
print(greet("Shayan"))