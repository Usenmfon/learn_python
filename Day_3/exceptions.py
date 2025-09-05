try:
    result = 2/ 0
except ZeroDivisionError:
    print("Zero Division Error ")
finally:
    result = 1

print(result)