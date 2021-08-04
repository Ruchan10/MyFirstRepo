from tkinter import*
from PIL import Image, ImageTk
rk=Tk()
'''
rk.maxsize(width=300,height=300)
rk.minsize(width=300,height=300)

image0=ImageTk.PhotoImage(Image.open("sunflower.png"))
label0=Label(image=image0)
label0.pack()
bg = PhotoImage(file="Download.png")
label1=Label(rk,image=bg)
label1.pack()
button0=Button(rk,text="Quit",command=rk.quit)
button0.pack()
'''
photo=Image.open('Download.png')
resize0=photo.resize((300,300),Image.ANTIALIAS)
resized=ImageTk.PhotoImage(resize0)
label0=Label(rk,image=resized)
label0.pack()



rk.mainloop()