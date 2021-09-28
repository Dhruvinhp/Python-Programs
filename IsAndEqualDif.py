a = [5,6,8,6,52,4]
print(a)
b = a
print(b==a) # == means two variables have same value 
print(b is a) # is means two variable have same reference,
              # means in memory they stored in same location
c = a[:] #create a copy of a
print(c == b) # have a same value
print(c is b) # but have a different reference location
a[0] = 45
print(a)
print(b==a)
print(b is a)
print(c == b)
print(c is b) 
