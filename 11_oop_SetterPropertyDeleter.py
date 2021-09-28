"""
property: we use property decorator for avoid attributes value changing while runtime 
        like, if we want to change email id without using property it'll not gonna change it, 
        you should write it in property rather than writing in __init__ constructor.

setter: to avoid error which says can't set attribute
        if we want to give value to the email so we must use setter like,
        dhruvin.email = "this.that@gmail.com" 

deleter: to delete the value of emailid and didn't return none, which is done by property
"""


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}{self.lname}" #it'll not gonna change it

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email not set, please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter  # first write in which function you want apply setter then write .setter
    def email(self, stringAttribute):
        print("Setting Now...")
        name = stringAttribute.split("@")[0]  # take value of list index[0]
        # before @, take value of list index[0]
        self.fname = name.split(".")[0]
        # before @, take value of list index[1]
        self.lname = name.split(".")[1]

    @email.deleter  # first write in which you want apply deleter then write .setter
    def email(self):
        self.fname = None  # set value of fname and lname by None
        self.lname = None


dhruvin = Employee("Dhruvin", "Prajapati")
print(dhruvin.email)  # by property
# with the help of property decorator now you don't have to put bracket() after email
# cause now email is attribute not a function

dhruvin.fname = "Vrunda"  # by setter
print(dhruvin.email)

dhruvin.email = "this.that@gmail.com"  # by setter
# by setter it'll split by . and @
print(f"fname: {dhruvin.fname}, lname: {dhruvin.lname}")

del dhruvin.email  # by deleter, then it'll check in property
print(dhruvin.email)
