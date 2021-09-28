# num = int(input("How many terms? "))

# n1, n2 = 0, 1
# count = 0

# if num <= 0:
#     print("Please enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     while count < num:
#         print(n1)
#         n = n1 + n2
#         n1 = n2
#         n2 = n
#         count += 1


num = int(input('>>'))
n1, n2 = 0, 1
count = 0

while count < num:
    print(n1)
    n = n1+n2
    n1 = n2
    n2 = n
    count += 1
