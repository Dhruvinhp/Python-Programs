"""
Multiple inheritance create confussion that's why we avoid it
java doesnt support
python and c++ can support 
"""


class A:
    def met(self):
        print("A")


class B(A):
    def met(self):
        print("B")


class C(A):
    def met(self):
        print("C")


class D(B, C):
    # def met(self):
    #     print("D")
    pass


a = A()
c = C()
d = D()

d.met()
c.met()
