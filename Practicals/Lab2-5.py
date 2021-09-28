#Fibonacci using function
print("Dhruvin Prajapati")
def fib():
    n = int(input("Enter Number: "))
    c, a, b, s = 1, 0, 1, 0
    print("\nFibonacci:")
    while(c<=n):
        print(s, end =" ")
        c += 1
        a = b
        b = s
        s = a + b
fib()