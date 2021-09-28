start=False
stop=True
while True:
    command=input('>').lower()
    if command=='start':
        if start:
            print('Car already started')
        else:
            start=True
            stop=False
            print('Car started...')
    elif command=='stop':
        if stop:
            print('hey man! what are you doing car already stopped')
        else:
            stop=True
            start=False
            print('car stopped')
    elif command=='help':
        print("""
start- to start the car
stop- to stop the car
quit- to exit from the Game
        """)
    elif command=='quit':
        break
    else:
        print("sorry,I didn't get that!")

