#check in data
print("Dhruvin Prajapati")

def grp(data, n):
    for i in data:
        if n == i:
            return True
    return False
    
print(grp([22,15,6,0,11,53,78,18], 6))
print(grp([2, 8, 3, 12, 54, 69], 4))