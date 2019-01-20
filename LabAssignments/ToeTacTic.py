""" Gary Baker, Isaiah Sherfick, Jared Stemper """


class box:
    def __init__(self):
        self.letter = " "
        self.content = "| "+ self.letter + " |"
    def addletter(self,x):
        self.letter = x
        self.content = "| " + self.letter +" |"

topleft=box()
topmid=box()
topright=box()
midleft=box()
midmid=box()
midright=box()
botleft=box()
botmid=box()
botright=box()

top = [topleft,topmid,topright]
mid = [midleft,midmid,midright]
bot=[botleft,botmid,botright]
diag1 = [topleft,midmid,botright]
diag2 = [topright,midmid,botleft]
c1 = [topleft, midleft,botleft]
c2 = [topmid,midmid,botmid]
c3 = [topright,midright,botright]
winruns = [top,mid,bot,diag1,diag2,c1,c2,c3]

plays = {"1":topleft,"2":topmid,"3":topright,"4":midleft,"5":midmid,"6":midright,"7":botleft,"8":botmid,"9":botright}

def draw():
    print(topleft.content + topmid.content + topright.content)
    print("---------------")
    print(midleft.content + midmid.content + midright.content)
    print("---------------")
    print(botleft.content+botmid.content+botright.content)
print("Toe-Tac-Tic")
print("")
print("| 1 | | 2 | | 3 |")
print("----------------")
print("| 4 | | 5 | | 6 |")
print("----------------")
print("| 7 | | 8 | | 9 |")
print("")
print("Input the number corresponding to the square you'd like to play.")
print("")

winner = False
winningletter = ""
tie = False

def checkwin():
    global winruns
    global winner
    global winningletter
    global tie
    for i in range(len(winruns)):
        if winruns[i][0].letter == winruns[i][1].letter and winruns[i][1].letter == winruns[i][2].letter and winruns[i][0].letter != " ":
            winner = True
            winningletter = winruns[i][0].letter
    if topleft.letter != " " and topmid.letter != " " and topright.letter != " " and midleft.letter != " " and midmid.letter != " " and midright.letter!= " " and botleft.letter != " " and botmid != " " and botright!= " ":
        winner = True
        tie = True

what = True
history = []
while winner == False:
    print("")
    draw()
    print("")
    if what:
        print("It\'s x\'s turn!")
        currentplayer="x"
        what = False
    else:
        print("It\'s o\'s turn!")
        currentplayer = "o"
        what = True
    valid = False
    while valid == False:
        play = input("Where do you want to place your letter? ")
        validinputs = []
        for i in range(1,10):
            validinputs += [str(i)]
        if play in validinputs and play not in history:
            history += [play]
            valid = True
        else:
            print("")
            print("Please enter a proper position.")
            print("")
    plays[play].addletter(currentplayer)
    checkwin()
draw()
print("")
if tie == False:
    print(winningletter + " wins!")
else:
    print("Tie!")
