k=int(input('Enter a number: '))
sum = 0
if k>=0:
    for i in range(0,k+1):
        sum=sum+i
    print(f'The dum from{0} to {k} is {sum}')
elif k<0:
    for i in range(0,k-1,-1):
        sum = sum+i
    print(f'The sum from {0}to {k} is {sum}')

