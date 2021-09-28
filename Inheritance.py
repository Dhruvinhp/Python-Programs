class animal:
    def walk(self):
        print('and Walk')
class Dog(animal):
    def bark(self):
        print('Dog can Bark')
class Cat(animal):
    def Meow(self):
        print('Cat can meow')

dog=Dog()
dog.bark()
dog.walk()

cat=Cat()
cat.Meow()
cat.walk()