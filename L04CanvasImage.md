Lesson 3 Images
====================

Today's lessons is how to add images to the canvas. One of the image is used as background. Others are used for as foreground.

Tkinter has very limited image type support. For common image types, it only support gif format. For other images types, we can use PIL.

The Python Imaging Library (PIL) supports images in a much wider variety of formats. Its ImageTk class is specifically designed for displaying images within Tkinter applications.

```python
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
```


* Google a jpg image as background and save it in the project directory
* Resize and crop to get a 800*800 image to as background
* Google few other gif files as foreground and save it in the project directory
* Create a new python file
* Type in all the code
* Replace the example file names with the file names downloaded
* Run the code
* Explain the coordination system.