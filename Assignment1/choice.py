color = input("What is your favorite color? ")
if color == "red":
    print("you like a primary color.")

if color == "red" or color == "yellow":
    print("You like warm colors.")

if color == "blue":
    print("The color of the ocean")
elif color == "green":
    print("part of Elif.")
else:
    print("Fushia is also nice.")

if not (color == "red" or color == "yellow"):
    print("You do not like warm colors.")

if (color == "red" and color == "blue"):
    print("That is impossible!")

x, y = 10, 11

if (x < y):
    print("You've made it.")

if (x > y):
    print("You've made it.")
else:
    print("You're a bit short")

if (2*x <= y + (y - 2)):
    print("Something is fishy with " + str(x) + " and " + str(y))