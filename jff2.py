def fact(n):
    if n==5:
        return 5
    else:
        return n*fact(n+1)
print(fact(1))