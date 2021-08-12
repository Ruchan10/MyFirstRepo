from tkinter import*
root=Tk()
root.title("Calculator")
#root.geometry('300x450')

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def buttonclick(number):
    current=e.get()
    e.delete(0, END)
    global exp
    exp=str(current) + str(number)
    e.insert(0, exp )

def buttonclear():
    e.delete(0,END)

def button_add():
    firstnumber=e.get()
    global fnum
    global math
    math="addition"
    fnum=float(firstnumber)
    e.delete(0, END)

def button_pwr():
    firstnumber=e.get()
    global fnum
    global math
    math="power"
    fnum=float(firstnumber)
    e.delete(0,END)

def button_mod():
    firstnumber=e.get()
    global fnum
    global math
    math="modulus"
    fnum=float(firstnumber)
    e.delete(0,END)

def button_sub():
    firstnumber = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = float(firstnumber)
    e.delete(0, END)

def button_mul():
    firstnumber = e.get()
    global fnum
    global math
    math = "multiply"
    fnum = float(firstnumber)
    e.delete(0, END)

def button_div():
    firstnumber = e.get()
    global fnum
    global math
    math = "division"
    fnum = float(firstnumber)
    e.delete(0, END)

def button_equal():
    secondnumber=float(e.get())
    e.delete(0,END)
    if math=='addition':
        e.insert(0,fnum + secondnumber)
    elif math=='subtraction':
        e.insert(0,fnum - secondnumber)
    elif math=='division':
        e.insert(0,fnum / secondnumber)
    elif math=='power':
        e.insert(0,fnum ** secondnumber)
    elif math=='subtraction':
        e.insert(0,fnum - secondnumber)
    elif math=='multiply':
        e.insert(0,fnum * secondnumber)
    elif math=='modulus':
        e.insert(0,fnum // secondnumber)

button1=Button(root,text="1",padx=40,pady=20,command=lambda : buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda : buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda : buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda : buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda : buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda : buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda : buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda : buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda : buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda : buttonclick(0))
buttonadd=Button(root,text="+",padx=39,pady=20,command=button_add)
buttonequal=Button(root,text="=",padx=90,pady=20,command=button_equal)
buttoncls=Button(root,text="CLS",padx=79,pady=20,command=buttonclear)
buttonsub=Button(root,text="-",padx=39,pady=20,command=button_sub)
buttonmul=Button(root,text="*",padx=39,pady=20,command=button_mul)
buttondiv=Button(root,text="/",padx=39,pady=20,command=button_div)
buttonpwr=Button(root,text="^",padx=39,pady=20,command=button_pwr)
buttonmod=Button(root,text="mod",padx=40,pady=20,command=button_mod)



button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonequal.grid(row=4,column=1,columnspan=2)

buttoncls.grid(row=5,column=1,columnspan=2)
buttonadd.grid(row=5,column=0)

buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)
buttonpwr.grid(row=7,column=1)
buttonmod.grid(row=7,column=0)


root.mainloop()
