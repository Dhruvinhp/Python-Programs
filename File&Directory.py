from pathlib import Path

path=Path()
for file in path.glob('*'):
     print(file)

print("--------------")

f = open("text.txt")
print(f.read())

for line in f:
    print(line, end="")

print("----------")
print("writing in file")
print(f.readline())
f = open("text.txt","a") #append
f.write("\nI'M IRONMAN!!!") #write this line

print("----------")
print("current index: ",f.tell()) #tell character file pointer
print("after updation to zero: ",f.seek(0)) #reset file pointer to given number

print("----------")
print("with block:")
with open("text.txt") as f: #with block, no need to close file
    a = f.readlines(7) #print till 5th index
    print(a)

