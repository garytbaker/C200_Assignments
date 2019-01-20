def maxThree (x,y,z):
    if x > y:
        if x > z:
            return x 
    elif y > z:
        return y 
    else:
        return z 


def minThree (x,y,z):
    if x < y:
        if x < z:
            return x 
    elif y < z:
        return y 
    else:
        return z 

def MaxTwoSum (x,y,z):
    if (x + y) > (y + z):
        if (x + y) > (x + z):
            return (x + y)
    elif (y + z) > (x + z):
        return (y + z)
    else: 
        return (x + z)

def MinTwoSum (x,y,z):
    if (x + y) < (y + z):
        if (x + y) < (x + z):
            return (x + y)
    elif (y + z) < (x + z):
        return (y + z)
    else: 
        return (x + z)

def maxList(alist):
    currentmax = -9999999999999999999999999999999999999999999999999999999999999999999999
    for item in alist:
        if item > currentmax:
            currentmax = item 
    return currentmax

def minList(alist):
    currentmin = 9999999999999999999999999999999999999999999999999999999999999999999999
    for item in alist:
        if item < currentmin:
            currentmin = item 
    return currentmin


alist = [1,2,3,4,5]
print(maxThree(1,2,3))
print(minThree(1,2,3))
print(MaxTwoSum(1,2,3))
print(MinTwoSum(1,2,3))
print(maxList(alist))
print(minList(alist))