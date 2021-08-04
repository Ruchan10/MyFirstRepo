list0=[0,1,10,2,3,4,5,6,7,8,9]
k=0
r=0
for i in list0:
    if i%2==0:
        k=k+1
    else:
        r=r+1
print(f'''
odds={r}
even={k}''')
