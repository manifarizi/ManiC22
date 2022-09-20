import ITools
import Errors
import string
import tkinter as tk

root = tk.Tk()
root.geometry("512x512")
root.maxsize(512, 512)
root.minsize(512, 512)
draw = tk.Canvas(root, background='black')
draw.pack(fill=tk.BOTH, expand=1)
hexdi = string.hexdigits

key = (0, 'p')
key_is = 0

task_list = []
def key_release(event):
    global key
    try:
        key = (ord(event.char), 'r')
    except TypeError:
        key = (0, 'r')
    return key

def key_press(event):
    global key
    try:
        key = (ord(event.char), 'p')
    except TypeError:
        key = (0, 'p')
    return key

root.bind('<KeyRelease>', key_release)
root.bind('<KeyPress>', key_press)

def pixel(x, y, c, name):
    global draw
    try:
        draw.create_rectangle(x * 2, y * 2, (x * 2) + 2, (y * 2) + 2, fill=('#' + ''.join([str(c)[i] if str(c)[i] in hexdi else '0' for i in range(len(str(c)))][1:4])), outline="")
    except KeyError:
        ITools.Error(name, Errors.VarNotDefined, 'ac')

def run(_):
    global root
    root.mainloop()

def task():
    global task_list
    for i in task_list:
        pixel(*i)
    root.update()

def do_nothing():
    pass

def wait(time):
    var = tk.IntVar()
    root.after(time, var.set, 1)
    root.wait_variable(var)