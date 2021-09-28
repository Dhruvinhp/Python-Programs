#Divide the Apples

harry = int(input("Enter the numbers of apples harry have: "))
potterMin = int(input("Enter the range of Min: "))
potterMax = int(input("Enter the range of Max: "))

for i in range(potterMin, potterMax + 1):
    if (harry % i)== 0:
        print(f"{i} is divisior of {harry}")
    else:
        print(f"{i} is not divisior of {harry}")