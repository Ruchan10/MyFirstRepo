k=int(input('Enter a number between 1 and 7: '))
dict={1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
if k>0 and k<8:
    print(dict[k])
else :
    print('Please, enter a number between 1 and 7')