print("\n_______________________________MAP__________________________________")
lst = ['23','5','35','9','12']

for i in range(len(lst)):
    lst[i] = int(lst[i])
#OR
lst = list(map(int,lst))
print(lst[0]+lst[1])
#________________________________________
def sq(n):
    return n*n

num=[2,5,9,4,55,12,36,7,10]
print(list(map(sq,num)))
#OR
print(list(map(lambda x:x*x, num))) 
#map traverses the list, calls the function for each element, and returns the results.

#_________________________________________
def square(n):
    return n*n

def cube(n):
    return n*n*n

func=[square, cube]
for i in range(5):
    print(list(map(lambda x:x(i), func)))

print("\n_______________________FILTER_________________________________")
lst=[2,3,8,5,1,3,66,12,45,8,32,9,10,60,55,70,236,45,12]
def gtr5(num):
    return num<40
        
gtrt5 =list(filter(gtr5, lst)) #filter given condition in function
print("Greater than 40: ",gtrt5)
lst.sort()
print("After sorting As:",lst)

print("\n_________________________REDUCE________________________________")
from functools import reduce

lst= [1,2,3,4]

num = 0
for i in lst:
    num = num + i
print(num)
#or
num1 = reduce(lambda x,y: x+y, lst) #reduce time and work
print(num1)
