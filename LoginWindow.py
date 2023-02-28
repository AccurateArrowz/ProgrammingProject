from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from PIL import ImageTk, Image
from subprocess import call



pswdButtonClicked = 0
confirmPswdButtonClicked = 0
loginEyeClicked = 0


loginWindow = Tk()
loginWindow.geometry('1920x1200')
loginWindow.title("Learners")
loginWindow.configure(bg='#E2C5ED')
loginWindow.minsize(width=900, height=600)
loginWindow.maxsize(width=1600, height=1000)

def showLoginPswd():
    global loginEyeClicked
    loginEyeClicked+=1
    if loginEyeClicked%2 != 0:
        passwordEntry.config(show='')
    elif loginEyeClicked%2 == 0:
        passwordEntry.config(show="*")

def signup():

    signUpWindow = Toplevel()
    signUpWindow.title("Sign Up")
    signUpWindow.geometry('1920x1200')
    signUpWindow.config(bg='#F3EEE5')
    signUpWindow.focus_force()
    signUpWindow.grab_set()

    # Frame for register--------------------------------------------------------------------------
    registerFrame = Frame(signUpWindow, width=500, height=583, bg='#E2C5ED')
    registerFrame.place(x=80, y=68)

    # # labels of register page frame--------------------------------------------------------------
    text = Label(registerFrame, text="CREATE YOUR ACCOUNT", fg='#4F1D63', bg='#E2C5ED', font=('Calibri', 29, 'bold'))
    text.place(x=40, y=35)

    # labels and entry box for first name---------------------------------------------------------
    def on_enter_1(e):
        x = user_1.get()
        if x == '     First Name':
            user_1.delete(0, 'end')

    def on_leave_1(e):
        if user_1.get() == '':
            user_1.insert(0, '     First Name')

    user_1 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 16), width=29)
    user_1.place(x=65, y=110)
    user_1.insert(0, '     First Name')
    user_1.bind("<FocusIn>", on_enter_1)
    user_1.bind("<FocusOut>", on_leave_1)

    #     # labels and entry box for last name--------------------------------------------------
    def on_enter_1(e):
        x = user_2.get()
        if x == '     Last Name':
            user_2.delete(0, 'end')

    def on_leave_1(e):
        if user_2.get() == '':
            user_2.insert(0, '     Last Name')

    user_2 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 16), width=29)
    user_2.place(x=65, y=155)
    user_2.insert(0, '     Last Name')
    user_2.bind("<FocusIn>", on_enter_1)
    user_2.bind("<FocusOut>", on_leave_1)

    # #     #gender--------------------------------------------------------
    gender = Label(registerFrame, text="Gender", fg='black', bg='#E2C5ED', font=('Inter Normal', 15))
    gender.place(x=75, y=200)

    gender = ['Male', 'Female', 'Others']
    gender_var = StringVar()
    gender_var.set('none')

    gender_male_button = Radiobutton(signUpWindow, text="Male", bg='#E2C5ED', fg='Black', font=('Arial', 14),
                                     variable=gender_var, value="Male")
    gender_male_button.place(x=230, y=265)

    gender_female_button = Radiobutton(signUpWindow, text="Female", bg='#E2C5ED', fg='Black', font=('Arial', 14),
                                       variable=gender_var, value="Female")
    gender_female_button.place(x=299, y=265)

    gender_other_button = Radiobutton(signUpWindow, text="Others", bg='#E2C5ED', fg='Black', font=('Arial', 14),
                                      variable=gender_var, value="Others")
    gender_other_button.place(x=389, y=265)

    # labels and entry box for date of birth---------------------------------
    def on_enter_1(e):
        user_3.delete(0, 'end')

    def on_leave_1(e):
        if user_3.get() == '':
            user_3.insert(0, ' Year')

    user_3 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 14), width=5)
    user_3.place(x=85, y=276)
    user_3.insert(0, ' Year')
    user_3.bind("<FocusIn>", on_enter_1)
    user_3.bind("<FocusOut>", on_leave_1)

    dob = Label(registerFrame, text="Date of Birth", font=('Inter Normal', 15), bg='#E2C5ED', fg="black")
    dob.place(x=75, y=237)

    DOBimage = PhotoImage(file='DOB.png')
    DOBimage = DOBimage.zoom(15)  # with 250, I ended up running out of memory
    DOBimage = DOBimage.subsample(20)
    imageofdob = Label(signUpWindow, image=DOBimage, bg='#E2C5ED')
    imageofdob.place(x=271, y=306)

    def on_enter_1(e):
        user_4.delete(0, 'end')

    def on_leave_1(e):
        if user_4.get() == '':
            user_4.insert(0, ' Month')

    user_4 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 14), width=6)
    user_4.place(x=160, y=276)
    user_4.insert(0, ' Month')
    user_4.bind("<FocusIn>", on_enter_1)
    user_4.bind("<FocusOut>", on_leave_1)

    def on_enter_1(e):
        user_5.delete(0, 'end')

    def on_leave_1(e):
        if user_5.get() == '':
            user_5.insert(0, ' Day')

    user_5 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 14), width=5)
    user_5.place(x=238, y=276)
    user_5.insert(0, ' Day')
    user_5.bind("<FocusIn>", on_enter_1)
    user_5.bind("<FocusOut>", on_leave_1)

    #     #labels and entry box for user name---------------------------------
    def on_enter_1(e):
        x = user_6.get()
        if x == '     Username':
            user_6.delete(0, 'end')

    def on_leave_1(e):
        if user_6.get() == '':
            user_6.insert(0, '     Username')

    user_6 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 16), width=29)
    user_6.place(x=65, y=360)
    user_6.insert(0, '     Username')
    user_6.bind("<FocusIn>", on_enter_1)
    user_6.bind("<FocusOut>", on_leave_1)

    # userimage=PhotoImage(file='Group.png')
    # userimage= userimage.zoom(16) #with 250, I ended up running out of memory
    # userimage = userimage.subsample(20)
    # imageofuser=Label(signUpWindow,image=userimage,bg='white')
    # imageofuser.place(x=150,y=432)

    #     # labels and entry box for Type(student,teacher)--------------------------------------
    hi = Label(registerFrame, text="Type", width=15, bg="#E2C5ED", font=("Inter Normal", 16), fg='black')
    hi.place(x=10, y=316)
    user7_var = StringVar(value='  Select your type')
    user7_combobox = ttk.Combobox(registerFrame, values=['Teacher', 'Student'], font=('Inter Normal', 15), width=15,
                                  textvariable=user7_var)
    user7_combobox.place(x=148, y=316)

    #     # labels and entry box for new password----------------------------------------------------
    def on_enter_1(e):

        if user_7.get() == '     New Password':
            user_7.delete(0, 'end')
        user_7.config(show='*')

    def on_leave_1(e):
        if user_7.get() == '':
            user_7.insert(0, '     New Password')
            user_7.config(show='')

    user_7EntryVar = StringVar()
    user_7 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 16), width=29,
                   textvariable=user_7EntryVar)
    user_7.place(x=65, y=404)
    user_7.insert(0, '     New Password')
    user_7.bind("<FocusIn>", on_enter_1)
    user_7.bind("<FocusOut>", on_leave_1)

    #     # labels and entry box for confirm password--------------------------------------------
    def on_enter_1(e):
        x = user_8.get()
        if x == '     Confirm Password':
            user_8.delete(0, 'end')
        user_8.config(show='*')

    def on_leave_1(e):
        if user_8.get() == '':
            user_8.insert(0, '     Confirm Password')
            user_8.config(show='')

    user_8 = Entry(registerFrame, fg='black', bg='white', font=('Inter Normal', 16), width=29)
    user_8.place(x=65, y=449)

    def showPswd():
        if user_7.get()=='     New Password':
            return
        global pswdButtonClicked
        pswdButtonClicked += 1
        if pswdButtonClicked % 2 != 0:
            passwordHideButton.config(text='H')
            user_7.config(show='')
        elif pswdButtonClicked % 2 == 0:
            passwordHideButton.config(text='S')
            user_7.config(show='*')

    def showConfirmPswd():
        if user_8.get()=='     Confirm Password':
            return
        global confirmPswdButtonClicked
        confirmPswdButtonClicked += 1
        if confirmPswdButtonClicked % 2 != 0:
            confirmPasswordHideButton.config(text='H')
            user_8.config(show='')
        elif confirmPswdButtonClicked % 2 == 0:
            confirmPasswordHideButton.config(text='S')
            user_8.config(show='*')

    passwordHideButton = Button(registerFrame, text='S', command=showPswd)
    passwordHideButton.place(x=375, y=404)
    confirmPasswordHideButton = Button(registerFrame, text='S', command=showConfirmPswd)
    confirmPasswordHideButton.place(x=375, y=449)
    user_8.insert(0, '     Confirm Password')
    user_8.bind("<FocusIn>", on_enter_1)
    user_8.bind("<FocusOut>", on_leave_1)

    def signup_function():
        if user_1.get() == '     First Name' or user_2.get() == '     Last Name' or user_3.get() == ' Year' or user_4.get() == ' Month' or user_5.get() == ' Day' or user_6.get() == '     Username' or user7_var.get() == '     New Password' or user_8.get() == '     Confrim Passsword':
            messagebox.showerror('Error', 'All fields are required')
            return
        elif user_1.get() == '' or user_2.get() == '' or user_3.get() == '' or user_4.get() == '' or user_5.get() == '' or user_6.get() == '' or user7_var.get() == '' or user_8.get() == '':
            messagebox.showerror('Error', 'All fields are required')
            return
        elif user_3.get().isdigit() ==False or user_4.get().isdigit() ==False or user_5.get().isdigit() ==False:
            messagebox.showerror('Error', 'Date of birth must be inserted in digits')
            return
        elif int(user_3.get())<1850 or int(user_4.get())>12 or int(user_5.get())>32:
            messagebox.showerror('Error', 'Your date of birth is invalid')
            return
        elif len(user_7.get()) < 7:
            messagebox.showerror("Error", "Password should contain at least 6 character", parent=signUpWindow)
            return
        elif user_7.get() != user_8.get():
            messagebox.showerror("Error", "password and confirm password entry did not match", parent=signUpWindow)
            return
        elif user_7.get() == user_8.get():
            conn = sqlite3.connect('learners.db')
            c = conn.cursor()
            c.execute("SELECT * FROM college_system where username=? ",
                          (usernameEntry.get(),))
            record = c.fetchone()

            if record is None: #i.e username is not taken already
                c.execute("""CREATE TABLE IF NOT EXISTS college_system(
                                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           first_name TEXT NOT NULL,
                                                           last_name TEXT NOT NULL,
                                                           gender TEXT NOT NULL,
                                                           date_of_birth INTEGER NOT NULL,
                                                           user_type TEXT NOT NULL,
                                                           username TEXT NOT NULL,
                                                           password TEXT NOT NULL,
                                                           confirm_password TEXT NOT NULL
                                                           )""")
                # Extract the values entered by the user
                first_name = user_1.get()
                last_name = user_2.get()
                gender = gender_var.get()
                dob = str(user_3.get()) + '-' + str(user_4.get()) + '-' + str(user_5.get())
                user_type = user7_var.get()
                username = user_6.get()
                password = user_7.get()
                confirm_password = user_8.get()

                # Store the values in a dictionary
                data = {
                    "first_name": first_name,
                    "lastname": last_name,
                    "gender": gender,
                    "date_of_birth": dob,
                    "user_type": user_type,
                    "username": username,
                    "password": password,
                    "confirm_password": confirm_password
                }

                query = f"INSERT INTO college_system (first_name, last_name, gender, date_of_birth, user_type, username, password, confirm_password) VALUES('{first_name}','{last_name}', '{gender}', '{dob}','{user_type}','{username}','{password}','{confirm_password}')"
                messagebox.showinfo("Success", "Data inserted successfully ✅")
                c.close()
                conn.close()
                signUpWindow.destroy()

                try:
                    c.execute(query)
                    conn.commit()
                    print("Data added successfully")
                except Exception as e:
                    print(f"Error:{str(e)}")
                    conn.rollback()
            else:
                username= user_6.get()
                print(f'username "{username}" is already taken')
                messagebox.showinfo("Success",f"Username '{username}' is already taken")



    button_register = Button(registerFrame, pady=3, width=8, height=-9, border=0, text="Register", bg="#39339B",fg='black',
                              font=("Inter Normal", 16,'bold'), command=signup_function)
    button_register.place(x=150, y=515)

    global image_2
    image_2 = PhotoImage(file='Rectangle 6.png')
    image_2 = image_2.zoom(30)
    image_2 = image_2.subsample(32)
    signUp_ideaImg = Label(signUpWindow, image=image_2, bg="#F3EEE5")
    signUp_ideaImg.place(x=720, y=115)

