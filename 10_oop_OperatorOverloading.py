"""
dunder Method ( special method )
Operator overloading 
"mapping operator to function in python":
https://docs.python.org/3/library/operator.html#:~:text=Mapping%20Operators%20to%20Functions%20%C2%B6%20%20%20,truediv%20%28a%2C%20b%29%20%2031%20more%20rows%20
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # -------------------------------------
    # special method or dunder method, handle Operator overloading

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __pow__(self, other):
        return self.salary ** other.salary

    # -------------------------------------
    def __repr__(self):
        return f"{self.name}, {self.salary}"

    def __str__(self):
        return f"str {self.name}, {self.salary}"


emp1 = Employee("Dhruvin", 25)
emp2 = Employee("Rohan", 5)
print(emp1 + emp2)  # handle operator overloading by dunder method
print(emp1 / emp2)
print(emp1 ** emp2)

print(repr(emp1))
# __repr__ format, you should write repr for print __repr__ format otherwise it'll print __str__ format
print(emp1)
# without or with str it'll print __str__ format
# if there is no str then and then it'll print __repr__ format
