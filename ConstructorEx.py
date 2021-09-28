class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"hi, i'm {self.name} ")


person=Person('Dhruvin Prajapati')
person.talk()