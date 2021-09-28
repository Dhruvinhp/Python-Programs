def students(normal, *argsMe,**kwargs): 
    #normal argument should be write first then args and then kwargs
    print(normal)
    for i in argsMe:
        print(i)
    print("\nProfessions: ")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

normal="Student list: "
ls=["Dhruvin","Steav", "Mukesh", "Bill","Mark"]
dic={"Dhruvin":"Programmer","Steav":"CEO",
    "Mukesh":"Owner","Bill":"Developer",
    "Mark":"junior programmer"}
students(normal, *ls, **dic) 
#args and kwargs are optional