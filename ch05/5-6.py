#!/usr/bin/env python

from Tkinter import *

def click():
    v = entry.get()
    label['text'] = v

top = Tk()

label = Label(top, text='Hello World!')
label.pack()

str = StringVar()
str.set('Hello World!')
entry = Entry(top, width=60, textvariable=str)
entry.pack()

update = Button(top, text='UPDATE', command=click, bg='green', fg='white')
update.pack(fill=X)
quit = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=X)


mainloop()