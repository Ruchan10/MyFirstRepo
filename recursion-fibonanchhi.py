def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
a=int(input('How many numbers do u want: '))
for i in range(a):
    print(fibo(i))