import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray 
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(180,210):
        for j in range(350,395):
            if data[i,j]>90:
                hit("down")
                return

    for i in range(230,250):
        for j in range(400,480):
            if data[i,j]>90:
                hit("up")
                return
    return

# for i in range(200,350):#downkey
        #for j in range(380,400):
         #   data[i,j]=0

         #for i in range(230,280):#upkey
          #  for j in range(400,500):
    
if __name__ == "__main__":
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)        
        #print(asarray(image))
'''
        for i in range(175,205):
            for j in range(350,395):
                data[i,j]=75
                    
        for i in range(190,240):
            for j in range(395,480):
                data[i,j]=0

        image.show()
        break'''