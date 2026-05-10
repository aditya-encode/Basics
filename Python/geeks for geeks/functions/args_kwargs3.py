def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
greet(a=1, b=2, a=3)