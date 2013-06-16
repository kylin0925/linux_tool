#!/usr/bin/env python
import os
def cmd():
    val = raw_input('input brightness: ')
    v=int(val)
    os.system('echo %d |sudo tee /sys/class/backlight/acpi_video0/brightness ' % v)


##
# from http://www.tutorialspoint.com/python/tk_scale.htm
##
from Tkinter import *
cmd = "gksudo \"bash -c 'echo %d > /sys/class/backlight/acpi_video0/brightness'\""

def sel():
    selection = "Value = " + str(var.get())
    label.config(text = selection)   
    os.system(cmd  % var.get())

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var ,orient=HORIZONTAL)
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()

