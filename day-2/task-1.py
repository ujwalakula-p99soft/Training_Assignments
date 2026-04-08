import os

with open("sample.txt","w") as f:
    f.write("Hello,everyone")

with open("sample.txt") as f:
    print(f"The content present in file is {f.read()}")

with open("sample.txt","a") as f:
    f.write(",How are you")

newfile = open("test3.txt","x")

with open("test.txt","w") as f:
    f.write("This the file to test the application.")

with open("test.txt") as f:
    print(f"The content present in test file is , {f.read()}")

try:
    if os.path.exists("test2.txt"):
        os.remove("test2.txt")
    else:
        print("The file does not exist")
except Exception as e:
    print("failed to delete the file",e)