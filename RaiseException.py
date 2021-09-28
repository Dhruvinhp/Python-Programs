n = input("NAME: ")

if n.isnumeric():
    raise Exception("name should be in characters ")
print("HI", n)
#------------------------------------------------------------------------
b = input("NAME: ")
try:
    print(a)
except Exception as e:
    if b == "Dhruvin":
        raise ValueError("Dhruvin is blocked by organization")
    print("Exception handled!")
# ------------------------------------------------------------------------
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if a==0 or b==0:
    raise ZeroDivisionError("Values can't be zero.")
else:
    c = a/b
    print(c)
#------------------------------------------------------------------------ 
list = ["Never", "Nope", "yes", "yeah"] 
ind = [0, 1, "2", 3] 
for i in range(len(ind)): 
    try: 
        print(list[ind[i]]) 
    except TypeError: 
        print(f"Type Error: String value on index {ind[i]}")