def login_authentication():
    if usernameEntry.get() == '' and passwordEntry.get() == '':
        errorLabel.config(text='Username and Password is empty!', bg="#F3EEE5", fg='Red',
                          font=('calibri', 13))
        return
    elif usernameEntry.get() == '':
        errorLabel.config(text='Username is empty')
        return
    elif passwordEntry.get() == '':
        errorLabel.config(text='Password is empty')
        return

    else:
        conn = sqlite3.connect('learners.db')
        c = conn.cursor()

        c.execute("SELECT * FROM college_system where username=? and password=?",
                  (usernameEntry.get(), passwordEntry.get()))
        record = c.fetchone()

        if record is None:
            messagebox.showerror('Error', 'invalid username or password')
        else:
            global currentUser
            currentUser =usernameEntry.get()
            print(currentUser)
            loginWindow.destroy()
            call(["python3", "HomeWindow.py"])

        conn.commit()
        conn.close()





# photo of log in page-----------------------------------------------
imgpath = 'Rectangle 1.png'
img = PhotoImage(file=imgpath)
img = img.zoom(33)
img = img.subsample(32)

girlImg = Label(loginWindow, image=img, bg='#E2C5ED')
girlImg.place(x=18, y=95)

heading = Label(text="Learners", fg="black", bg='#E2C5ED', font=("Brush Script MT", 128, 'bold'))
heading.place(x=500, y=-5)
#Login Frame---------------------------------------------------------
loginFrame = Frame(loginWindow, width=310, height=390, bg='#F3EEE5')
loginFrame.place(x=835, y=195)

