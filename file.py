file1=open('sigma.txt','r')
print(file1.readlines())


file2=open('matin.txt','w')
file2.write("Beknur!")
file2.close()

print(file2.__hash__)