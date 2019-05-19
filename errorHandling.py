# Error handling in Python

try:
    a = 10
    b = 20
    print("10/0 = " + str(a/b))
except Exception:
    print("Cannot divide by zero.")
else:
    print("Hi, I am an else block")