details = Label(loginFrame, text="Your Hub for learning", font=("Calibiri", 23, "bold"), bg='#F3EEE5', fg="black")
details.place(x=29, y=26)

# UserName of log in page----------------------------------------------------
username = Label(loginFrame, text="Username", font=('Inter Normal', 16), bg='#F3EEE5', fg="black")
username.place(x=25, y=80)
usernameEntry = Entry(loginFrame, bg="White", width=21, font=('Inter Normal', 16), bd=0, fg='black')
usernameEntry.place(x=30, y=120)

# username_______icon------------------------------------------------------
imgpath_1 = 'user (2).png'
Username_image = PhotoImage(file=imgpath_1)

Label(loginWindow, image=Username_image, bg='#F3EEE5').place(x=945, y=275)

# Password of log in page---------------------------------------------------

password= Label(loginFrame, text="Password", font=("Inter Normal", 16), bg='#F3EEE5', fg="black")
password.place(x=25, y=160)
passwordEntry = Entry(loginFrame, bg="White", width=21, font=('Inter Normal', 16), bd=0, fg='black', show='*')
passwordEntry.place(x=30, y=199)

# labels of don't have an account in log in page loginFrame-----------------------------------------------
label = Label(loginFrame, text="Don't have an account?", fg='black', bg='#F3EEE5', font=('Inter Normal', 14),
              padx=20, pady=20)
label.place(x=40, y=280)

# password____icon-------------------------------------------------
imgpath_2 = 'ABC.png'
password_image = PhotoImage(file=imgpath_2)
password_image = password_image.zoom(30)
password_image = password_image.subsample(32)

Label(loginWindow, image=password_image, bg='#F3EEE5').place(x=952, y=356)


# eye icon-----------------------------------------------------------------------

eyeImg = PhotoImage(file='view.png')
showPswdButton = Button(loginFrame, image=eyeImg, bg="#F3EEE5", bd=0,command=showLoginPswd)
showPswdButton.place(x=260, y=199)


errorLabel = Label(loginFrame, text='', font=(8), fg='red',bg='#F3EEE5')
errorLabel.place(x=33, y=224)
loginButton = Button(loginFrame, width=9, pady=3, text="Log In", bg="#2586DA", fg="black", border=0,
                font=('Calibri', 13, 'bold'),command=login_authentication)#

loginButton.place(x=80, y=252)

signUpButton = Button(loginFrame, width=7,bg='#F3EEE5' ,text='Sign Up', border=0, fg="Blue",
                 font=("Calibri", 13, 'bold', UNDERLINE),command=signup )#
signUpButton.place(x=85, y=328)


loginWindow.mainloop()



