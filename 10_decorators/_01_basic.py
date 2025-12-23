# def my_decorator(func):
#     def wrapper():
#         print('Before functions runs')
#         func()
#         print('After functions runs')
#     return wrapper

# @my_decorator
# def greet():
#     print(f'Hello from decorators from Python')

# greet()
# print(greet.__name__)
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print('Before functions runs')
        func()
        print('After functions runs')
    return wrapper

@my_decorator
def greet():
    print(f'Hello from decorators from Python')

greet()
print(greet.__name__)