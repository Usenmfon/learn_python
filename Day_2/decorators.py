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
