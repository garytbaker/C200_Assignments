
def increase(alist):
    listoflists = []
    currentlist = [alist[0]]
    longestlist = []
    for i in range(1, len(alist)):
        if alist[i-1] <= alist[i]:
            currentlist.append(alist[i])
        else:
            listoflists.append(currentlist)
            currentlist = [alist[i]]
    listoflists.append(currentlist)
    for i in listoflists:
        if len(i) >= len(longestlist):
            longestlist = i
    if len(longestlist) < 2:
        return []
    return longestlist
     

def runOfOnes(alist):
    listofonelength = []
    counter = 0
    for i in alist:
        if i == 1:
            counter += 1
        elif i == 0:
            listofonelength.append(counter)
            counter = 0
    listofonelength.append(counter)
    finalanswer = listofonelength[0]
    for i in listofonelength:
        if i > finalanswer:
            finalanswer = i
    return finalanswer

def stringIntersection(x,y):
  strings = ""
  for i in x:
        for z in y:
            if z == i:
                strings += str(i)
  return strings
                







print(increase([1,2,2,1,5,2,3,4,5,8,3]))
print(increase([7,1,7,1,8,1]))
print(increase([1,1,5,2,2,3,3,1]))
print(increase([5,4,3,2,1]))
print(runOfOnes([0]))
print(runOfOnes([0,1,1,0,1,0,1,1,1,0,1,0,1]))
print(runOfOnes([]))
print(runOfOnes([1]))
print(runOfOnes([1,1,1,1,1,0,1]))
print(stringIntersection("abcd325","5tDEDc3"))
