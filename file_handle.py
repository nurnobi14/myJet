print("file write(create) :")
 
f_create = open("new.txt",'a')
print(f_create)
f_create.write("something \n")
f_create.write(" kicu")
v= open("new.txt",'r')

for data in v :
	print(data)