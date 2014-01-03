from Tkconstants import CENTER
import Tkinter
from random import random

from util import *


# from L07CanvasGridCoord import drawGrid

top = Tkinter.Tk()

# frame = Tkinter.Frame(top, width=800, height=800)


def key_press(event):
	print "pressed", repr(event.char)

move_step = 10


def left_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0 - move_step, fy0, fx1 - move_step, fy1)
	canvas.coords(eye, ex0 - move_step, ey0, ex1 - move_step, ey1)


def right_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0 + move_step, fy0, fx1 + move_step, fy1)
	canvas.coords(eye, ex0 + move_step, ey0, ex1 + move_step, ey1)


def up_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0, fy0 - move_step, fx1, fy1 - move_step)
	canvas.coords(eye, ex0, ey0 - move_step, ex1, ey1 - move_step)


def down_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0, fy0 + move_step, fx1, fy1 + move_step)
	canvas.coords(eye, ex0, ey0 + move_step, ex1, ey1 + move_step)


def a_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0 - move_step, by0)


def d_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0 + move_step, by0)


def w_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0, by0 - move_step)


def s_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0, by0 + move_step)


def space_pressed(event):
	canvas.itemconfigure(face, start=close_start)
	canvas.itemconfigure(face, extent=close_extent)

	bx0, by0 = canvas.coords(ball)
	x0, y0, x1, y1 = canvas.coords(face)
	fx0, fy0 = centerCoor(x0, y0, x1, y1)
	if is_in_mouth(bx0, by0, fx0, fy0):
		canvas.delete(ball)

		create_ball()


def is_in_mouth(bx0, by0, fx0, fy0):
	if (fx0 < bx0 < fx0 + fw) and (fy0 < by0 < by0 + fh):
		return True
	else:
		return False


def space_released(event):
	canvas.itemconfigure(face, start=open_start)
	canvas.itemconfigure(face, extent=open_extent)

top.bind("<KeyPress-space>", space_pressed)
top.bind("<KeyRelease-space>", space_released)

top.bind("a", a_pressed)
top.bind("d", d_pressed)
top.bind("s", s_pressed)
top.bind("w", w_pressed)

top.bind("<Left>", left_pressed)
top.bind("<Right>", right_pressed)
top.bind("<Up>", up_pressed)
top.bind("<Down>", down_pressed)

# frame.pack()


canvas = Tkinter.Canvas(top, height=800, width=800, bg="white")

filename = Tkinter.PhotoImage(file="ball.gif")


def create_ball():
	global ball, canvas

	x, y = int(random() * 800), int(random() * 800)

	ball = canvas.create_image(x, y, anchor=CENTER, image=filename)


def draw_monster(canvas, fx0, fy0):
	global face, fw, fh

	fw, fh = 80, 80
	ew, eh = 40, 30

	ex0 = fx0 + 30
	ey0 = fy0 - 20

	global open_start, open_extent
	global close_start, close_extent
	open_start, open_extent = 0, 270
	close_start, close_extent = -20, 310

	face = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

	global eye
	eye = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")


create_ball()
draw_monster(canvas, 100, 100)


canvas.pack()
top.focus()
top.mainloop()
