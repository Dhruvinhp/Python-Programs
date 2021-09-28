weight= int(input('Weight: '))
unit= input('L(bs) or K(g): ')
if unit.upper()=='L':
    con=weight*0.45
    print(f"You are {con} kilos")
else:
    con=weight//0.45
    print(f"You are {con} pounds")