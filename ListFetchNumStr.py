items=[int, float, "dhruvin", 23, "dh", 55,"ru", 2,"vi", 1, "n", 8, 7, 56, 4, 98, 1,12, 90]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)


while int(input("enter number: "))< 100: #both do same thing
    continue

while(True):
    inp = int(input("enter a number: ")) #both
    if inp>100:
        print("congo")
        break
    else:
        continue
    
