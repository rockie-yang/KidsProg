Lesson 02 Hello World
====================

Teaching kids programming could be tricky. They will certain loose interesting at any minute. How to sustain his interesting is a big challenge to me. I need give him some immediate effect in each lesson. All those grammar stuff could only be explained on the way.

The second lesson is just show a Hello World message box, a tradition start. It fairly easy using Tkinter, the builtin GUI library in Python.

I'd bought a IntelliJ IDEA personal license last year. It has really good code completion. It avoids quite some typing error.


He has no sense about those programming terms what so ever. I got to found some good metaphors. Today is for Function Parameter Callback.

> When I tell you run. That run is a Function

> Then if I did not say anything more. You could run forever

> Then I tell you, time=3 minutes, speed=medium. time and speed are parameters.

> How could I know you had finished the run?

> There are two ways.

> One is that I periodically asked you, "have you finished the run?"

> The other is after you finished run, call me. call me is a call back.

```python

import Tkinter
import tkMessageBox

top = Tkinter.Tk()


def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World")

b = Tkinter.Button(top, text="Hello", command=helloCallBack, width=100)

b.pack()

top.mainloop()

```

* Create a new python file
* Type in the previous code
* Save and Run the program
* Exit the program
* Experience change those text values and width of the button

