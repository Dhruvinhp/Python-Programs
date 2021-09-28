list=["one, two, three, four, five"] #list
numb = [1,22,3,58,4,16,14,55,23,2,15,36,6,8]
numb.sort() #sorted numb
numb.pop() #remove last int
numb.remove(3)
numb[2]=69 #inserted in the given index
print("list: String", list)
print("List: int", numb )

tup=(1,2,5,3,5,4,5) #immutable, cannot be changed or edited
print("tupple:",tup)

a= 23
b= 48
a,b=b,a #exchanging value
print(a , b)