class Student:
    no_of_leaves = 8
    def __init__(self, name, std, role): 
        self.name = name
        self.std = std
        self.role = role

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves 

    @classmethod
    def from_dash(cls, string): #Alternative Constructor
        # params = string.split("-")
        # return cls(params[0],params[1],params[2]) #by list
        return cls(*string.split("-")) #by*args

    @staticmethod #simple static method which does not use self
    def printxyz(string):
        print("This is " + string)

hermione = Student("Hermione Granger", 4,"Student")
dhruvin = Student.from_dash("Dhruvin-5-GoalKeeper") #in one-line by constructor
Student.change_leaves(10)
Student.printxyz("Dhruvin") #static method call

print(hermione.name, hermione.std, hermione.role)
print(hermione.no_of_leaves)
print(dhruvin.role)