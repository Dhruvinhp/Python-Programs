# object introspection means to know about object

import inspect


class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"Name:{self.name}, salary is {self.salary}$"


dhruvin = Emp("Dhruvin", "250")
print("\n", dhruvin.details())
print("\nType:", type("Dhruvin"))
print("\nDirectory: ", dir(dhruvin.details()))
print("\nStored in", id(dhruvin.details()))
print("\nCheck and get members of dhruvin attribute: ",
      inspect.getmembers(dhruvin))
