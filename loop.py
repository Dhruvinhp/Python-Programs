print('For loop:')
total=0
range=[10,20,30]
for price in range:
    total+=price
print(total)

course='Dhruvin Prajapati'
print(course[0:5])

i=1
while i<=5:
    print('*' * i)
    i += 1

name=input('BirthYear:')
date=2020-int(name)
print('your age is',date)

print("----Star----")
"""
row = input("Enter Rows: ")
updown = bool(input("Enter type, eg. 1 or 0"))

if updown == True:
    for i in range(1, row+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
elif updown == False:
    for i in range(row, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
else:
    print("Enter")"""
    