from Tkconstants import NE
import Tkinter
from L07CanvasGridCoord import drawGrid

top = Tkinter.Tk()

canvas = Tkinter.Canvas(top, height=800, width=800, bg="white")

filename = Tkinter.PhotoImage(file="ball.gif")
image = canvas.create_image(150, 150, anchor=NE, image=filename)


def draw_monster(canvas, fx0, fy0):
	fw, fh = 80, 80
	ew, eh = 40, 30

	eox = 30
	eoy = - 20
	ex0 = fx0 + eox
	ey0 = fy0 + eoy

	global arc
	arc = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

	global oval
	oval = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")

draw_monster(canvas, 100, 100)
drawGrid(canvas)

canvas.pack()
top.focus()
top.mainloop()
