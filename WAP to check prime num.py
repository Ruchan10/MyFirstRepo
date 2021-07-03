k=int(input('Enter a number: '))
for i in range(2,k):
    if k%i==0:
        print(f'{k} is not a prime number')
        break
    print(f'{k} is a prime number')