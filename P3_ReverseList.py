#Foods and Calories
#Reverse List by Different 3 methods

from typing import List


ListA = []
n = int(input("Enter range of List Values: "))
print("Use Actual value e.g 01, 02, 03 - n")
for i in range(0,n):
    ele = input("Enter List Values: ")
    ListA.append(ele)
print("\nOriginal list: ",ListA)

ListA.sort()
print("Sorted list: ",ListA)

ListA.reverse()
print("\nby Inbuilt Method:        ",ListA)
r1 = ListA[:] #Create a copy of ListA

ListA[::-1]
print("by list[::-1]:            ",ListA)
r2 = ListA[:] #Create a copy of ListA

for i in range(0, n):
    ListA[i], ListA[-i] = ListA[-i], ListA[i]
print("by Third swapping method: ", ListA)
r3 = ListA[:] #Create a copy of ListA
 
if r1 == r2 and r2 == r3: 
    print("\nALL THREE METHODS GIVE SAME RESULT")
