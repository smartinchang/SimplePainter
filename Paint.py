from tkinter import *
from tkinter.ttk import *

def clicked(event):
    global x1
    global y1
    global draw
    x1, y1 = event.x, event.y
    shape = cmb_shape.get()
    color = cmb_color.get()
    size = int(cmb_size.get())
    if (shape == "point"):
        draw = canvas.create_oval(x1, y1, x1, y1, fill = color, outline = color, width = size)
    elif (shape == "line"):
        draw = canvas.create_line(x1, y1, x1, y1, fill = color, width = size)
    elif (shape == "rectangle"):
        draw = canvas.create_rectangle(x1, y1, x1, y1, outline = color, width = size)
    elif (shape == "oval"):
        draw = canvas.create_oval(x1, y1, x1, y1, outline = color, width = size)
    elif (shape == "square"):
        draw = canvas.create_rectangle(x1, y1, x1, y1, outline = color, width = size)
   

def motion(event):
    global draw
    x2, y2 = event.x, event.y
    shape = cmb_shape.get()
    color = cmb_color.get()
    size = int(cmb_size.get())
    if (shape == "point"):
        draw = canvas.create_oval(x2, y2, x2, y2, fill = color, outline = color, width = size)
    elif (shape == "line"):
        canvas.delete(draw)
        draw = canvas.create_line(x1, y1, x2, y2, fill = color, width = size)
    elif (shape == "rectangle"):
        canvas.delete(draw)
        draw = canvas.create_rectangle(x1, y1, x2, y2, outline = color, width = size)
    elif (shape == "oval"):
        canvas.delete(draw)
        draw = canvas.create_oval(x1, y1, x2, y2, outline = color, width = size)
    elif (shape == "square"):
        canvas.delete(draw)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        d = min(dx, dy)
        if ((x2 - x1) > 0):
            sx = 1
        else:
            sx = -1
        if ((y2 - y1) > 0):
            sy = 1
        else:
            sy = -1
        draw = canvas.create_rectangle(x1, y1, x1 + sx * d, y1 + sy * d, outline = color, width = size)
    
window = Tk()

window.title("Draw Rectangle with Mouse")
window.geometry('600x500')

cmb_shape = Combobox(window)
cmb_shape['values']= ("point", "line", "rectangle", "oval", "square")
cmb_shape.current(0)
cmb_shape.grid(column = 0, row = 0)

cmb_color = Combobox(window)
cmb_color['values']= ("red", "green", "blue")
cmb_color.current(0)
cmb_color.grid(column = 1, row = 0)

cmb_size = Combobox(window)
cmb_size['values']= ("1", "2", "3", "4", "5")
cmb_size.current(0)
cmb_size.grid(column = 2, row = 0)

canvas = Canvas(window, width = 600, height = 480, background = "white")
canvas.bind('<Button-1>', clicked)
canvas.bind("<B1-Motion>", motion)
canvas.grid(columnspan = 40, row = 1)

window.mainloop()
