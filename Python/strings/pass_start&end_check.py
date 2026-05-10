password=input('pass:')

while True:
    aty=input('aty:')

    if password.endswith(aty):
        print("your password ends with aty")
        break
    elif password.startswith(aty):
        print("your password starts with aty")
        break




