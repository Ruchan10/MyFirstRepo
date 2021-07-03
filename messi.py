#WAP to find weekday according to the inserted number

WD=int(input('Enter a number between 1 and 7 : '))
if WD==1 :
    print('It is Sunday')
elif WD==2 :
    print('It is Monday')
elif WD==3 :
    print('It is Tuesday')
elif WD==4 :
    print('It is Wednesday')
elif WD==5 :
    print('It is Thursday')
elif WD==6 :
    print('It is Friday')
elif WD==7 :
    print('It is Saturday')
else :
    print("Given number is invalid")