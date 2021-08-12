file0=open('abc.txt','r+')
a=file0.read()
file0.close()

file1=open('abc0.txt','w')
file1.write(a)
file1.close()