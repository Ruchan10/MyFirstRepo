from tkinter import * # importing all the required modules from tkinter
win = Tk() # win is a variable and Tk() creates a window

win.title('RK') # giving a title to the window if not used the title will be 'Tk'
win.iconbitmap('icon.ico') # sets the icon u want to use

#win.maxsize(width=1000,height=1000) # limits the size of the window
#win.minsize(width=1,height=1) # limits minimum size of thw window
win.geometry('600x400') # opens the window in given width and height
redbutton = Button(win, text = 'LEFT', fg = 'red') # creates a button
redbutton.pack(side = LEFT)
greenbutton=Button(win, text = 'RIGHT', fg='green')
greenbutton.pack(side=RIGHT)
bluebutton=Button(win,text='TOP',fg='BLUE')
bluebutton.pack(side=TOP)
blackbutton=Button(win,text='BOTTOM',fg='black')
blackbutton.pack(side=BOTTOM)
