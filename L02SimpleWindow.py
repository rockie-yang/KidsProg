import Tkinter
import tkMessageBox

top = Tkinter.Tk()


def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World")


b = Tkinter.Button(top, text="Hello", command=helloCallBack, width=100)

b.pack()

top.mainloop()