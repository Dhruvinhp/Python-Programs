def getDate():
    import datetime
    return datetime.datetime.now()

def take(n):
    if n==1:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            value = input("Type here\n")
            with open("logs/DhruvinExLog.txt", "a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("logs/DhruvinFoodLog.txt", "a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Syccessfully written")
        else:
            print("Invalid input")
    elif n==2:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            value = input("Type here\n")
            with open("logs/VrundaExLog.txt", "a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("logs/VrundaFoodLog.txt","a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Successfully written")
        else:
            print("Invalid input")
    elif n==3:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            value = input("Type here\n")
            with open("logs/VaibhaviExLog.txt", "a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type here\n")
            with open("logs/VaibhaviFoodLog.txt","a") as f:
                f.write(str(getDate())+" : "+value+"\n")
            print("Successfully written")
        else:
            print("Invalid input")
    else:
        print("Invalid input: Enter 1 for Dhruvin, 2 for Vrunda, 3 for Vaibhavi")
    
def retrieve(n):
    if n==1:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            with open("logs/DhruvinExLog.txt") as f:
                for i in f:
                    print(i, end="")
        elif c==2:
            with open("logs/DhruvinFoodLog.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("Invalid input")
    elif n==2:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            with open("logs/VrundaExLog.txt") as f:
                for i in f:
                    print(i, end="")
        elif c==2:
            with open("logs/VrundaFoodLog.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("Invalid input")
    elif n==3:
        c = int(input("Enter 1 for Excersise and 2 for Food: "))
        if c==1:
            with open("logs/VaibhaviExLog.txt") as f:
                for i in f:
                    print(i, end="")
        elif c==2:
            with open("logs/VaibhaviFoodLog.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("Invalid input")
    else:
        print("Invalid input: Enter 1 for Dhruvin, 2 for Vrunda, 3 for Vaibhavi")

print("\n---------Health Management System---------\n")
a = int(input("Press 1 for Log the value and 2 for retrieve the value: "))
if a==1:
    b = int(input("Press 1 for Dhruvin, 2 for Vrunda, 3 for Vaibhavi: "))
    take(b)
elif a==2:
    b = int(input("Press 1 for Dhruvin, 2 for Vrunda, 3 for Vaibhavi: "))
    retrieve(b)
else:
    print("Invalid input, Press 1 for Log the value and 2 for retrieve the value")
