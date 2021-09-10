# It is used to import all the required modules for our calculator
from tkinter import*

# Then let's create window
win=Tk()

# Setting a name and icon for the window
win.title("calculator")
win.iconbitmap("calculator.ico")


# Creating a  box to display the all the content
e=Entry(win,font=('arial',20,'bold'),bd=30,insertwidth=4,bg='grey',width=30,borderwidth=20,justify='right')
e.grid(columnspan=5)

# Setting size of the window
x = 650
y = 500
win.geometry(f"{x}x{y}")

file0 = open('abc.txt', 'w')
file0.write("")
file0.close()

def b_del():
    current_number = e.get()
    length = len(current_number) - 1
    e.delete(length, END)


def show():
    global x
    global y
    file0 = open('abc.txt', 'r+')
    data_var = file0.read()
    file0.write('\n')
    file0.close()

    Label(win, text=data_var,font=("arial",20,'bold'), bg="grey").grid(columnspan=5,rowspan=6)
    y += 20
    win.geometry(f"{x}x{y}")


# All the required buttons
def buttonclick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num)) # Concatinate the strings

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

def btn_equal():
   snum=int(e.get())
   e.delete(0,END)

   file0 = open('abc.txt', 'r+')
   file0.read()
   file0.write(str(fnum))
   file0.close()

   if math=="mul":
       m = fnum * snum
       e.insert(0, m)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" * " + str(snum) + ' = ' + str(m))
       file0.close()

   elif math == "sub":
       s = fnum - snum
       e.insert(0, s)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" - " + str(snum) + ' = ' + str(s))
       file0.close()

   elif math=="add":
       a = fnum+snum
       e.insert(0, a)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" + " + str(snum) + ' = ' + str(a))
       file0.close()

   elif math=="div":
       d = fnum/snum
       e.insert(0, d)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" / " + str(snum) + ' = ' + str(d))
       file0.close()


# All the required buttons
btn1=Button(win,text="1",padx=40,pady=20,command=lambda : buttonclick(1),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn2=Button(win,text="2",padx=40,pady=20,command=lambda : buttonclick(2),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn3=Button(win,text="3",padx=40,pady=20,command=lambda : buttonclick(3),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn4=Button(win,text="4",padx=40,pady=20,command=lambda : buttonclick(4),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn5=Button(win,text="5",padx=40,pady=20,command=lambda : buttonclick(5),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn6=Button(win,text="6",padx=40,pady=20,command=lambda : buttonclick(6),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn7=Button(win,text="7",padx=40,pady=20,command=lambda : buttonclick(7),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn8=Button(win,text="8",padx=40,pady=20,command=lambda : buttonclick(8),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn9=Button(win,text="9",padx=40,pady=20,command=lambda : buttonclick(9),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btn0=Button(win,text="0",padx=40,pady=20,command=lambda : buttonclick(0),bg='blue',fg='black',bd=7,font=("arial",20,'bold'))
btnequal=Button(win,text="=",padx=99,pady=19,command=btn_equal,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnadd=Button(win,text="+",padx=35,pady=73,command=btn_add,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnsub=Button(win,text="-",padx=40,pady=20,command=btn_sub,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btndiv=Button(win,text="/",padx=41,pady=20,command=btn_div,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btnmul=Button(win,text="*",padx=40,pady=20,command=btn_mul,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
btncls=Button(win,text="C",padx=37,pady=18,command=btn_cls,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))
history_btn = Button(win, text='History',padx=6,pady=21, command=show,bg='grey67',fg='orange',bd=7,font=("arial",19,'bold'))
bdel = Button(win, text="←", padx=30, pady=18, command=b_del,bg='grey67',fg='orange',bd=7,font=("arial",20,'bold'))



# First row
btn7.grid(column=0,row=3)
btn8.grid(column=1,row=3)
btn9.grid(column=2,row=3)
btnadd.grid(column=4,row=4,rowspan=2)
history_btn.grid(column=1, row=6)
bdel.grid(column=4, row=3)

# Second row
btn4.grid(column=0,row=4)
btn5.grid(column=1,row=4)
btn6.grid(column=2,row=4)
btnsub.grid(column=3,row=4)

# Third row
btn1.grid(column=0,row=5)
btn2.grid(column=1,row=5)
btn3.grid(column=2,row=5)
btndiv.grid(column=3,row=5)

# Fourth row
btn0.grid(column=0,row=6)
btncls.grid(column=3,row=3)
btnmul.grid(column=2,row=6)
btnequal.grid(column=3,row=6, columnspan=2)

# Changing the background color of the window
win.config(bg="grey")

win.mainloop()