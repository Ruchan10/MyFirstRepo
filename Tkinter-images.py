from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
win= Tk()
win.title('Just For Images')
win.iconbitmap('10.ico')
def fun0():
    messagebox.showinfo("I am Ruchan", "This is me")
    button0 = Button(win, text='EXIT', command=win.quit)
    button0.pack(side=BOTTOM)
def fun1():
    given=messagebox.askyesnocancel("This is my msgbox", "Do whatever u want to ")
    Label(win,text=given).pack()
    if given==1:
        Label(win, text='YES YES YES').pack()
    else:
        Label(win, text='Noooooo!!!').pack()

image0=ImageTk.PhotoImage(Image.open('Download.png').resize((300,250),Image.ANTIALIAS))
label0=Label(win, image=image0)
label0.pack()

button1=Button(win, text='Dare U', command=fun0)
button1.pack()

button2=Button(win, text="wanna popup", command=fun1).pack()


win.mainloop()