name=input('Enter you name: ')

if len(name)<3:
    print('Name should have at least 3 character')
elif len(name)>10:
    print('Name can be maximum of 10 character long')
else:
    print('Name looks good')