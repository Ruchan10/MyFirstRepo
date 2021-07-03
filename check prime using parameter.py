k=int(input('Enter a number: '))
def prime(k):
    for i in range(2,k):
        if k%i==0:
            print(f'{k} is not a prime number')
            break
    else:
        print(f'{k} is a prime number')
prime(k)