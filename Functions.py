#with no parameter and no return statement

print('For addition')
def add():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    print(f'The sum is {a+b}')
add()

# with no parameter and with return ststement

print('For subtraction')
def sub():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    return a-b
s=sub()
print(f"The subtraction is {s}")

#with parameter and no return statement

print('For division')
def div(c,d):
    print(f'The division is {c/d}')
c=int(input('Enter first number :'))
d=int(input('Enter second number :'))
div(c,d)

# with parameter and return ststement

print('For multiplication')
def mul(r,k):
    return r*k
r=int(input('Enter first number: '))
k=int(input('Enter second number :'))
m=mul(r,k)
print(f'The multiplication is {m}')