print("---NESTED FUNCTION, GLOBAL KEYWORD---")
x = 50
def function1():
    x = 20
    def function2():
        global x #with calling global keyword it goes outof functions  
        x = 88
    print("Before calling function2: ", x) #search in function1
    function2()
    print("After calling function2: ", x)
    """ After calling function2, it search in out of function1 
        cause in function2 global variable has been called"""

function1()
print(x) #now it search in function2 cause global keyword make x = 88 in global portion

print("---Iterative Factorial Function---")
def Iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

print(Iterative(int(input("Enter num: "))))

print("---Recursive Factorial Function---")
def Recursive(n):
    if n==1:
        return 1
    else:
        return n * Recursive(n-1)

print(Recursive(int(input("Enter num: "))))

print("---Fibonacci Series---")
def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(int(input("Enter num: "))))

