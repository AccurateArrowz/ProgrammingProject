from tkinter import *
import sqlite3

root = Tk()
root.geometry('600x600')
root.title("Update CRUD")

label1 = Label(root, text="SHOW DATA")
label1.grid(row=0, column=1)

# Add labels and entry widgets to update record
record_id_label = Label(root, width=30, text="Record ID:")
record_id_label.grid(row=1, column=0)

record_id_entry = Entry(root, width=30)
record_id_entry.grid(row=1, column=1)

first_name_label = Label(root, text="First Name:")
first_name_label.grid(row=2, column=0)

first_name_entry = Entry(root, width=30)
first_name_entry.grid(row=2, column=1)

last_name_label = Label(root, text="Last Name:")
last_name_label.grid(row=3, column=0)

last_name_entry = Entry(root, width=30)
last_name_entry.grid(row=3, column=1)

gender_label = Label(root, text="Gender:")
gender_label.grid(row=4, column=0)

gender_entry = Entry(root, width=30)
gender_entry.grid(row=4, column=1)

dob_label = Label(root, text="Date of Birth: 'YYYY-MM-DD' ")
dob_label.grid(row=5, column=0)

dob_Entry = Entry(root, width=30)
dob_Entry.grid(row=5, column=1)

user_type_label = Label(root, text="User Type:")
user_type_label.grid(row=6, column=0)

user_type_entry = Entry(root, width=30)
user_type_entry.grid(row=6, column=1)

username_label = Label(root, text="username:")
username_label.grid(row=7, column=0)

username_Entry = Entry(root, width=30)
username_Entry.grid(row=7, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=8, column=0)

password_Entry = Entry(root, width=30)
password_Entry.grid(row=8, column=1)

confirm_password_label = Label(root, text="Confirm_Password:")
confirm_password_label.grid(row=9, column=0)

confirm_password_Entry = Entry(root, width=30,)
confirm_password_Entry.grid(row=9, column=1)

def show_data():

    # create a connection to the database
    conn = sqlite3.connect('love.db')

    # create a cursor object to execute SQL commands
    c = conn.cursor()

    record_id = record_id_entry.get()

    c.execute("SELECT * from maya WHERE id=?", (record_id,))
    data = c.fetchone()
    conn.close()

    # Populate entry fields with data
    if data:
        record_id_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        gender_entry.delete(0, END)
        dob_Entry.delete(0, END)
        user_type_entry.delete(0, END)
        username_Entry.delete(0, END)
        password_Entry.delete(0, END)
        confirm_password_Entry.delete(0, END)

        record_id_entry.insert(0, data[0])
        first_name_entry.insert(0, data[1])
        last_name_entry.insert(0, data[2])
        gender_entry.insert(0, data[3])
        dob_Entry.insert(0, data[4])
        username_Entry.insert(0, data[5])
        user_type_entry.insert(0, data[6])
        password_Entry.insert(0, data[7])
        confirm_password_Entry.insert(0, data[8])

show_data()
# Add a button to trigger the data retrieval and entry field population
show_data_button = Button(root, text="Show Data", command=show_data)
show_data_button.grid(row=10, column=1)

root.mainloop()






