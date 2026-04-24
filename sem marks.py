try:
    marks=25
    result=25/0
    print(result)
except ZeroDivisionError:
    print("A number cannot be divide by zero")
finally:
    print("code runs successfully")
