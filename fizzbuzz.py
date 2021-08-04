k=int(input('Enter a number:'))
def fb(k):
    if k%3==0 and k%5==0:
        return "FizzBuzz"
    elif k%3==0:
        return "Fizz"
    elif k%5==0:
        return "Buzz"
    else:
        return k
print(fb(k))
