stds= int(input('Enter no.of students: '))
if stds%3==0:
    des=stds/3
    print(f'The required no. of desks is {des}')
else:
    if (stds+1)%3==0:
        des=(stds+1)/3
        print(f'The required no. of desks is {des}')
    else:
        stds=stds+2
        des=stds/3
        print(f'The required no. of desks is {des}')