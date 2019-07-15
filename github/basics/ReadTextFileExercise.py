
myfile = open("/media/sf_SharedFolderFedora/fruits (1).txt")
content=myfile.read()
fruitArray=content.splitlines()
for item in fruitArray:
	print(len(item))
