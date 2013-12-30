Lesson 05 Grid and Loop
====================

In previous lessons, the coordination change is quite time costly. It needs change and run, change and run. It needs quite some round to place items into correct places. He should already realized that the need for some guide of the coordinate.

And in previous lessons, the coordination system has been explained quite few times. In this lesson, I'm try to more formalize it. I using following steps to clarify the coordination system.
1. Draw X and Y axises
2. Point the original point
3. Review concept of (x, y)
4. Let him give first and second horizontal line's coordination (x0, y0) - (x1, y1)
5. Let him give first and second vertical line's coordination (x0, y0) - (x1, y1)

He does not have those abstract concept. So explain clear what is a loop. I use following game to explain.
1. Let him write done numbers 10, 20, 30, 40, 50, 60 on paper
2. Cut those numbers
3. Tell him every time I ask a new number, give me the smallest number
4. Give me the next number(from 10 to 60), I draw a line
5. I said give me the next number
6. He said there is no numbers left, then I explain the loop is end



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
```

* Create a new python file
* Type in the vertical part
* Let him play with the horizontal part
