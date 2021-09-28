from colorama import Fore, Back, Style
import time

for i in range(15):
    for j in range(70):
        if i <= 4:
            print("\033[33m"+"*", end="")
        elif i <= 9:
            if j >= 30 and j <= 40:
                if(i == 9 or i == 5) and (j == 30 or j == 31 or j == 40 or j == 39):
                    print(Fore.WHITE + "*", end="")
                else:
                    print(Fore.BLUE + "*", end="")
            else:
                print(Fore.WHITE+"*", end="")
        elif i <= 14:
            print(Fore.GREEN+"*", end="")
    time.sleep(0.1)
    print()
