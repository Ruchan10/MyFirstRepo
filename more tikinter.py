from tkinter import*
win=Tk()
win.title('GUI')
win.configure(bg='grey')
def click():
    label=Label(win,text=f'Hello {e.get()}')
    label.pack()
    button3=Button(win, text='Dare', command=fun)
    button3.pack()
def fun():
    text1=f"Name:  {text0.get('1.0',END)}"
    label2.config(text=str(text1))
    button4 = Button(win, text='Dare2.0', command=click)
    button4.pack()

label2=Label(win, text='')
label2.place(x=660,y=600)
text0=Text(win,width=20,height=20,font=('Times New Roman',5))
text0.pack(x=100,y=100)
button0=Button(win,text='Next',command=fun)
button0.pack()
e0=Entry(win,text='hi',bg='brown',borderwidth=5)
e0.pack()
label0=Label(win,text='Tkinter',fg='green',font=('Arial',10))
label0.pack(side=TOP)
button=Button(win,text='A',padx=10,pady=10,fg='pink',bg='red',font=('Arial Bold',8),state=DISABLED)
button.pack(side=TOP)
button=Button(win,text='B',padx=11,pady=11,fg='yellow',bg='blue',font=('Times New Roman',6))
button.pack(side=TOP)
button=Button(win,text='C',padx=9,pady=9,fg='white',bg='grey',font=('Times',8))
button.pack(side=TOP)
button=Button(win,text='D',padx=12,pady=12,fg='green',bg='black',font=('Courier',10),command=fun)
button.pack(side=TOP)
e=Entry(win)
e.pack()
button=Button(win,text='B1',padx=5,pady=10,fg='red',bg='blue',command=click)
button.pack(side='left')
button0=Button(win,text='B2',padx=15,pady=15,fg='green',bg='black')
button0.pack(side='right')
button1=Button(win,text='B3',padx=20,pady=20,fg='white',bg='pink')
button1.pack(side='top')
button2=Button(win,text='B0',padx=18,pady=18,fg='grey',bg='yellow')
button2.pack(side='bottom')


win.mainloop()