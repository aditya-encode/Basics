# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# # Storing functions in a dictionary
# d = {
#     "add": add,
#     "subtract": subtract
# }

# # Calling functions from the dictionary
# # print(d["add"](5, 3))       
# print(d["add"](5,3))
# print(d["subtract"](5,3)) 

def greet(func): # higher-order function 
    return func("Hello")


def uppercase(text): # function to be passed
    return text.upper()


print(greet(uppercase))