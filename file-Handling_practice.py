from tkinter import *
win = Tk()

list0 = []
def show():
    file0 = open('RK.txt', 'r+')
    data_var = file0.read()
    file0.write(' ' + e0.get())


    Label(win, text=data_var).pack()

e0 = Entry(win)
e0.pack()


history_btn = Button(win, text='History', command=show)
history_btn.pack()

win.mainloop()