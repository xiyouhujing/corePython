#!/usr/bin/env python

from Tkinter import *

top = Tk()

def get_text_file():
    filename = entry.get()
    f = open(filename)
    content = f.read()
    label['text'] = content

label = Label(top, text='open a file')
label.pack()

entry = Entry(top, width=50, textvariable='')
entry.pack()

button1 = Button(top, text='OPEN', command=get_text_file)
button1.pack()
button2 = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
button2.pack()

mainloop()