from tkinter import*
win=Tk()
win.title("Calculator")

e=Entry(win,font=('arial',20,'bold'),bd=30,insertwidth=4,bg='grey',width=30,borderwidth=20,justify='right')
e.grid(columnspan=4)
def buttonclick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def btn_cls():
    e.delete(0,END)
def btn_add():
    firstnum=e.get()
    global math
    global fnum
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def btn_mul():
    firstnum=e.get()
    global math
    global fnum
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
def btn_sub():
    firstnum=e.get()
    global math
    global fnum
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
def btn_div():
    firstnum=e.get()
    global math
    global fnum
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)

   snum=int(e.get())
   e.delete(0,END)
   if math=="mul":
       e.insert(0,fnum*snum)
   elif math == "sub":
       e.insert(0, fnum - snum)
   elif math=="add":
       e.insert(0,fnum+snum)
   elif math=="div":
       e.insert(0,fnum/snum)
btn1=Button(win,text="1",bg='blue',fg='black',bd=7,font=("arial",20,'bold'),padx=40,pady=20,command=lambda : buttonclick(1))
btn2=Button(win,text="2",bg='blue',fg='black',bd=7,font=("arial",20,'bold'),padx=40,pady=20,command=lambda : buttonclick(2))
btn3=Button(win,text="3",padx=40,pady=20,command=lambda : buttonclick(3),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn4=Button(win,text="4",padx=40,pady=20,command=lambda : buttonclick(4),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn5=Button(win,text="5",padx=40,pady=20,command=lambda : buttonclick(5),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn6=Button(win,text="6",padx=40,pady=20,command=lambda : buttonclick(6),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn7=Button(win,text="7",padx=40,pady=20,command=lambda : buttonclick(7),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn8=Button(win,text="8",padx=40,pady=20,command=lambda : buttonclick(8),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn9=Button(win,text="9",padx=40,pady=20,command=lambda : buttonclick(9),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn0=Button(win,text="0",padx=40,pady=20,command=lambda : buttonclick(0),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btnequal=Button(win,text="=",padx=40,pady=20,command=btn_equal,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnadd=Button(win,text="+",padx=38,pady=20,command=btn_add,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnsub=Button(win,text="-",padx=41,pady=20,command=btn_sub,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btndiv=Button(win,text="/",padx=41,pady=20,command=btn_div,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnmul=Button(win,text="*",padx=40,pady=20,command=btn_mul,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btncls=Button(win,text="C",padx=37,pady=20,command=btn_cls,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btn1.grid(column=0,row=3)
btn2.grid(column=1,row=3)
btn3.grid(column=2,row=3)
btn4.grid(column=0,row=4)
btn5.grid(column=1,row=4)
btn6.grid(column=2,row=4)
btn7.grid(column=0,row=5)
btn8.grid(column=1,row=5)
btn9.grid(column=2,row=5)
btn0.grid(column=0,row=6)
btnequal.grid(column=2,row=6)
btnadd.grid(column=3,row=3)
btncls.grid(column=1,row=6)
btnmul.grid(column=3,row=6)
btndiv.grid(column=3,row=5)
btnsub.grid(column=3,row=4)
win.config(bg="grey")
win.mainloop()