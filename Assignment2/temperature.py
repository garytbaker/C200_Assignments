
TempC = input("What is the temperature outsid ein celcius? ")

def conversion(TempC):
    TempF = ((TempC * (9/5)) + 32)
    return TempF

def conv(temperature,kind):
    if kind == 0:
        Temperature = conversion(temperature)
    elif kind == 1:
        Temperature = (temperature - 32) * (9/5)
    return Temperature

if float(conversion(TempC)) < 45:
    print("It is " + str(conversion(TempC)) + " degrees outside. Wear a coat!")
elif float(conversion(TempC)) > 90:
    print("It is " + str(conversion(TempC)) + " degrees outside. Stay hydrated!")
else:
    print("It is " + str(conversion(TempC)) + " degrees outside.")

