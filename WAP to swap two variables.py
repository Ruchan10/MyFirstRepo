k = input('Enter a string : ')
r = input('Enter another string : ')
def fun(k,r):
    s=k
    k=r
    r=s
    return k,r

fun(k,r)
print(f'The value of k after swap is {k}')
print(f'The value of r after the swap is {r}')