num=[2,5,6,4,8,5,4,2,6,5,4,6,3,5,2,5,6,6,8]
unique=[]
for num2 in num:
    if num2 not in unique:
        unique.append(num2)
print('After deleted duplicate values from the list we get')
print(unique)