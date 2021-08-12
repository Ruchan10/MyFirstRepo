from tkinter import*
root=Tk()
root.iconbitmap("10.ico")
root.title("Registration")
root.geometry('250x250')

lbl=Label(root,text="Name:")
lbl.pack()
e=Entry(root)
e.pack()

lbl2=Label(root,text="Address:")
lbl2.pack()
e2=Entry(root)
e2.pack()

lbl3=Label(root,text="Date Of Birth: ")
lbl3.pack()
e3=Entry(root)
e3.pack()

lbl4=Label(root,text="Phone no.:")
lbl4.pack()
e4=Entry(root)
e4.pack()

btn=Button(root,text="Exit",command=root.quit)
btn.pack()

root.mainloop()