def function1(a,b):
    """This function print average of two number""" #docstring
    average=((a+b)/2)
    return average

print(function1.__doc__) #print docstring
print(function1(5,7))