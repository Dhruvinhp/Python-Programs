def dect1(num1):
    def noexc():
        print("Executing...")
        num1()
        print("Executed")
    return noexc

@dect1
def de():
    print("---FUNCTION---")
#de = dect1(de)

de()
#Use: if we need to use one funtion in many function so we can use this as decorator by applying to functions.
