ls = [i for i in range(10) if i%2==0] # [] list comprehension
print(ls)

dic = {i:f"item {i}" for i in range(10)} # {} dictionary comprehension
dic2 = {value:key for key, value in dic.items()} #reverse dictionary
print(dic,"\n",dic2)

set = {i for i in ['d1', 'd2', 'd1', 'd2'] } #{} [] set, only one time print 
print(set)

even = (i for i in range(10) if i%2==0) # () Generator comprehension  
print(even.__next__())
print(even.__next__())
print(even.__next__())
 #or
for i in even:
    print(i)