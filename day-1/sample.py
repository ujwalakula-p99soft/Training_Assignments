
try:
    a = "abc"
    b = "def"
    print(a - b)
except Exception as e:
    print("The exception is",e)
finally:
    print("finished")
