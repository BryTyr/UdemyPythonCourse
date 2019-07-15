
def convert_Celsius_fahrenheit(temp):
	return temp*(9/5)+32

print("Passed 23 celsius returned {}".format(convert_Celsius_fahrenheit(23)))
print("Passed 100 celsius returned {}".format(convert_Celsius_fahrenheit(100)))
print("Passed 0 celsius returned {}".format(convert_Celsius_fahrenheit(0)))

temperatures = [10, -20, 100]

for temperature in temperatures:
	print(convert_Celsius_fahrenheit(temperature))
