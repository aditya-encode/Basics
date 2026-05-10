# *args example
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for  val in kwargs.values():
        print(val)

fun(a=1, b=2, c=3)