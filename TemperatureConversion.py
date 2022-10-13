# Luis Juarez CIS261 WK2 Temperature Conversion

def convert_f_to_c(farTemp):
    #convert f to C
    celTemp = (farTemp - 32) * 5 / 9
    return celTemp

def convert_c_to_f(celTemp):
    farTemp = (celTemp * 9) / 5 + 32
    return farTemp

#for in loop range of temps
for x in range(0, 212, 40):
    cTemp = round(convert_f_to_c(x),2)
    print(str(x) +' Farhenheit = ' + str(cTemp) + " Celsius")
#print results and round to 2 dec places

for y in range(0, 100, 20):
    newTemp = convert_c_to_f(y)
    print(str(y)+" Celsius = " + str(newTemp) + " Fahrenheit")