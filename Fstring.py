import math
me = "Dhruvin "
c ="morning"

a = "Hey this is %s"%me
print(a,"\n")#bad format

a1 = "This is {}{}" #or a1="This is {1}{0}" #this will print opposite value of me and c
b = a1.format(me, c)
print(b,"\n")#bad format

f = f"{c}, this is {me}" 
f1 = f"{c}, this is {me},{25*6},{math.cos(90)}"
#fstring 
#we can use module or function in this line e.g. f"{c}, this is {me},{25*6},{math.cos(90)}" 
print(f,"\n",f1)



