
game = [["x", "o", "x"],["_", "x", "o"],["_", "_", "_"]]
game[2][0] = "o"

for row in game:
    print(row)

x = [25,2,142,0,54,-1]

def min(x):
    currentmin = x[0]
    for i in x:
        if i < currentmin:
            currentmin = i
    return currentmin

print(min(x))