k=int(input('Enter no. of seconds to convert: '))
r=k//3600
a=k%3600
n=a//60
c=a%60
print(f'{k} is {r}hr {n}min {c}secs')