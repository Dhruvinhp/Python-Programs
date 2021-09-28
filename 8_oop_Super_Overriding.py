class A:
    classvar1 = "class variable of A"
    def __init__(self):
        self.var1 = "inside the class A constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "Special"

class B(A):
    classvar1 = "class variable of B"
    def __init__(self):
        super().__init__()#handle the overriding 
        self.var1 = "Inside the class B constructor"
        self.classvar2 = "Instance variable in class B"
        print(super().classvar1) 
        #with the help of super you can access variable of class A 
        #without printing instance variable of same name in class A

a = A()
b = B()
print("After overriding: ",b.classvar2)
print("Special instance by super: ",b.special) 
#Now it can access the class A's special variable even after the Method overriding, by super()

#class variable : which is written in class 
#instance variable: which is written in class's constructor or method or function