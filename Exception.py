try:
    age= int(input('Enter Age: '))
    income=20000
    risk=income/age
    print('Your age is ',age)
    print('Risk is ',risk)
except ZeroDivisionError: #shows a exception handling for Zero Division
    print('Age cannot be ZERO')
except ValueError: #shows a Exception handling for Value Error
    print('Enter valid value')