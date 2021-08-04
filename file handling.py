'''list0=['20580416']

file0=open('abc.txt','w')
file0.write('RK')
file0.close()

file0=open('abc.txt','a')
list0.append('ruchan')
file0.close()
print(list0)

file0=open('abc.txt')
print(file0.read())
file0.close()

file0=open('abc.txt','r+')
print(file0.read())
file0.write('rk')
file0.close()

file0=open('abc.txt','w+')
file0.write('rk')
print(file0.read())
file0.close()

file0=open('abc.txt','a+')
list0.append('RK')
print(list0)
print(file0.read())
file0.close()

file0=open('abc4.txt','x')
file0.write('K')
file0.close()

file0=open('abc4.txt','r')
print(file0.read())
file0.close()'''

import pickle
rk=['speaker','pen']
file=open('abc0.txt','ab')
pickle.dump(rk,file)
file.close()

file=open('abc0.txt','rb')
s={'key':'shyam','name':'iamironman','age':'50'}
s0=pickle.load(file)
for key in s0:
    print(key,':',s0[key])
file.close()

