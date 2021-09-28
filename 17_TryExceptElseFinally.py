try:
    f = open("xyz.py")
    f.close()
# except Exception as e: #print if try gives error
#     print("Exception---",e)
except IOError as e: #print if try gives error
    print("IO Error---",e)
except EOFError as e: #print if try gives error
    print("EOF Error---",e)     
else:
    print("..Else..") #print if except not work
finally:
    print("..Finally..") #print anyway
print("..Outside..")
    
