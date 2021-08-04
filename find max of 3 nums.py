r=float(input('Enter a number: '))
k=float(input('Enter another number: '))
s=float(input('Enter another number: '))
if r>k and r>s:
    print(f'{r} is maximum')
elif k>s and k>r:
    print(f'{k} is maximum')
else:
    print(f'{s} is the maximum')