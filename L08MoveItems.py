from Tkconstants import NE
import Tkinter
# from L07CanvasGridCoord import drawGrid

top = Tkinter.Tk()

frame = Tkinter.Frame(top, width=800, height=800)


def key_press(event):
	print "pressed", repr(event.char)

move_step = 3

def left_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(arc)
	ex0, ey0, ex1, ey1 = canvas.coords(oval)
	canvas.coords(arc, fx0 - move_step, fy0, fx1 - move_step, fy1)
	canvas.coords(oval, ex0 - move_step, ey0, ex1 - move_step, ey1)

def right_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(arc)
	ex0, ey0, ex1, ey1 = canvas.coords(oval)
	canvas.coords(arc, fx0 + move_step, fy0, fx1 + move_step, fy1)
	canvas.coords(oval, ex0 + move_step, ey0, ex1 + move_step, ey1)


top.bind("a", key_press)
top.bind("<Left>", left_pressed)
top.bind("<Right>", right_pressed)
# frame.bind("a", key_press)
frame.pack()

canvas = Tkinter.Canvas(frame, height=800, width=800, bg="white")

# canvas.bind("a", key_press)
filename = Tkinter.PhotoImage(file="ball.gif")
image = canvas.create_image(150, 150, anchor=NE, image=filename)


def move_monster(canvas, direction):
	if direction == 'Left':
		pass
	# elif direction == 'Right'



def draw_monster(canvas, fx0, fy0):
	fw, fh = 80, 80
	ew, eh = 40, 30

	ex0 = fx0 + 30
	ey0 = fy0 - 20

	global arc
	arc = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

	global oval
	oval = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")


draw_monster(canvas, 100, 100)

canvas.pack()
top.focus()
top.mainloop()
