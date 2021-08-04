from tkinter import * # importing all the required modules from tkinter
win = Tk() # win is a variable and Tk() creates a window

win.title('RK') # giving a title to the window if not used the title will be 'Tk'
win.iconbitmap('icon.ico') # sets the icon u want to use

name= Label(win,text='Name').place(x=0,y=10)
e1=Entry(win).place(x=50,y=10)
address=Label(win,text='Address').place(x=0,y=50)
e2=Entry(win).place(x=50,y=50)
contact=Label(win,text='Contact').place(x=0,y=90)
e3=Entry(win).place(x=50,y=90)


win.mainloop() # pauses the created window above