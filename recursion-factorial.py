def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
k=int(input('Enter a number to find factorial: '))
print(fact(k))