def passThroughDoor(string):
    for i in range(0,len(string)):
        if i == (len(string)-1):
            return False
        if string[i] == string[(i+1)]:
            return True
       
print(passThroughDoor("ballon"))
print(passThroughDoor("color"))
print(passThroughDoor("wendall"))
print(passThroughDoor("gary baker"))
print(passThroughDoor("Peanut butter"))