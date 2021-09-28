class Number:
    def move(self):
        print('Move Method has been called!')
    def run(self):
        print('You are calling Run method')

Number2=Number()
Number2.x=10
Number2.y=20
print(Number2.x)
Number2.move()

Number3=Number()
Number3.x=12
Number3.run()