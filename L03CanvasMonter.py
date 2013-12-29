from Tkconstants import NE
import Tkinter

top = Tkinter.Tk()

canvas = Tkinter.Canvas(top, height=800, width=800, bg="white")

fx0 = 100
fy0 = 100
fw = 80
fh = 80
arc = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

ex0 = 100
ey0 = 80
ew = 30
eh = 30
oval = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")

canvas.pack()
top.focus()
top.mainloop()
