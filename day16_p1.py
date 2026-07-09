import time
from functools import wraps 
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time= time.perf_counter()
        print(f"function  {func.__name__} took {end_time-start_time:.10f} seconds")
        return result
    return wrapper

@timer
def add(a,b):
    return a+b
print(add(1,1333))