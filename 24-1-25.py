"""def greet_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Good bye")
    return wrapper

@greet_decorator
def greet():
    print("My Name is chinmay")

greet()







def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(3, 4)

  





def decorator_one(func):
    def wrapper():
        print("1")
        func()
        print("2")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("3")
        func()
        print("4")
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("5")

result = greet()
print(result)



import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)  # original function calling
        end_time = time.time()
        print(f"start time {start_time}, and end time {end_time}")
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
    return wrapper

@timer_decorator
def fun():
    time.sleep(2)
    print("Function Finished")

fun()"""




class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return ComplexNumber(new_real, new_img)

    def __str__(self):
        return f"{self.real}i+{self.img}j"

c1 = ComplexNumber(real=5, img=3)
c2 = ComplexNumber(real=3, img=2)

c3 = c1 + c2
print(c3)  




