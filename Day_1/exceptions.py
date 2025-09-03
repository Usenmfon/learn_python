
# result = 2 / 0
# print(result)

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    result = 1

print(result)

# Raise Exceptions

try:
    raise Exception("This is an error message.")
except Exception as e:
    print(e)