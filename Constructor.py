class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Run(self):
        print('Run Method')
    def Num(self):
        print('Num Method')

point = Point(10,20)
print(point.x)