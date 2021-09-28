# num = int(input(">> "))
# fact = 1

# if num < 0:
#     print("Factorial cant be negative")
# elif num == 0:
#     print("Factorial cant be zero")
# else:
#     for i in range(1, num+1):
#         fact = fact * i
#     print(fact)

def factorial(num):
    fact = 1
    if num < 0:
        print("Factorial cant be negative")
    elif num == 0:
        print("Factorial cant be zero")
    else:
        for i in range(1, num+1):
            fact = fact * i
        return fact


print(factorial(int(input(">>"))))
