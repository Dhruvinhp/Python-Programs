"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
Generator - only one time accessible Iterator  
"""
def gen(n): #Generator
    for i in range(n):
        yield i # on the fly value generate, not need store in RAM

# print(gen())
g =  gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__(),"\n")

d = "Dhruvin" # only string can iterate int value don't have iter method
i = iter(d)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
# for i in d:
#     print(i)

# def fib():
#     n, c, a, b, s = 10, 1, 0, 1, 0
#     print("\nFibonacci:")
#     while(c<=n):
#         print(s, end =" ")
#         c += 1
#         a = b
#         b = s
#         s = a + b
# fib()

# def fac():
#     fac = 1
#     n = 5
#     if n >=1:
#         for i in range(1, n+1):
#             fac = fac * i
#         print(f"\nFactorial of {n} is : {fac}\n")
# fac()

def factorial(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x > 0:
        while b<x:
            a = a * b
            b+=1
    yield a
z = 10
g = (factorial(n) for n in range (1, 10))
print(next(g))

def fib(n):
    a, b=0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
print(fib(5))