k=int(input('Enter a number:'))
fact = 1
if k>0:
    for i in range (1,k+1,1):
        fact=fact*i
    print(f'The factorial of {k} is {fact}')
else :
    print("error")

