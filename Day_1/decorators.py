def myDecorator(func):
    def wrapper():
        print("Before the function begins...")
        func()
        print("After the function ends...")
    return wrapper

@myDecorator
def sayHello():
    print("Hello, World!")

sayHello()


def mathDecorator(func) -> int:
    def wrapper(*args, **kwargs) -> int:
        print("Before the function...")
        result = func(*args, **kwargs)
        print("After the function...")
        return result
    return wrapper

@mathDecorator
def sum(a: int, b: int) -> int:
    return a + b

print(sum(2, 5))