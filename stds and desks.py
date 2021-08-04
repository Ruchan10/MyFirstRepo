ca=int(input('Enter total stds of class a: '))
cb=int(input('Enter total stds of class b: '))
cc=int(input('Enter total stds of class c: '))
def classa(ca):
    if ca%3==0:
        da=ca/3
        print(f'No. of desks required in class a is {da}')
    elif ca%3==1:
        da=(ca+2)/3
        print(f'No. of desks required in class a is {da}')
    else:
        da=(ca+1)/3
        print(f'No. of desks required in class a is {da}')
classa(ca)
def classb(cb):
    if cb%3==0:
        db=cb/3
        print(f'No. of desks required in class b is {db}')
    elif cb%3==1:
        db=(cb+2)/3
        print(f'No. of desks required in class b is {db}')
    else:
        db=(cb+1)/3
        print(f'No. of desks required in class a is {db}')
classb(cb)
def classc(cc):
    if cc%3==0:
        dc=cc/3
        print(f'No. of desks required in class c is {dc}')
    elif cc%3==1:
        dc=(cc+2)/3
        print(f'No. of desks required in class c is {dc}')
    else:
        dc=(cc+1)/3
        print(f'No. of desks required in class c is {dc}')
classc(cc)