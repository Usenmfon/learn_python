def myDecorator(func):
    def wrapper():
        print("This is where the function starts")
        func()
        print("This is where the function ends")
    return wrapper

@myDecorator
def sayHello():
    print("Hello Usenmfon")

sayHello()


def acceptParams(func):
    def sumDecor(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return sumDecor

@acceptParams
def sum(a, b):
    return a + b

print(sum(3,4))

