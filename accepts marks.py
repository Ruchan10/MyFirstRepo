def function():
    a=float(input("Enter marks of Account:"))
    m=float(input("Enter marks of Maths:"))
    e=float(input("Enter marks of English:"))
    c=float(input("Enter marks of Computer:"))
    eco=float(input("Enter marks of Economics:"))

    b=a+m+e+c+eco
    if 0<=b<501:
        print(f'Your total marks is {b}')

    d=(b/5)
    if 0<=d<101:
         print(f'Your percentage is {d} %')

    if 101>d>=70:
        print('Distinction')
    elif 70>d>=60:
        print('First Division')
    elif 60>d>=40:
        print('Pass')
    elif 40>d:
        print('Fail')
    else:
        print('Invalid Input')
lst={2,5,6,5,3,5}
for i in lst:
    function()
