import pygame as pg, sys
from pygame.locals import *
import time

xo='x'
winner=None
draw=False
width=300
height=200
white=(255,255,255)
line_color=(10,10,10)
TTT=[[None]*3,[None]*3,[None]*3]

pg.init()
fps=60
CLOCK=pg.time.Clock()
screen=pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

opening=pg.image.load('grapes.jpg')
ximg=pg.image.load('doreamon.png')
oimg=pg.image.load('grapes.jpg')
ximg=pg.transform.scale(ximg,(80,80))
oimg=pg.transform.scale(oimg,(80,80))
opening=pg.transform.scale(opening,(width,height+100))

def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

pg.draw.line(screen,line_color,(width/3,0),(width/3,0,height),7)
pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)
pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)

def draw_status():
    global draw
    if winner is None:
        msg=xo.upper()+"'s Turn"
    else:
        msg=winner.upper()+ "WON!"
    if draw:
        msg="Game Draw!"
    font=pg.font.Font(None,30)
    txt=font.render(msg,1,(255,255,255))
    screen.fill((0,0,0),(0,400,500,100))

    txt_rect=txt.get_rect(center=(width/2,500-50))
    screen.blit(txt, txt_rect)
    pg.display.update()

draw_status()

def check_win():
    global TTT, winner,draw
    for row in range(0,3):
        if((TTT[row][0]==TTT[row][1]==TTT[row][2])and(TTT[row][0]is not None)):
            winner=TTT[row][0]

print("FUVK tHIS WoRlD")