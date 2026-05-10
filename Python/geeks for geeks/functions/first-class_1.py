# def add(x, y): 
#     return x + y
# def sub(x, y): 
#     return x - y

# # choice = input()

# # if choice == "add":
# #     operation = add
# # elif choice=="sub":
# #     operation = sub
# # else:
# #     print("please enter right value ")

# # print(operation(5, 3))

# ops = {"add": add,"sub": sub}

# print(ops["add"](5, 3))

def run(func):
    func()

def hello():
    print("Hello")

def bye():
    print("Bye")

run(hello)   # Hello
run(bye)     # Bye