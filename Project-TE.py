from tkinter import *
from tkinter import filedialog
from tkinter import font

win = Tk()
win.title('Notepad')
win.iconbitmap('eagle.png')
win.geometry("1200x660")

# Create new file function
def new_file():
    my_text.delete("1.0", END)
    win.title('New File - TextPad!')
    status_bar.config(text="New File          ")

def open_file():
    # Delete previous data
    my_text.delete("1.0", END)

    # Take file name
    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    # Update status bar
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/gui/", "")
    win.title(f'{name} - Textpad')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def saveas_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdri="C:/gui/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("C:/gui/", "")
        win.title(f'{name} - TextPad')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

# Create main frame
my_frame = Frame(win)
my_frame.pack(pady=5)

# Create scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure scrollbar
text_scroll.config(command=my_text.yview)

# CreateMenu
my_menu = Menu(win)
win.config(menu=my_menu)

# Add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)

# Add edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add status bar
status_bar = Label(win, text="Ready     ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


win.mainloop()