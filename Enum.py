ls=["car","bike","Riksha","cab","airplane","helicopter","cycle","train","bus"]
i=0
for item in ls:
    if i%2 is not 0:
        print("Transportation Even: ", item)
    i+=1
print("\n")

for ts, item in enumerate(ls):
    if ts%2==0:
        print(f"Transportation Odd: ", item)

#you can do both, second method is using enumerate function
