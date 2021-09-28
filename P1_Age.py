#Find the Age
birth = int(input("Enter your age or birth year: "))

if 0<birth<=150:
    print("your age is", birth)
    b = 100 + birth
    print("Your age after 100 year: ",b)
    year = int(input("Enter Year to know your age in that year: "))
    a = year - (2021 - birth)
    if a>=150:
        print(f"Your age in {year} is {a}")
        print("you seems to be oldest person alive")
    elif a<0:
        print("You'r not born yet!")
    else:
        print(f"Your age in {year} is {a}")

elif 1900<birth<2021:
    print("Your birthyear is", birth)
    b = (2021 + 100) - birth
    print("Your age after 100 years: ",b)
    year = int(input("Enter year to know your age in that year: "))
    a = year - birth
    if a>=50:
        print(f"Your age in {year} is {a}")
        print("you seems to be oldest person alive")
    elif a<0:
        print("You'r not born yet!")
    else:
        print(f"Your age in {year} is {a}")
else:
    print("Invalid value")