
for i in range(0,4):
    print(i)

for move in range(0,4):
    print(move)

for i in range(1,5):
    print(i)

for kitty in range(0,1+2):
    print(kitty)

for Supercalifragilisticexpialidocious in range(0,1):
    print(Supercalifragilisticexpialidocious)

for i in range(11,0,-2):
    print(" "*int((12-i)/2) + "*"*i, end="")
    print()

sum = 0
for i in range(11):
    sqr = i**2
    sum += sqr
print(sum)

donor = [10, 12, .75, 5.23, 25.35, 14.53, 15.99, 8.00, 8.01, .25]

dontotal = 0
if donor == []:
    print("no donations")
else:
    for i in donor:
        dontotal += i
if dontotal > 100:
    print("The total is over $100! The professor will double it!")

