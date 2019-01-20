LifeData = [["Bison", 20, 10, 2],["Wolf", 10, 15, 4],["Praire Dog", 15, 15, 1],["Mountain Lion", 10, 8, 1]]

def EstPopSize(taggedFirst, captureAgain, taggedSecond):
    popsizeest = (taggedFirst*captureAgain)/taggedSecond
    return popsizeest

for d in LifeData:
    print(d[0] + " estimated population size = " + str(EstPopSize(d[1],d[2],d[3])))