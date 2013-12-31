Lesson 06 Add Coordinate Label and Better Grid
====================

In previous lessons, the grids are all drew with dashed lines. Which makes difficult to tell which is which. For people with intense phobia will be tough to look at that grid.

Today's lesson have two parts

1.  For every 5 line, change from dash line to solid line. It is also use to explain if statement.
1.  On one side of the line, add coordinate label. It is used to make easy to tell coordinate on the canvas. Other wise,   most likely need count from beginning to tell which point it is.



```python
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
	if x % 50 == 0:
		canvas.create_line(x0, y0, x1, y1, fill=fill)
		canvas.create_text(x0, y0, text="{0}".format(x), fill=fill)
	else:
		canvas.create_line(x0, y0, x1, y1, dash=(1, 3), fill=fill)

# draw horizontal lines (from left to right)
ys = range(10, 800, 10)
for y in ys:
	x0, y0 = 0, y
	x1, y1 = 800, y
	if y % 50 == 0:
		canvas.create_line(x0, y0, x1, y1, fill=fill)
		canvas.create_text(x0, y0, text="{0}".format(y), fill=fill)
	else:
		canvas.create_line(x0, y0, x1, y1, dash=(1, 3), fill=fill)

canvas.pack()
top.focus()
top.mainloop()
```

* Directly change files on Lesson 05
* Type in the vertical part
* Let him finish the horizontal part

