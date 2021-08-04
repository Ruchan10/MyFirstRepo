l={0,1,2,3,4,5,6,7,8,9,10}
k=0
r=0
for i in l:
    if i%2==0:
        r=r+1
    else:
        k=k+1
print(f'''
Even = {r}
Odd = {k}''')