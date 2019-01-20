income = input("How much money did you make last year? $")
income = float(income)

if income <= 0:
   print("Sorry for your loss.")
elif income > 0 and income <= 9075:
    income = income * .1
    print("You owe " + str(income) + " dollars.")
elif income > 9075 and income <= 36900:
    income = 907.50 + ((income - 9075) * .15)
    print("You owe " + str(income) + " dollars.")
elif income > 36900 and income <= 89350:
    income = 5081.25 + ((income - 36900) * .25)
    print("You owe " + str(income) + " dollars.")
elif income > 89350 and income <= 186350:
    income = 18193.75 + ((income - 89350) * .28)
    print("You owe " + str(income) + " dollars.")
elif income > 186350 and income <= 405100:
    income = 45353.75 + ((income - 186350) * .33)
    print("You owe " + str(income) + " dollars.")
elif income > 405100 and income <= 406750:
    income = 117541.25 + ((income - 405100) * .35)
    print("You owe " + str(income) + " dollars.")
elif income > 406750:
    income = 118118.75 + ((income - 406750) * .396)
    print("You owe " + str(income) + " dollars.")
