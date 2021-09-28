class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def emp(self):
        return f"name is {self.name}, salary is {self.salary}"


class Programmer(Employee):
    # "inherite class, now this class can access all the attribute of class employee"

    # def __init__(self, aname, asalary):
    #     self.name = aname
    #     self.salary = asalary

    # def prog(self):
    #     return f"name is {self.name}, salary is {self.salary}"
    pass


rohan = Programmer("Rohan", "30000")
karan = Employee("Karan", "25000")
print(rohan.emp())
print(karan.emp())
