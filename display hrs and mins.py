k = int(input('How many minutes has passed since midnight : '))
if k>-1:
    hrs = k//60
    mins = k % 60
    print(f"It's {hrs}:{mins} right now")
else:
    print('Invalid number entered')