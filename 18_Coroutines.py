def Searcher():
    import time
    # some 3 second consuming tasks
    Meritlist = ["Dhruvin", "rahul", "mahesh", "ramesh", "kishor"]
    time.sleep(3)
    # after one time execution now no need to execute this sleep portion
    # now it'll run to the while loop
    while True:
        text = yield  # coroutine
        if text in Meritlist:
            print("You are in the list")
        else:
            print("You are not in the list kindly contact admin")


search = Searcher()  # coroutine
print("Time consuming task....")
next(search)  # Generator Started
print("Next Method...")
while True:
    search.send(str(input("Enter your name: ")))  # check name
    search.send(str(input("Enter your name: ")))
    search.send(str(input("Enter your name: ")))
    # search.close() #coroutine closes
