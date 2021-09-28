# Access Specifier:
# Public variable can access by all classes
# Protected variable only can access by class itself and child classes
# private variable only can access by class itself

class info:
    publicVar = 15
    _protectedVar = 10  # Protected Variable
    __privateVar = 5  # Private Variable
    print(__privateVar)  # you can use Private variable into in this class only


class otherinfo(info):
    pass
    # return(info._protectedVar)


dh = info()
ru = otherinfo()
print(dh.publicVar)
print(ru._protectedVar)
print(dh._info__privateVar)  # if you want to access private values
# Outside class private variable needs to call like this, _classname__VariableName
