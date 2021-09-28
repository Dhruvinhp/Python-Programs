class Student:
    no_of_leaves = 8  # class object

    def details(self):
        return f" Name is {self.name}, year is {self.std}, subject is {self.sub}, role is {self.role}"


dhruvin = Student()  # instance assign
harry = Student()
rone = Student()

dhruvin.name = "Dhruvin Prajapati"
harry.name = "Harry potter"
rone.name = "Rone Weasley"

dhruvin.std = 5
harry.std = 4
rone.std = 4

dhruvin.sub = ["magic", "postion", "mystry"]
harry.sub = ["magic", "postion", "mystry"]
rone.sub = ["magic", "postion", "mystry"]

dhruvin.role = "Goal keeper"
harry.role = "Seeker"
rone.role = "Attacker"

print(
    f"\nDhruvin: {dhruvin.std}, {dhruvin.no_of_leaves},{dhruvin.sub},Harry: {harry.std},Rone:{rone.std}\n")
# dhruvin.no_of_leaves, instance can access the value of class but cannot change it in the class
# dhruvin instance can change value only for dhruvin like,
dhruvin.no_of_leaves = 9
print(f"Dhruvin.no_of_leaves: {dhruvin.no_of_leaves}\n")

# with help of __dict__ Student class give dictionary of class
print(Student.__dict__, "\n")

# automatic take value of dhruvin and assign to self
print(dhruvin.details(), "\n")
print(harry.details(), "\n")
print(rone.details(), "\n")
