from tkinter import*

w=Tk()
w.iconbitmap("r0.ico")
w.title("Register")
w.geometry('250x200')

def fun0():
    label=Label(w,text='Data successfully received').grid(columnspan=2)
    button=Button(w,text='Quit',command=w.quit).grid(columnspan=2)
label=Label(w,text='Enter your details',fg='green',bg='black',font=('Times',20)).grid(columnspan=2)
label0=Label(w,text='Name:').grid(column=0,row=1)
entry0=Entry(w).grid(column=1,row=1)
label1=Label(w,text='Permanant Address:',fg='black').grid()
entry1=Entry(w).grid(column=1,row=2)
label2=Label(w,text='Email Address:').grid()
entry2=Entry(w).grid(column=1,row=3)
label3=Label(w,text='Phone No.:').grid()
entry3=Entry(w).grid(column=1,row=4)
button0=Button(w,text='Next',command=fun0).grid(columnspan=2)


w.mainloop()