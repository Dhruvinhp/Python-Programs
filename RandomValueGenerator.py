import random
for i in range(3):
    print(random.randint(1,5))

name=['Akshay Kumar', 'Aayushman Khurana', 'Rajkumar Rao', 'Hrithik Roshan', 'Navazuddin ziddagi' ]
print('Nominate Actors: ',name)
bestActor = random.choice(name)
print('And the best actor award goes to', bestActor)

class Dice:
    def Roll(self):
        print(f"({random.randint(1,6)},{random.randint(1,6)})")

roll=Dice()
roll.Roll()

