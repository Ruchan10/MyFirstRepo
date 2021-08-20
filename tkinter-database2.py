from tkinter import *
import sqlite3

window = Tk()

window.title('Employees')

conn = sqlite3.connect('management.db')

c = conn.cursor()
'''
c.execute("""Create Table Addresses(
user_name text,
first_name text,
last_name text,
address text,
age integer
)""")
'''


# Create a update function
def update():
    conn = sqlite3.connect('management.db')

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
    user_name = :user,
    first_name = :first,
    last_name = :last,
    address = :address,
    age = :age
    
    WHERE oid = :oid""",
              {
                  'user': user_name_editor.get(),
                  'first': first_name_editor.get(),
                  'last': last_name_editor.get(),
                  'address': address_editor.get(),
                  'age': age_editor.get(),
                  'oid': record_id
              })

    conn.commit()

    conn.close()

    editor.destroy()


# Create a edit function
def edit():
    global editor
    editor = Toplevel()
    editor.title('Update The Record')
    conn = sqlite3.connect('management.db')

    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create global variables
    global user_name_editor
    global first_name_editor
    global last_name_editor
    global address_editor
    global age_editor

    # Create text boxes
    user_name_editor = Entry(editor, bg='grey', font='times')
    user_name_editor.grid(row=0, column=1, padx=10, pady=10)

    first_name_editor = Entry(editor, bg='grey', font='times')
    first_name_editor.grid(row=1, column=1, padx=10, pady=10)

    last_name_editor = Entry(editor, bg='grey', font='times')
    last_name_editor.grid(row=2, column=1, padx=10, pady=10)

    address_editor = Entry(editor, bg='grey', font='times')
    address_editor.grid(row=3, column=1, padx=10, pady=10)

    age_editor = Entry(editor, bg='grey', font='times')
    age_editor.grid(row=4, column=1, padx=10, pady=10)

    # Labels for text boxes
    Label(editor, text='Username', bg='grey', fg='blue', font='times').grid(row=0, column=0)
    Label(editor, text='Firstname', bg='grey', fg='blue', font='times').grid(row=1, column=0)
    Label(editor, text='Lastname', bg='grey', fg='blue', font='times').grid(row=2, column=0)
    Label(editor, text='Address', bg='grey', fg='blue', font='times').grid(row=3, column=0)
    Label(editor, text='Age', bg='grey', fg='blue', font='times').grid(row=4, column=0)

    # Loop through records
    for record in records:
        user_name_editor.insert(0, record[0])
        first_name_editor.insert(0, record[1])
        last_name_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        age_editor.insert(0, record[4])

    #Create a Update button
    Button(editor, text='Update', command=update, fg='yellow', bg='green', font='times').grid(row=5, columnspan=2)

    editor.config(bg='grey')

    editor.mainloop()


# Function for delete
def delete():
    conn = sqlite3.connect('management.db')

    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)

    conn.commit()

    conn.close()


# Function to show records
def show_records():
    conn = sqlite3.connect('management.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)
    print_record = ' '
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[5]) + '\n'

    Label(window, text=print_record, bg='grey', fg='blue', font='times').grid(row=10, columnspan=2)

    conn.commit()

    conn.close()


# Function for submit button
def submit():
    conn = sqlite3.connect('management.db')

    c = conn.cursor()

    c.execute("INSERT INTO addresses Values(:user_name, :first_name, :last_name, :address, :age)", {
        'user_name': user_name.get(),
        'first_name': first_name.get(),
        'last_name': last_name.get(),
        'address': address.get(),
        'age': age.get()
    })

    conn.commit()

    conn.close()

    # Remove all entries from boxes
    user_name.delete(0, END)
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    age.delete(0, END)


# Create text boxes
user_name = Entry(window, bg='grey', font='times')
user_name.grid(row=0, column=1, padx=10)

first_name = Entry(window, bg='grey', font='times')
first_name.grid(row=1, column=1, padx=10)

last_name = Entry(window, bg='grey', font='times')
last_name.grid(row=2, column=1, padx=10)

address = Entry(window, bg='grey', font='times')
address.grid(row=3, column=1, padx=10)

age = Entry(window, bg='grey', font='times')
age.grid(row=4, column=1, padx=10)

# Labels for text boxes
Label(window, text='Username', bg='grey', fg='blue', font='times').grid(row=0, column=0)
Label(window, text='Firstname', bg='grey', fg='blue', font='times').grid(row=1, column=0)
Label(window, text='Lastname', bg='grey', fg='blue', font='times').grid(row=2, column=0)
Label(window, text='Address', bg='grey', fg='blue', font='times').grid(row=3, column=0)
Label(window, text='Age', bg='grey', fg='blue', font='times').grid(row=4, column=0)
Label(window, text='Enter ID', bg='grey', fg='blue', font='times').grid(row=7, column=0)

# Create a submit button
Button(window, text='Submit', fg='yellow', bg='green', font='times', command=submit, padx=118).grid(row=5, padx=10, pady=10, columnspan=2)

# Create a show records button
Button(window, text='Show Records', fg='yellow', font='times', bg='green', command=show_records, padx=100).grid(row=6, padx=10, pady=10, columnspan=2)

# Create a delete button and text box
delete_box = Entry(window, bg='grey', font='times')
delete_box.grid(row=7, padx=10, pady=10, columnspan=2)
Button(window, text='Delete ID', font='times', fg='yellow', bg='green', command=delete, padx=112).grid(row=8, padx=10, pady=10, columnspan=2)

# Create a edit button
Button(window, text='Edit', fg='yellow', font='times', bg='green', command=edit, padx=125).grid(row=9, padx=10, pady=10, columnspan=2)

conn.commit()

conn.close()

window.config(bg='grey')

window.mainloop()
