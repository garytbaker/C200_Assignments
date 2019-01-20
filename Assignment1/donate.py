bloodtype = input("What is your blood type? (A+, B+, O+, AB+, A-, B-, O-, AB-)  ")

if bloodtype == "A+":
    print("You can doante blood to people wit A+ and AB+ blood.")
elif bloodtype == "O+":
    print("You can donate blood to people with O+, A+, B+, and AB+ blood.")
elif bloodtype == "B+":
    print("You can donate blood to people with B+ and AB+ blood.")
elif bloodtype == "AB+":
    print("You can donate blood to people with AB+ blood.")
elif bloodtype == "A-":
    print("You can donate blood to people with A+, A-, AB+, and AB- blood.")
elif bloodtype == "O-":
    print("You can donate blood to everyone.")
elif bloodtype == "B-":
    print("You can donate blood to people with B+, B-, AB+, and AB- blood.")
elif bloodtype == "AB-":
    print("You can donate blood to people with AB+ and AB- blood.")
else:
    print("You don't have real blood.")