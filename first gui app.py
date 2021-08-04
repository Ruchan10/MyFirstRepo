from tkinter import*
win=Tk()
win.title('FACEBOOK')
win.iconbitmap('10.ico')
win.minsize(width=200,height=200)
def fun1():
    label2=Label(text='Successfully got your ID and Password')
    label2.pack()
def fun0():
    label1=Label(win,text=f'''Hello {entry0.get()}
     Please, Enter your password''')
    label1.pack()
    entry1=Entry(win)
    entry1.pack()
    button1=Button(win,text='Next',command=fun1)
    button1.pack()

label0=Label(win,text='Login',fg='red',bg='green')
label0.pack(side=TOP,expand=FALSE)
label2=Label(win,text='Enter your username')
label2.pack()
entry0=Entry(win)
entry0.pack()
button0=Button(win,text='Next',command=fun0)
button0.pack()
win.mainloop()