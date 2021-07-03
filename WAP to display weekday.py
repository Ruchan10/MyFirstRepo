k = int(input('ENTER A NUMBER between 1 and 7: '))
dict=("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
if 0<k<8:
    print(dict[k-1])
else :
    print('Invalid')