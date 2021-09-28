while True:
    balance=10000
    print("WELCOME IN AnyTimeMoney")
    print("")
    print("""please choose an option
    1. BALANCE
    2. WITHDRAW
    3. DEPOSIT
    4. QUIT
    """)
    try:
        option=int(input("Enter Option: "))
    except Exception as e:
        print("ERROR: ", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    if option==1:
        print("Balance Rs.",balance)
    if option==2:
        print("Balance Rs.",balance)
        withdraw=float(input("Enter Ammount Rs."))
        if withdraw<balance:
            forbalance=(balance-withdraw)
            print("Forward Balance Rs.",forbalance)
        elif withdraw>balance:
            print("Insufficient Balance")
        else:
            print("NONE WITHDRAW MADE")
    if option==3:
        print("Balance Rs.",balance)
        deposit=float(input("Enter Ammount Rs."))
        if deposit>0:
            forbalance=(balance+deposit)
            print("Forward balance Rs.",forbalance)
        else:
            print("Please Enter Valid Ammount")
    if option==4:
        print("Process Canceled")
        exit()
