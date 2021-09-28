def add(n1, n2):
    return n1 + n2

def printstring(string):
    return f"You are in: {string}"

print("You are now in: ", __name__)
if __name__ == "__main__":
    print(add(10,5))
    print(printstring("NameMain.py"))
