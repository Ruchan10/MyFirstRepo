dict={'anupa':90,'ruchan':85,'kanchan':80,'bikal':75, 'python':70, 'ruby':65, 'c':60,'c++':55, 'java':50,'javascript':45,'swift':40,'php':35, 'html':30}
a=input('Enter a name of student: ')
if a in dict:
    print(f'The mark obtained by {a} is {dict[a]}')
else:
    print('No student found in the database')
print('Just some extra stuff')

dict['python']='71'     # Replaces value stored in the given key(python)
print(dict['kanchan']) # Prints the value in the given key(kanchan) and returns KeyError if there is no key in dict
print(dict.get('python')) # Prints the value in the given key(kanchan) and returns None if there is no key in dict
print(dict.pop('ruby')) # Removes the value of the given key from dict and returns it
print(dict)
print(dict.popitem()) # Removes random key:value pair from dict and returns it
print(dict)
del dict['swift'] # Deletes the value stored in given key(swift)
print(dict)
dict.clear() # Makes the dict empty
print(dict)
del dict # Deletes the entire dict
