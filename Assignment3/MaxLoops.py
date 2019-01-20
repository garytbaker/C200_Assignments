#worked with Jarad Stemper  id = jaastem
def MaxFor(aList):
    if aList == []:
        return []
    max = aList[0]
    for i in aList:
        if i > max:
            max = i
    return max

def MaxWhile(aList):
    if aList == []:
        return []
    else: 
        max = aList[0]
        counter = 0
        while counter < len(aList):
            if aList[counter] > max:
                max = aList[counter]
            counter += 1
        return max

def max(x,y):
    if x>y:
        return x
    else:
        return y

def MaxRec(aList):
    if aList == []:
        return []
    if len(aList) == 1:
        return aList[0]
    else:
        return max(aList[0], MaxRec(aList[1:]))

x_wing = [1,2,3,4,5,6,7,8,9,99,47,149,1]
y_wing = []
z_wing = [12,3,2]

print(MaxFor(x_wing))
print(MaxWhile(x_wing))
print(MaxRec(x_wing))
print(MaxFor(y_wing))
print(MaxWhile(y_wing))
print(MaxRec(y_wing))
print(MaxFor(z_wing))
print(MaxWhile(z_wing))
print(MaxRec(z_wing))
