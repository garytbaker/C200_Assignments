#worked with Jarad Stemper id = jaastem
import math
def savings_after_interest(d,r,t):
    deposit = d
    rate = r
    time = t
    final_total = (deposit) * (math.exp((rate * time)))
    return final_total

def Salmonella_Growth_Rate(n,m,t):
    initial_bacteria = n
    growth_rate = m
    time = t
    BacteriaCount = (initial_bacteria) * (math.exp((growth_rate * time)))
    return BacteriaCount

def rate(age):
    if age >= 6:
        if age > 10:
            if age > 15:
                if age > 17:
                    return 4
                else:
                    return 3
            else:
                return 2.5
        else: 
            return 2
            
def DWtime(w, r):
    width = w
    rate = r
    DW_TIME = ((width / rate) - 6)
    return DW_TIME 
print(savings_after_interest(1000,.02,10))
print(Salmonella_Growth_Rate(500,100,4))
print(rate(7))
print(rate(12))
print(rate(17))
print(rate(21))
print(DWtime(30,rate(7)))