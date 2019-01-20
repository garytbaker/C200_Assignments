TA = input("What is the temperature in Fahrenheit today?  ")
V = input("So it is " + str(TA) + " degrees out today. What is the windspeed in miles per hour?  ")

TWC = (34.74 + (0.6215 * float(TA)) - (35.75 * (float(V) ** .16)) + ((.4275 * float(TA) * (float(V) ** .16))))
print("The windchill is " + str(TWC) + " degrees Fahrenheit.")