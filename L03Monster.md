Lesson 03 Draw Monster on a Canvas
====================

It's draw to a monster on a canvas by combining an arc and oval. The initial program just has an arc and and oval. But it's not in the correct position. So he need be adjust the coordinate to form a correct monster.

In this lesson, the difficult part is explain the coordinate system. The way I used to explain is using a grid note book. Draw the X axis and y axis. Explain the original point (0, 0). The way of one point denoted as (x, y). How the value extend for X and Y axis.


```python
import Tkinter

top = Tkinter.Tk()


# to be easy understood, we just use fix number 800 as width and height
canvas = Tkinter.Canvas(top, height=800, width=800, bg="white")


# The coordinate used by Tkinter is the top left and bottom right point of rectangle
# which just hold the arc.
# It's fairly difficult to adjust, so we just using the center point of the arc, and length and with
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
```


* Create a new python file
* Type in all the code
* Run the code
* Explain the coordinate system.
* Adjust the coordinate to form a sound monster

