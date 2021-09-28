from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):
    DefaultPen = 5.0
    DefaultColor = 'black'

    def use_pen(self):
        self.activate_btn(self.pen_btn)

    def __init__(self):
        self.root = Tk()

        self.pen_btn = Button(self.root, text='pen', command=self.use_pen)
        self.pen_btn.grid(row=0, column=0)

        self.brush_btn = Button(self.root, text='Brush', command=self.use_pen)
        self.brush_btn.grid(row=0, column=1)

        self.color_btn = Button(self.root, text='Color', command=self.use_pen)
        self.color_btn.grid(row=0, column=2)

        self.eraser_btn = Button(
            self.root, text='Eraser', command=self.use_pen)
        self.eraser_btn.grid(row=0, column=3)

        self.choose_size_btn = Scale(
            self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_btn.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_btn.get()
        self.color = self.DefaultColor
        self.eraser_on = False
        self.active_btn = self.pen_btn
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<BtnRelease-1>', self.reset)


def use_brush(self):
    self.activate_btn(self.brush_btn)


def choose_color(self):
    self.eraser_on = False
    self.color = askcolor(color=self.color)[1]


def use_eraser(self):
    self.activate_btn(self.eraser_btn, eraser_mode=True)


def activate_btn(self, some_btn, eraser_mode=False):
    self.active_btn.config(relief=RAISED)
    some_btn.config(relief=SUNKEN)
    self.active_btn = some_btn
    self.eraser_on = eraser_mode


def paint(self, event):
    self.line_width = self.choose_size_btn.get()
    paint_color = 'white' if self.eraser_on else self.color
    if self.old_x and self.old_y:
        self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, full=paint_color,
                           capstyle=ROUND, smooth=True, splinesteps=36)
    self.old_x = event.x
    self.old_y = event.y


def reset(self, event):
    self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
