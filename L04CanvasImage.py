from Tkconstants import *
import Tkinter
from PIL import ImageTk

top = Tkinter.Tk()

frame = Tkinter.Frame(top, width=800, height=800)
frame.pack()

canvas = Tkinter.Canvas(frame, height=800, width=800)

bg = ImageTk.PhotoImage(file='background.jpg')
bgImage = canvas.create_image(0, 0, image=bg, anchor=NW)

filename = Tkinter.PhotoImage(file="ball.gif")
image = canvas.create_image(150, 150, anchor=NE, image=filename)


canvas.pack()
top.focus()
top.mainloop()
