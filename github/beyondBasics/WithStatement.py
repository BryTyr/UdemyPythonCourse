
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f


def temp_writer(temperatures):
    with open("temperatureFile.txt","w") as myFile:
        for t in temperatures:
            temp=c_to_f(t)
            if type(temp)==float:
                myFile.write(str(temp)+"\n")


temperatures = [10, -20, -289, 100]
temp_writer(temperatures)
