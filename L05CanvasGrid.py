import Tkinter

top = Tkinter.Tk()

width = 800
height = 800
canvas = Tkinter.Canvas(top, height=height, width=width, bg="white")

# draw vertical lines (from top to bottom)
fill = "gray"
xs = range(10, 800, 10)
for x in xs:
	x0, y0 = x, 0
	x1, y1 = x, 800
	canvas.create_line(x0, y0, x1, y1, dash=(1, 3), fill=fill)

# draw horizontal lines (from left to right)
ys = range(10, 800, 10)
for y in ys:
	x0, y0 = 0, y
	x1, y1 = 800, y
	canvas.create_line(x0, y0, x1, y1, dash=(1, 3), fill=fill)

canvas.pack()
top.focus()
top.mainloop()

