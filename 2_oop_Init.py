class Student:
    def __init__(self, name, std, sub, role): 
        #__init__ handle the arguments which is given to class
        self.name = name
        self.std = std
        self.sub = sub
        self.role = role

hermione = Student("Hermione Granger", 4,["magic", "postion", "mystry"],"Student") 
#in this line hermione is self in init, and given data is stored in given name like,
#hermione.name = "Hermione Granger"
#without init cannot execute this task^ 
print(hermione.name, hermione.role, hermione.sub)

#this is better way to execute this type of task then oopsSelf.py file
#init is a constructor