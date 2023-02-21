from tkinter import *
import sqlite3
from tkinter import messagebox
import datetime

root = Tk()
root.geometry('600x600')
# Create a function to retrieve data from the database and display it in the frontend
def display_data(user_id):
    # Connect to the database
    conn = sqlite3.connect('user_detail.db')
    # Create a cursor object to execute SQL commands
    c = conn.cursor()
    # Execute a SELECT statement to retrieve data from the database for the specified user ID
    c.execute('SELECT * FROM users_details WHERE id=?', (user_id,))
    # Fetch the row returned by the SELECT statement
    row = c.fetchone()
    # Create a listbox to display the data
    listbox = Listbox(root)
    # Insert the row into the listbox
    listbox.insert(END, row)
    # Pack the listbox into the Tkinter window
    listbox.pack()

# Call the function to display the data for user with ID 1 when the Tkinter window is opened
display_data(1)

# Run the Tkinter event loop
root.mainloop()


def query():
    # create a databases or connect to one
    conn = sqlite3.connect('user_detail.db')

    # create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM users_details")

    records = c.fetchall()
    print(records)

    # loop through the results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[8]) + '\n'

    query_label = Label(root, text=print_record)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()
    conn.close()

root = Tk()
root.title("Update Record")
root.geometry("600x600")

# Create connection to database
conn = sqlite3.connect("user_detail.db")
c = conn.cursor()

# Function to update record
def update_record():
    # Get values from entry widgets
    record_id = record_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_var.get()
    dob = dob_Entry.get()
    user_type = clicked.get()
    username = username_Entry.get()
    password = password_Entry.get()
    confirm_password = confirm_password_Entry.get()

    # Update record in database
    c.execute("UPDATE users_details SET first_name=?, last_name=?, gender=?, date_of_birth=?, user_type=?, username=?, password=?, confirm_password=? WHERE id=?",
        (first_name, last_name, gender, dob, user_type, username, password, confirm_password, record_id))
    conn.commit()
    # Clear entry widgets
    record_id_entry.delete(0, END)
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    gender_var.set('none')
    dob_Entry.delete(0, END)
    clicked.set('')
    username_Entry.delete(0, END)
    password_Entry.delete(0, END)
    confirm_password_Entry.delete(0, END)

    # Show message box
    messagebox.showinfo("Success", "Record updated successfully.")

# Add labels and entry widgets to update record
record_id_label = Label(root, text="Record ID:")
record_id_label.grid(row=0, column=0)

record_id_entry = Entry(root)
record_id_entry.grid(row=0, column=1)

first_name_label = Label(root, text="First Name:")
first_name_label.grid(row=1, column=0)

first_name_entry = Entry(root)
first_name_entry.grid(row=1, column=1)

last_name_label = Label(root, text="Last Name:")
last_name_label.grid(row=2, column=0)

last_name_entry = Entry(root)
last_name_entry.grid(row=2, column=1)

gender_label = Label(root, text="Gender:")
gender_label.grid(row=3, column=0)

gender = ['Male', 'Female', 'Others']
gender_var = StringVar()
gender_var.set('none')
gender_male_button = Radiobutton(root, text="Male", padx=5, variable=gender_var, value="Male")
gender_male_button.grid(row=3, column=1)
gender_female_button = Radiobutton(root, text="Female", padx=20, variable=gender_var, value="Female")
gender_female_button.grid(row=3, column=2)
gender_other_button = Radiobutton(root, text="Others", variable=gender_var, value="Others")
gender_other_button.grid(row=3, column=3)

dob_label = Label(root, text="Date of Birth: 'YYYY-MM-DD' ")
dob_label.grid(row=4, column=0)

dob_Entry = Entry(root, width=30)
dob_Entry.grid(row=4, column=1)

def validate_dob(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except ValueError:
        return False

user_type_label = Label(root, text="User Type:")
user_type_label.grid(row=5, column=0)

clicked = StringVar()
clicked.set('Select your type')
droplist = OptionMenu(root, clicked, "Student", "Teacher")
droplist.grid(row=5, column=1)

username_label = Label(root, text="username:")
username_label.grid(row=6, column=0)

username_Entry = Entry(root, width=30)
username_Entry.grid(row=6, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=7, column=0)

password_Entry = Entry(root, width=30, show="*")
password_Entry.grid(row=7, column=1)

confirm_password_label = Label(root, text="Confirm_Password:")
confirm_password_label.grid(row=8, column=0)

confirm_password_Entry = Entry(root, width=30, show="*")
confirm_password_Entry.grid(row=8, column=1)


# Add button to update record
update_button = Button(root, text="Update Record", command=update_record)
update_button.grid(row=9, column=0, columnspan=2, pady=10)

def query():
    # create a databases or connect to one
    conn = sqlite3.connect('user_detail.db')

    # create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM users_details")

    records = c.fetchall()
    print(records)

    # loop through the results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[8]) + '\n'

    query_label = Label(root, text=print_record)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()
    conn.close()

# create query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()