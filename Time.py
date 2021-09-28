import time

initial = time.time()
k=0
while k<10:
    print("DHRUVIN")
    k+=1

whiletime = time.time() - initial
print("WHILE TIME:", whiletime,"\n")
initial2 = time.time()
for i in range(10):
    print("PRAJAPATI")
    i+=1
fortime= time.time() - initial2
print("FOR TIME: ",fortime )
time.sleep(2)
local = time.asctime(time.localtime(time.time()))
print("TODAYS TIME: ", local)