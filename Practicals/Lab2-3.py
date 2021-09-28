#Difference between dates
print("Dhruvin Prajapati")
from datetime import datetime

def days():
    print("Enter Dates in YYYY-MM-DD format")
    d1 = str(input("Enter first date:"))
    d2 = str(input("Enter second date: "))
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
    
print(days(),"Days")