dict={'anupa':90,'ruchan':85,'kanchan':80,'bikal':75, 'python':70, 'ruby':65, 'c':60,'c++':55, 'java':50,'javascript':45,'swift':40,'php':35, 'html':30}
a=input('Enter a name of student: ')
if a in dict:
    print(f'The mark obtained by {a} is {dict[a]}')
else:
    print('No student found in the database')
print('Just some extra stuff')
print(dict['kanchan'])

