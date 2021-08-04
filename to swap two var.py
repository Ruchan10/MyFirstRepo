fv=input('Enter a variable: ')
sv=input('Enter another variable: ')
print(f'''First variable = {fv}
Second Variable = {sv}
''')
k=fv
fv=sv
sv=k
print(f'''After Swap
First Variable = {fv}
Second Variable = {sv}''')