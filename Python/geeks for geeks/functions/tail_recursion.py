def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

print(tail_fact(10000))