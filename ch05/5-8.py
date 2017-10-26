#!/usr/bin/env python

from Tkinter import *

def openFile():
    filename = entry.get()
    f = open(filename)
    content = f.read()
    text.insert(END, content)
    f.close()

def saveFile():
    filename = entry.get()
    f = open(filename, 'w')
    content = text.get("0.0", "end")
    f.write(content)
    f.close()

def secTk():
    sec = Tk()

    def save_quit():
        saveFile()
        sec.quit()

    label = Label(sec, text='Save the file? Yes or No?', fg='red')
    label.grid(columnspan=5)
    button1 = Button(sec, text='Yes', command=save_quit)
    button1.grid(row=2, column=2)
    button2 = Button(sec, text='No', command=top.quit)
    button2.grid(row=2, column=4)

top = Tk()
top.title('Text Editor')

entry = Entry(top, textvariable='', width=40)
entry.grid(row=0, sticky=W)

openBut = Button(top, text='Open', width=10, command=openFile)
openBut.grid(row=0, column=1, sticky=W)
saveBut = Button(top, text='Save', width=10, command=saveFile)
saveBut.grid(row=0, column=2, sticky=W)

text = Text(top, width=60)
text.grid(columnspan=3, sticky=W+E+N+S)

quitBut = Button(top, text='Quit', command=secTk, bg='red', fg='white', width=10)
quitBut.grid(columnspan=3)

mainloop()
