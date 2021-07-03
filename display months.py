n=int(input('Enter a number between 1 and 12: '))
mon=("Janaury", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
if 13>n>0 :
    k=n-1
    print(mon[k])
else :
    print('Error number entered')
