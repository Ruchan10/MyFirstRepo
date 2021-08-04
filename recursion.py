def cd(n):
    if n<=0:
        print('Blast!')
    else:
        print(n)
        cd(n-1)
cd(3)