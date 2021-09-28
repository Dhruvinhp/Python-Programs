from random import randint

t=['snake', 'water', 'gun']
computer=t[randint(0,2)]
player = False
count = 0
win = 0
loose = 0
print("\n----------SNAKE WATER GUN----------\n")
print("You gonna play with computer")

while count <10:
    player=input("""snake, water, gun?
    >""") 
    if player==computer:
        print(" Tie!")
    elif player=="snake":
        if computer=="gun":
            print("You Lose!", computer, "kills", player)
            loose+=1
        else:
            print("You Win!", player,"drinks",computer)
            win+=1

    elif player=="water":
        if computer=="snake":
            print("You Lose!", computer, "drinks", player)
            loose+=1
        else:
            print("You Win!", player,"destroy", computer)
            win+=1
    elif player=="gun":
        if computer=="water":
            print("You Lose!",computer,"destroy",player)
            loose+=1
        else:
            print("You Win!", player, "kills", computer)
            win+=1
    else:
        print("Not a Valid play. Check your spelling! they are case-sensitive options")

    player = False
    count +=1
    computer=t[randint(0,2)]

print("\n----------GAME OVER----------\n")
print("WIN: ", win)
print("LOOSE: ", loose)
if win>loose:
    print("YOU WIN")
elif loose>win:
    print("YOU LOOSE")
else:
    print("TIE")