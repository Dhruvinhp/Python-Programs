n = int(input("Enter numeric number: "))
boo = bool(input("Enter True or False: "))
if boo == True:
    for t in n:
        s = ("*")*t
        print(s)
else:
    for f in n:
        s=("*")*f
        print(s)
