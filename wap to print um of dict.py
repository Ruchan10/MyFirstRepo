d={1:2,2:3,3:4}
a=0
for i in d:
    b= d.get(i)
    a=a+b
print(a)