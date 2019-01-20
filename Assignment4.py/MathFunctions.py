def aRecursive(n):
    if n == 1:
        return 3
    return 2*aRecursive(n-1)+5

def aWhileLoop(n):
    if n == 1:
        return 3
    total = 3
    counter = 1
    while counter < n:
        total *= 2
        total += 5
        counter = counter + 1
    return total

def aForLoop(n):
    total = 3
    for i in range(1,n):
        total*=2
        total+=5
    return total



def hRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    return hRecursive(n-1) + 2*hRecursive(n-2)

def hForLoop(n):
    if n == 0:
        return 0
    if n == 1:
        return 3 
    itterations = [0,3,3]
    for i in range (2,n+1):
        itterations[2] = itterations[1] + 2*itterations[0]
        itterations[0] = itterations[1]
        itterations[1] = itterations[2]
    return itterations[2]

def hWhileLoop(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    itterations = [0,3,3]
    counter = 2
    while counter < n+1:
        itterations[2] = itterations[1] + 2*itterations[0]
        itterations[0] = itterations[1]
        itterations[1] = itterations[2]
        counter += 1
    return itterations[2]



def eRecursive(n):
    if n == 0:
        return 1
    return 2*eRecursive(n-1)+2

def eWhileLoop(n):
    if n == 0:
        return 1
    total = 1
    counter = 0
    while counter < n:
        total *= 2
        total += 2
        counter = counter + 1
    return total

def eForLoop(n):
    total = 1
    for i in range(0,n):
        total*=2
        total+=2
    return total



print(aRecursive(10))
print(aWhileLoop(10))
print(aForLoop(10))
print(hRecursive(10))
print(hWhileLoop(10))
print(hForLoop(10))
print(eRecursive(10))
print(eWhileLoop(10))
print(eForLoop(10))
