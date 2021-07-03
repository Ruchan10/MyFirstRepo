ca=int(input("Enter number of students in class a:"))
cb=int(input("Enter No. of students in class b:"))
cc=int(input("Enter No. of students in class c:"))
if ca>-1 and cb >-1 and cc>-1:
    if ca%2==1:
        ca=ca+1
        cad=ca/2
        print(f'No. of desk required in class a is {cad}' )
    else:
        cad=ca/2
        print(f'No. of desk required in class a is {cad}')
    if cb%2==1:
        cb=cb+1
        cbd=cb/2
        print(f'No. of desk required in class b is {cbd}')
    else:
        cbd=cb/2
        print(f'No. of desk required in class b is {cbd}')
    if cc%2==1:
        cc=cc+1
        ccd=cc/2
        print(f'No. of desk required in class c is {ccd}')
    else:
        ccd=cc/2
        print(f'No. of desk required in class c is {ccd}')
    print(f'The total number of desk required is {cad+cbd+ccd}')
else :
    print('Invalid number entered')