import time
print("Welcome to Dhruvin's Mountain Adventure game")
print("____________________________________________")
print("You are visiting Mountain Everest, INDIA")
print("You go on an evening hike alone in the Mountains.")
time.sleep(2)
print("You can pick any one item to take with you - ")
print("map (m), flashlight (f), chocolate (c), rope (r) or stick (s): ")
item = input("What do you choose?: ")
time.sleep(2)
print("you hear a humming sound.")
choice1 = input("Do you follow the sound? Enter y or n: ")
time.sleep(2)
if choice1 == 'y':
    print("You keep moving closer to the sound.")
    time.sleep(1)
    print("The sound suddenly stops.")
    time.sleep(1)
    print("You are now LOST!...")
    time.sleep(1)
    print("You try to call on your phone but there is no signal! ")
    time.sleep(1)
    direction = input(
        "Which direction do you go? north, south, east, ot west: ")
    time.sleep(1)
    if direction == 'north':
        print("you reach the abandoned cabin.")
        time.sleep(1)
        if item == "m":
            print("you use the map and find your way home.")
            time.sleep(1)
            print("CONGRATULATIONS! You won the game. ")
        else:
            print("If you had a map, you could find your way from here.")
            time.sleep(1)
            print("---You are still Lost. You Lost the Game.---")
    elif direction == "south":
        print("you reach a river with broken bridge.")
        time.sleep(1)
        if item == "r" or item == "s":
            print("You choose an item that can fix the bridge.")
            time.sleep(1)
            print("You fix the bridge by rope, cross over, and find your way home.")
            time.sleep(1)
            print("CONGRATULATIONS! You won the Game. ")
        else:
            print(
                "If you had a rope or stick, you could fix the bridge and find a way home.")
            time.sleep(1)
            print("---You are still lost. You Lost the game.---")
    elif direction == "west":
        print("You are walking and trip over a fallen log.")
        time.sleep(1)
        print("You have hurt your foot. You sit down and wait for help.")
        time.sleep(1)
        print("THis could be long time, you are still lost.")
        time.sleep(1)
        print("---You lost the Game.---")
    else:
        print("You reach the side of the highway. It is Dark.")
        time.sleep(1)
        if item == 'f':
            print('You use the flashlight to signal.')
            time.sleep(1)
            print("A car stops and gives you a ride home.")
            time.sleep(1)
            print("CONGRATULATIONS! You got out safely. You won the Game.")
        else:
            print("If you had a flashlight, you could signal for help.")
            print("---You are still Lost. you lost the Game.---")
else:
    print("Good Idea, You are not taking risk. ")
    print("You start walking back to the starting point.")
    print("You realize you are LOST! ")
    print("The sound is behind you and is getting loader. You panic! ")
    action = input("DO you start running (r), stop to make a call (c)?: ")
    while action == "c":
        print("The call Does not go through")
        action = input("Do you want to run (r) or try calling again (c)?: ")
    print("You are running fast. The Sound gets really load.")
    print("A woman on an electric scooter comes up behind you. ")
    answer = input(
        "She says, 'Name my favorite computer programming language.'")
    if answer == "python":
        print("She says, 'Yes, Python is my favorite programming language.'")
        print("If you have some chocolate, I can help you.")
        if item == 'c':
            print("Luckily you did choose correctly!")
            print("You give her the chocolate.")
            print("She helps you get home.")
            print("CONGRATULATIONS! You got out safely. You won the Game.")
        else:
            print("You should have chosen that Chocolate!")
            print("She rides away, Leaving you alone and lost.")
            print("---You lost the game.---")
    else:
        print("She did not like your answer.")
        print("Shw rides away, Leaving you Lost!")
        print("---You lost the game---")
