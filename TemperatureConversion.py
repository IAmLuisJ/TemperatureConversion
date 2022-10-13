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
    print(f'{x} Farhenheit = {}')
#print results and round to 2 dec places

for y in range(0, 100, 20):
    newTemp = convertconvert_c_to_f(y)
    print("{y} Celsius = " + str(newTemp + "Farhenheit.")