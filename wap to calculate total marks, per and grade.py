a=float(input('Enter marks of account: '))
b=float(input('Enter marks of maths: '))
e=float(input('Enter marks of english: '))
c=float(input('Enter marks of computer: '))
tm=a+b+e+c
print(f'Total marks: {tm}')
per=tm/400 * 100
print(f'Percentage = {per}%')
if per >=70:
    print('Distinction')
elif per >=60:
    print('First Division')
elif per >=40:
    print('Pass')
else:
    print('Fail')
