def mul(k):
    if k<=1:
        return a
    else:
        return a+mul(k-1)
a= int(input('Enter a number to multiply: '))
for i in range(1,11):
    print(f'{a} * {i} = {mul(i)}')