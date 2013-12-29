from Tkconstants import NE
import Tkinter

top = Tkinter.Tk()

width = 800
height = 800
canvas = Tkinter.Canvas(top, height=height, width=width, bg="white")



coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
#
filename = Tkinter.PhotoImage(file="wn_migrate48.gif")
image = canvas.create_image(50, 50, anchor=NE, image=filename)

eye_x0 = 100
eye_y0 = 80
eye_width = 30
eye_height = 30
oval = canvas.create_oval(eye_x0, eye_y0, eye_x0 + eye_width, eye_y0 + eye_height, fill="blue")

x0 = 0
x1 = width

y = 50

import util
util.drawGrid(canvas)
# line1 = x0, y, x1, y
# canvas.create_line(line1)
# canvas.create_text(x0 + 30, y - 10, text="({0}, {1})".format(x0, y))

# canvas.create_text(x1 - 30, y - 10, text="({0}, {1})".format(x1, y))

canvas.pack()
top.focus()
top.mainloop()
