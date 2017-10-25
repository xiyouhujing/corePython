#!/usr/bin/env python

from Tkinter import *

def click():
    val = v.get()
    if val == 1:
        label['text'] = 'first'
    elif val == 2:
        label['text'] = 'second'
    elif val == 3:
        label['text'] = 'third'

top = Tk()

label = Label(top, text='Hello World!')
label.pack()

v = IntVar()
rad1 = Radiobutton(top, text='first', variable=v, value=1)
rad1.pack(anchor=W)
rad2 = Radiobutton(top, text='second', variable=v, value=2)
rad2.pack(anchor=W)
rad3 = Radiobutton(top, text='third', variable=v, value=3)
rad3.pack(anchor=W)

update = Button(top, text='UPDATE', command=click, bg='green', fg='white')
update.pack(fill=X)
quit = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=X)


mainloop()