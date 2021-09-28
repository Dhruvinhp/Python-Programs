from random import randint

t=['Rock','Paper','Scissor']
computer=t[randint(0,2)]
player = False
print("You gonna play with computer")

while player == False:
    player=input("""Rock, Paper, Scissor?
    >""")
    if player==computer:
        print(" Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose!", computer, "covers", player)
        else:
            print("You Win!", player,"Smashes",computer)
    elif player=="Paper":
        if computer=="Scissor":
            print("You Lose!", computer, "cut the", player)
        else:
            print("You Win!", player,"covers", computer)
    elif player=="Scissor":
        if computer=="Rock":
            print("You Lose!",computer,"smashes",player)
        else:
            print("You Win!", player, "cut", computer)
    else:
        print("Not a Valid play. Check your spelling! they are case-sensitive options")

    player = False
    computer=t[randint(0,2)]