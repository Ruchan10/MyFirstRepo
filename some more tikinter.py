from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

def fun0():
    messagebox.showinfo("Hello World!!","Just Do IT")
    response=messagebox.askyesno("I Am Ironman",'Warning, Security Breach')
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No").pack()

image0=ImageTk.PhotoImage(Image.open('eagle.png').resize((300,250)))
Label(root,image=image0).pack()
#image1=Image.open('eagle.png')
#resizeimg= image1.resize((300,250),Image.ANTIALIAS)
#changedimg=ImageTk.PhotoImage(resizeimg)
#Label(root,image=changedimg).pack()
#button0=Button(root,text='POPUP',command=fun0)
#button0.pack()
root.mainloop()