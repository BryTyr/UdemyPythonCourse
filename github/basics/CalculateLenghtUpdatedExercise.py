def calculate_length(inputString=""):
	if type(inputString)==int:
		return	"integers dont have a length"
	elif type(inputString)==float:
		return  "floatss dont have a length"
	else:
		return	len(str(inputString))

print("Input 1 length: {} ".format(calculate_length("Hello There!")))
print("Input 2 length: {} ".format(calculate_length("hola senor")))
print("Input 3 length: {} ".format(calculate_length()))
print("Input 4 length: {} ".format(calculate_length(22134)))
print("Input 5 length: {} ".format(calculate_length(22134.123445)))


