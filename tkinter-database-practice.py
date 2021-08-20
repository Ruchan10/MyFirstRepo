from tkinter import*
import sqlite3

root = Tk()
root.title("Database")

# create a database or connect
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()
'''
# Create Table
c.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer
)""")
'''

# Function to save
def save():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              }
              )

    conn.commit()

    conn.close()

    editor.destroy()


# Function to update
def edit():
    global editor
    editor = Toplevel()
    editor.title('Update The Record')
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create global variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create text boxes
    f_name_editor = Entry(editor)
    f_name_editor.grid(row=0, column=1, padx=10, pady=10)

    l_name_editor = Entry(editor)
    l_name_editor.grid(row=1, column=1, padx=10, pady=10)

    address_editor = Entry(editor)
    address_editor.grid(row=2, column=1, padx=10, pady=10)

    city_editor = Entry(editor)
    city_editor.grid(row=3, column=1, padx=10, pady=10)

    state_editor = Entry(editor)
    state_editor.grid(row=4, column=1, padx=10, pady=10)

    zipcode_editor = Entry(editor)
    zipcode_editor.grid(row=5, column=1, padx=10, pady=10)

    # Labels for text boxes
    Label(editor, text='Username').grid(row=0, column=0)
    Label(editor, text='Firstname').grid(row=1, column=0)
    Label(editor, text='Lastname').grid(row=2, column=0)
    Label(editor, text='Address').grid(row=3, column=0)
    Label(editor, text='City').grid(row=4, column=0)
    Label(editor, text='State').grid(row=4, column=0)
    Label(editor, text='Zipcode').grid(row=4, column=0)

    # Loop through records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    #Create a Update button
    Button(editor, text='Update', command=save).grid(row=5, columnspan=2)

    editor.mainloop()


# Create function to delete a record
def delete():
    # create a database or connect
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Create Submit function
def submit():

    # create a database or connect
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO ADDRESSES VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create a function for show records
def query():
    # create a database or connect
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    # Loop through records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1])+ '\t' + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()




# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1,padx=20,pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1,padx=20,pady=(10,0))
address = Entry(root, width=30)
address.grid(row=2, column=1,padx=20,pady=(10,0))
city = Entry(root, width=30)
city.grid(row=3, column=1,padx=20,pady=(10,0))
state = Entry(root, width=30)
state.grid(row=4, column=1,padx=20,pady=(10,0))
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1,padx=20,pady=(10,0))

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=(10,0))

# Create Labels
f_name_label = Label(root, text="First Name").grid(row=0, column=0)
l_name_label = Label(root, text="Last Name").grid(row=1, column=0)
address_label = Label(root, text="Address").grid(row=2, column=0)
city_label = Label(root, text="City").grid(row=3, column=0)
state_label = Label(root, text="State").grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode").grid(row=5, column=0)
delete_box_label = Label(root, text='Select ID').grid(row=9, column=0, pady=10)

# Create Submit Button
submit_btn = Button(root, text="Submit Data", command=submit).grid(row=6,column=0,columnspan=2,pady=10)

# Create a query button
query_btn = Button(root, text="Show Records", command =query)
query_btn.grid(row=7, column=0, columnspan=2,pady=(10,0))

# Create a delete button
delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2,pady=(10,0))

# Create a update button
edit_btn = Button(root, text='Edit', command=edit)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10)

# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()