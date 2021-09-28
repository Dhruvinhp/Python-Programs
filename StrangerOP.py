num1 = 256
num2 = 256

print(num1==num2)

print(num1 is num2)

num3=300
num4=300

print(num3==num4)

print(num3 is num4)

x= y =1
z=0
a=(x and z) and (x or y)
print(a)

def test(m, n):
    b= range(n, (m*n)+1, n)
    print(*b)

