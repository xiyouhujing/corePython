#!/usr/bin/env python

from Tkinter import *

def click1():
    label['text'] = button1.config('text')[-1]

def click2():
    label['text'] = button2.config('text')[-1]

def click3():
    label['text'] = button3.config('text')[-1]

top = Tk()

label = Label(top, text='Hello World!')
label.pack()

button1 = Button(top, text='first', command=click1, bg='green', fg='white')
button1.pack(fill=X, expand=1)
button2 = Button(top, text='second', command=click2, bg='green', fg='white')
button2.pack(fill=X, expand=1)
button3 = Button(top, text='third', command=click3, bg='green', fg='white')
button3.pack(fill=X, expand=1)
quit = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=X, expand=1)

mainloop()