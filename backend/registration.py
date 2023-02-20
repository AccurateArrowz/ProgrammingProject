
from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime

root = Tk()
root.title("College management registration")
root.geometry('600x600')

label0 = Label(root, text="Registration Form", font=("bold",20))
label0.grid(row=0, column=3)

conn = sqlite3.connect('user_detail.db')

c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS users_details(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        date_of_birth INTEGER NOT NULL,
        username TEXT NOT NULL,
        user_type TEXT NOT NULL,
        password TEXT NOT NULL,
        confirm_password TEXT NOT NULL
        )""")
print("Table created successfully")

conn.commit()
conn.close()

# creating entry box
first_name = Entry(root, width=30)
first_name.grid(row=2, column=3)

last_name = Entry(root, width=30)
last_name.grid(row=3, column=3)

gender = ['Male', 'Female', 'Others']
gender_var = StringVar()
gender_var.set('none')
gender_male_button = Radiobutton(root, text="Male", padx=5, variable=gender_var, value="Male")
gender_male_button.grid(row=4, column=3)
gender_female_button = Radiobutton(root, text="Female", padx=20, variable=gender_var, value="Female")
gender_female_button.grid(row=4, column=4)
gender_other_button = Radiobutton(root, text="Others", variable=gender_var, value="Others")
gender_other_button.grid(row=4, column=5)

dob = Entry(root, width=30)
dob.grid(row=5, column=3)

def validate_dob(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except ValueError:
        return False

clicked = StringVar()
clicked.set('Select your type')
droplist = OptionMenu(root, clicked, "Student", "Teacher")
droplist.grid(row=6, column=3)

username = Entry(root, width=30)
username.grid(row=7, column=3)

password = Entry(root, width=30, show="*")
password.grid(row=8, column=3)

confirm_password = Entry(root, width=30, show="*")
confirm_password.grid(row=9, column=3)

# Adding textboxes label
first_name_label = Label(root, text="First Name:")
first_name_label.grid(row=2, column=2)

last_name_label = Label(root, text="Last Name:")
last_name_label.grid(row=3, column=2)

gender_label = Label(root, text="Gender:")
gender_label.grid(row=4, column=2)

dob_label = Label(root, text="Date of Birth: 'YYYY-MM-DD' ")
dob_label.grid(row=5, column=2)

user_type_label = Label(root, text="User Type:")
user_type_label.grid(row=6, column=2)

username_label = Label(root, text="username:")
username_label.grid(row=7, column=2)

password_label = Label(root, text="Password:")
password_label.grid(row=8, column=2)

confirm_password_label = Label(root, text="Confirm_Password:")
confirm_password_label.grid(row=9, column=2)


def insert_data():
    # Extract the values entered by the user
    first_name_value = first_name.get()
    last_name_value = last_name.get()
    gender_value = gender_var.get()
    dob_value = dob.get()
    user_type_value = clicked.get()
    username_value = username.get()
    password_value = password.get()
    confirm_password_value = confirm_password.get()

    # Validate the date of birth
    if not validate_dob(dob_value):
        messagebox.showerror("Error", "Invalid date of birth")
        return

    # Check if the password and confirm password fields match
    if password_value != confirm_password_value:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Store the values in a dictionary
    data = {
        "first_name": first_name_value,
        "last_name": last_name_value,
        "gender": gender_value,
        "date_of_birth": dob_value,
        "user_type": user_type_value,
        "username": username_value,
        "password": password_value,
        "confirm_password": confirm_password_value
    }

# Clear entry widgets

    first_name.delete(0, END)
    last_name.delete(0, END)
    gender_var.set('none')
    dob.delete(0, END)
    clicked.set('Select Your Type')
    username.delete(0, END)
    password.delete(0, END)
    confirm_password.delete(0, END)


    # Insert the data into the database
    conn = sqlite3.connect('user_detail.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO users_details (first_name, last_name, gender, date_of_birth, user_type, username, password, confirm_password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (data["first_name"], data["last_name"], data["gender"], data["date_of_birth"], data["user_type"],
         data["username"], data["password"], data["confirm_password"]))
    conn.commit()
    conn.close()

    # Show a success message
    messagebox.showinfo("Success", "Data inserted successfully")

submit_button = Button(root, text="Submit", command=insert_data)
submit_button.grid(row=10, column=3)

# to view the database
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
query_btn.grid(row=11, column=2, columnspan=2, pady=10, padx=10, ipadx=100)
root.mainloop()