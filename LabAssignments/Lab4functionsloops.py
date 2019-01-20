def sumListWhile(aList):
    counter = 0
    result = 0
    while counter < len(aList):
        result = result + aList[counter]
        counter = counter + 1
    return result
def multiplyListFor(aList):
    result = 1
    for i in aList:
        result = result * i
    return result
def factorialWhileLoop(n):
    if n == 0:
        return 1
    counter = 1
    result = 1
    while counter <= (n):
        result = result * counter
        counter = counter + 1
    return result
def multiplywhile(x,y):
    counter = 0
    result = 0
    while counter < y:
        result = result + x
        counter = counter + 1
    return result
a = [1,2,3]
print(sumListWhile(a))
print(multiplyListFor(a))
print(factorialWhileLoop(3))
print(multiplywhile(2,3))