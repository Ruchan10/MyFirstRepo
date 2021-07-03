secs = float(input('Enter seconds: '))
secs=int(secs)
if secs>=0:
    a=secs%3600
    hrs=secs//3600
    b=a%60
    mins=a//60
    print(f"{hrs} Hours {mins} Minutes {b} Seconds")
else:
    print('Invalid number entered')