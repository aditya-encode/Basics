import sys

while True:
    name = input("Enter name: ")

    if name == "exit":
        sys.exit()

    print("Hello", name)