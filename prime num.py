pn=int(input('Enter a number: '))
def fun(pn):
    for i in range(2,pn):
        if pn%i==0:
            print(f'{pn} is not a prime number')
            break
    else:
        print(f'{pn} is a prime number')
fun(pn)