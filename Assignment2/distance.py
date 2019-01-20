dis_spd = str(input("Do you want to know your speed or your distance? (speed or distance): "))
dis_spd = dis_spd.lower()

while True:
    if dis_spd == "distance":
        break
    elif dis_spd == "speed":
        break
    else:
       dis_spd = str(input("I'm sorry, did you mean speed or distance? "))

def myDistance(spd,time):
    #minutes * (1hr/60minutes) = hr
    time *= (1/60)
    #(mi/hr) * hr = mi
    distance = spd * time
    return distance

def mySpeed(distance,time):
    #speed = mi/hr 
    spd = (distance/time)
    return spd

if dis_spd == "distance":
    spd = float(input("What is your speed in miles per hour?  "))
    time = float(input("How long were you driving in minutes?  "))
    print("You went " + str(myDistance(spd,time)) + " miles if you went in a straight line at a constant speed.")
elif dis_spd == "speed":
    distance = float(input("What was your distance traveled in miles? "))
    time = float(input("What was your time traveled in hours? "))
    print("You were going " +str(mySpeed(distance,time)) + " miles per hour.")