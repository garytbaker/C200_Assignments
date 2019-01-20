import numpy as np


def sum(x):
    total = 0
    for i in x:
        total += i
    return total
def multiplysum(x,y):
    total = 0
    for i in range(len(x)):
        total += (x[i] * y[i])
    return total
def expsum(x):
    total = 0
    for i in x:
        total += i**2
    return total
def n(x):
    n = len(x)
    return n
def r(x,y):
    top = n(x)*multiplysum(x,y)-(sum(x)*sum(y))
    bottomL = (n(x)*expsum(x)-(sum(x)**2))
    bottomr = (n(x)*expsum(y)-(sum(y)**2))
    return (top/((bottomL*bottomr)**.5))

fm = open("studyhours.txt", "r")
a = np.array(range(12),int).reshape((6,2))
for i in range(6):
    d = fm.readline().split(",")
    a[i][1] = int(d[1])
    a[i][0] = int(d[0])
print("The correlation is: {0}.".format(r(a[:,[0]], a[:,[1]])))
