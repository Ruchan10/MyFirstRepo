from tkinter import * # importing all the required modules from tkinter
win = Tk() # win is a variable and Tk() creates a window

win.title('RK') # giving a title to the window if not used the title will be 'Tk'
win.iconbitmap('icon.ico') # sets the icon u want to use
win.maxsize(width=185,height=76)
win.minsize(width=185,height=76)

name=Label(win,text='ID').grid(row=0,column=0)
e1=Entry(win).grid(row=0,column=1)
password=Label(win,text='Password').grid(row=1,column=0)
e2=Entry(win).grid(row=1,column=1)
submit=Button(win,text="Submit").grid(row=3,column=1)


win.mainloop() # pauses the created window above