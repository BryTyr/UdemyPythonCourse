numbers = [1, 2, 3]
myfile=open("numberFile.txt","a+")
for number in numbers:
	myfile.write(str(number)+"\n")
myfile.close()
