#concatenate
print("Dhruvin Prajapati")

def concatenate(list):
    a = ''
    for e in list:
        a += str(e)
    return a

print(concatenate([1, 8, 0, 1, 6, 3, 1, 1, 6, 0, 1, 8 ]))