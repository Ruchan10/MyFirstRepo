from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

def fun0():
    response=messagebox.askyesno("I Am Ironman",'Warning, Security Breach')
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No").pack()
image0=ImageTk.PhotoImage(Image.open('yts.jpg'))
Label(root,image=image0).pack()
button0=Button(root,text='POPUP',command=fun0)
button0.pack()
root.mainloop()