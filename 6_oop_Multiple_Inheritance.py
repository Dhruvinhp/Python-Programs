class Employee:
    var = 8  # according to arrangement in class programmer, it will first check in class Employee

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary}, and role is {self.role}"


class Player:
    var = 9  # then it will check in class player


class Programmer(Employee, Player):  # multiple inheritance
    var = 10  # first check in itself
    language = "Python"

    def printlanguage(self):
        print(self.language)


Dhruvin = Programmer("Dhruvin", "45000", "Programmer")
print(Dhruvin.printdetails())
# fetch var value accoring to Multiple inheritance class Programmer
print(Dhruvin.var)
