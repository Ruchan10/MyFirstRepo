from tkinter import *
win = Tk()
win.title('RK')
win.iconbitmap('icon.ico')
#win.maxsize(width=1000,height=1000)
#win.minsize(width=1,height=1)
win.geometry('600x400')

def fun():
    text0=f"Info:- {text.get('1.0',END)}"
    label2.config(text=str(text0))

def fun0():
    label0=Label(win, text=f"I am Ruchan {e0.get()}")
    label0.pack()

label2=Label(text='Display Here')
label2.place(x=660,y=600)

e0=Entry(win, borderwidth=10)
e0.pack(padx=200,pady=100)

redbutton = Button(win, text = 'LEFT',padx=20,pady=10, fg = 'red', bg='yellow')
redbutton.pack(side = LEFT)

text=Text(win,width=25,height=10)
text.pack()

greenbutton=Button(win, text = 'RIGHT', fg='green', state=DISABLED, command=fun0)
greenbutton.pack(side=RIGHT)

bluebutton=Button(win,text='TOP',fg='BLUE', command=fun, font=('Times',10))
bluebutton.pack(expand=TRUE)


win.mainloop()