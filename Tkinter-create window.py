from tkinter import*
from PIL import Image,ImageTk
window=Tk()

def open():
    global img
    top=Toplevel()
    img=ImageTk.PhotoImage(Image.open("eagle.png").resize((300,250)))
    label0=Label(top,image=img).pack(pady=10)
    btn=Button(top,text="close window",command=top.destroy).pack()
btnn=Button(window,text="Open",command=open)
btnn.pack()

lst=["Male","Female","Others"]
def show():
    label=Label(window,text=Clicked.get()).pack()
Clicked=StringVar()
Clicked.set("Others")
drop=OptionMenu(window,Clicked,*lst).pack()
button=Button(window,text="Show selection",command=show).pack()

window.mainloop()