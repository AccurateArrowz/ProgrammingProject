from tkinter import *
import sqlite3
from tkinter import messagebox
# import registrations
root=Tk()

root.title("login")
root.geometry('500x400')
label = Label(root, text="Login Form", font=("bold", 10))
label.grid(row=0, column=3)
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showinfo('Error', 'Please fill all fields.')
    else:
        try:
            conn = sqlite3.connect('user_detail.db')
            c = conn.cursor()
        except:
            messagebox.showerror('Error', 'connection is not established try again')
            return

        c.execute("SELECT * FROM users_details where username=? and password=?", (usernameEntry.get(), passwordEntry.get()))
        record = c.fetchone()
        if record is None:
            messagebox.showerror('Error', 'invalid username or password')
        else:
            messagebox.showinfo('Success', 'login is successful')

        conn.commit()
        conn.close()

#Adding label
username_label = Label(root, text="Username:")
username_label.grid(row=3, column=2)

password_label = Label(root, text="Password:")
password_label.grid(row=4, column=2)

# Adding textbox
usernameEntry = Entry(root)
usernameEntry.grid(row=3, column=3)

passwordEntry = Entry(root, show='*')
passwordEntry.grid(row=4, column=3)

# Adding login button
button = Button(root, text="Login", command=login)
button.grid(row=6, column=3)
root.mainloop()