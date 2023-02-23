
from tkinter import *
from tkinter import messagebox ,ttk
import sqlite3
from PIL import ImageTk,Image
from subprocess import call


import ast
# window= Tk()
# window.geometry('1250x1000')
# window.title("Learners")
# window.configure(bg='#E2C5ED')
# window.minsize(width=900,height=600)   
# window.maxsize(width=1600,height=1000)

pswdButtonClicked=0
confirmPswdButtonClicked=0



class Login:
    def __init__(self,window):
        self.window=window
        
        self.window.geometry('1250x1000')
        self.window.title("Learners")
        self.window.configure(bg='#E2C5ED')
        self.window.minsize(width=900,height=600)   
        self.window.maxsize(width=1600,height=1000)



# photo of log in page-----------------------------------------------
        self.imgpath = 'Rectangle 1.png'
        self.img = PhotoImage(file=self.imgpath)
        self.img = self.img.zoom(33) 
        self.img = self.img.subsample(32) 
        

        Label(window,image=self.img,bg='#E2C5ED').place(x=18,y=95)


# Main___Frame of log in page---------------------------------------------------------
        frame=Frame(self.window,width=320,height=390,bg='#F3EEE5')
        frame.place(x=835,y=195)


# label of log in page for learners title--------------------------------------------
        heading=Label(text="Learners",fg="black",bg='#E2C5ED',font=("Brush Script MT",128,'bold'))
        heading.place(x=500,y=-5)


        details=Label(frame,text="Your Hub for learning",font=("Calibiri",23,"bold"),bg='#F3EEE5',fg="black")
        details.place(x=29,y=26)

# UserName of log in page----------------------------------------------------                                       
        username=Label(frame,text="Username",font=('Inter Normal',16),bg='#F3EEE5',fg="black")
        username.place(x=25,y=80)
        self.username_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0,fg='black')
        self.username_1.place(x=30,y=120)






# username_______icon------------------------------------------------------
        self.imgpath_1 = 'user (2).png'
        self.Username_image = PhotoImage(file=self.imgpath_1)
        

        Label(window,image=self.Username_image,bg='#F3EEE5').place(x=945,y=275)

# Password of log in page---------------------------------------------------

        password=Label(frame,text="Password",font=("Inter Normal",16),bg='#F3EEE5',fg="black")
        password.place(x=25,y=160)
        password_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0,fg='black',show='*')
        password_1.place(x=30,y=199)

        # labels of don't have an account in log in page frame-----------------------------------------------
        label=Label(frame,text="Don't have an account?",fg='black',bg='#F3EEE5',font=('Inter Normal',14),   padx=20,pady=20)
        label.place(x=40,y=280)


        # password____icon-------------------------------------------------
        self.imgpath_2 = 'ABC.png'
        self.password_image = PhotoImage(file=self.imgpath_2)
        self.password_image = self.password_image.zoom(30) 
        self.password_image = self.password_image.subsample(32) 
        

        Label(window,image=self.password_image,bg='#F3EEE5').place(x=952,y=356)

        # eye icon-----------------------------------------------------------------------
        show_image=PhotoImage(file='view.png')
        show=Button(frame,image=show_image,bg="#F3EEE5",bd=0)
        show.place(x=289,y=199)

        # def login_function(self):
        #     if self.username_1.get()=="" or self.username_1.get()=="":
        #         messagebox.showerror("Error","Fill the both fields",parent=self.window)
        #     elif self.username_1.get()!="r" or self.username_1.get()!="1":
        #         messagebox.showerror("Invalid username",parent=self.window)
        #     else:
        #         messagebox.showinfo("Welcome",f"Welcome {self.username_1.get()}\nYour Password: {self.username_1.get()}",parent=self.window)


        errorLabel = Label(frame,text='',font=(8),fg='red')
        errorLabel.grid(row =4,column =0,padx=10,sticky='W')
        errorLabel.place(x=33,y=224)


        errorLabel1 = Label(frame,text='',font=(8),fg='red')
        errorLabel1.grid(row =4,column =0,padx=10,sticky='W')
        errorLabel1.place(x=33,y=224)

        

  
# next window for signup/register page--------------------------------------------------------
        def signup():

                    



            window=Toplevel()
            window.title("Sign Up")
            window.maxsize(width=1290,height=1000)
            window.minsize(width=900,height=600)
            window.config(bg='#F3EEE5')
            window.focus_force()
            window.grab_set()

            
             # frame for register--------------------------------------------------------------------------
            frame_2=Frame(window,width=500,height=583,bg='#E2C5ED')
            frame_2.place(x=80,y=68)

    
    # # labels of register page frame--------------------------------------------------------------
            text=Label(frame_2,text="CREATE YOUR ACCOUNT",fg='#4F1D63',bg='#E2C5ED',font=('Calibri',29,'bold'))
            text.place(x=40,y=35)

            

    # labels and entry box for first name---------------------------------------------------------
            def on_enter_1(e):
                x=user_1.get()
                if x=='     First Name':
                    user_1.delete(0,'end')
            def on_leave_1(e):
                if user_1.get()=='':
                    user_1.insert(0,'     First Name')

            user_1=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_1.place(x=65,y=110)
            user_1.insert(0,'     First Name')
            user_1.bind("<FocusIn>",on_enter_1)
            user_1.bind("<FocusOut>",on_leave_1)


#     # labels and entry box for last name--------------------------------------------------
            def on_enter_1(e):
                x=user_2.get()
                if x=='     Last Name':
                    user_2.delete(0,'end')
            def on_leave_1(e):
                if user_2.get()=='':
                    user_2.insert(0,'     Last Name')

            user_2=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_2.place(x=65,y=155)
            user_2.insert(0,'     Last Name')
            user_2.bind("<FocusIn>",on_enter_1)
            user_2.bind("<FocusOut>",on_leave_1)


# #     #gender--------------------------------------------------------
            gender=Label(frame_2,text="Gender",fg='black',bg='#E2C5ED',font=('Inter Normal',15))
            gender.place(x=75,y=200)

            gender = ['Male','Female','Others']
            gender_var = StringVar()
            gender_var.set('none')

            gender_male_button=Radiobutton(window,text="Male",bg='#E2C5ED',fg='Black',font=('Arial',14), variable=gender_var, value="Male")
            gender_male_button.place(x=230,y=265)

            gender_female_button=Radiobutton(window,text="Female",bg='#E2C5ED',fg='Black',font=('Arial',14), variable=gender_var, value="Female")
            gender_female_button.place(x=299,y=265)

            gender_other_button=Radiobutton(window,text="Others",bg='#E2C5ED',fg='Black',font=('Arial',14), variable=gender_var, value="Others")
            gender_other_button.place(x=389,y=265)

        
    

    # labels and entry box for date of birth---------------------------------
            def on_enter_1(e):
                user_3.delete(0,'end')
            def on_leave_1(e):
                if user_3.get()=='':
                    user_3.insert(0,' Year')

            user_3=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
            user_3.place(x=85,y=276)
            user_3.insert(0,' Year')
            user_3.bind("<FocusIn>",on_enter_1)
            user_3.bind("<FocusOut>",on_leave_1)
    
            dob=Label(frame_2,text="Date of Birth",font=('Inter Normal',15),bg='#E2C5ED',fg="black")
            dob.place(x=75,y=237)

            DOBimage=PhotoImage(file='DOB.png')
            DOBimage= DOBimage.zoom(15) #with 250, I ended up running out of memory
            DOBimage = DOBimage.subsample(20)
            imageofdob=Label(window,image=DOBimage,bg='#E2C5ED')
            imageofdob.place(x=271,y=306)
    
            def on_enter_1(e):
                user_4.delete(0,'end')
            def on_leave_1(e):
                if user_4.get()=='':
                    user_4.insert(0,' Month')

            user_4=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=6)
            user_4.place(x=160,y=276)
            user_4.insert(0,' Month')
            user_4.bind("<FocusIn>",on_enter_1)
            user_4.bind("<FocusOut>",on_leave_1)

            def on_enter_1(e):
                user_5.delete(0,'end')
            def on_leave_1(e):
                if user_5.get()=='':
                    user_5.insert(0,' Date')

            user_5=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
            user_5.place(x=238,y=276)
            user_5.insert(0,' Date')
            user_5.bind("<FocusIn>",on_enter_1)
            user_5.bind("<FocusOut>",on_leave_1)
    
#     #labels and entry box for user name---------------------------------
            def on_enter_1(e):
                x=user_6.get()
                if x=='     Username':
                    user_6.delete(0,'end')
        
            def on_leave_1(e):
                if user_6.get()=='':
                    user_6.insert(0,'     Username')

            user_6=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_6.place(x=65,y=360)
            user_6.insert(0,'     Username')
            user_6.bind("<FocusIn>",on_enter_1)
            user_6.bind("<FocusOut>",on_leave_1)
    
            # userimage=PhotoImage(file='Group.png')
            # userimage= userimage.zoom(16) #with 250, I ended up running out of memory
            # userimage = userimage.subsample(20)
            # imageofuser=Label(window,image=userimage,bg='white')
            # imageofuser.place(x=150,y=432)


#     # labels and entry box for Type(student,teacher)--------------------------------------
            hi=Label(frame_2,text="Type",width=15,bg="#E2C5ED",font=("Inter Normal",16),fg='black')
            hi.place(x=10,y=316)
            user7_var=StringVar(value='  Select your type')
            user7_combobox=ttk.Combobox(frame_2,values=['Teacher','Student'],font=('Inter Normal',15),width=15, textvariable=user7_var)
            user7_combobox.place(x=148,y=316)
    
#     # labels and entry box for new password----------------------------------------------------
            def on_enter_1(e):

                if user_7.get()=='     New Password':
                    user_7.delete(0,'end')
                user_7.config(show='*')
            def on_leave_1(e):
                if user_7.get()=='':
                    user_7.insert(0,'     New Password')
                    user_7.config(show='')
            user_7EntryVar =StringVar()
            user_7=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29,textvariable=user_7EntryVar)
            user_7.place(x=65,y=404)
            user_7.insert(0,'     New Password')
            user_7.bind("<FocusIn>",on_enter_1)
            user_7.bind("<FocusOut>",on_leave_1)
    
#     # labels and entry box for confirm password--------------------------------------------
            def on_enter_1(e):
                x=user_8.get()
                if x=='     Confirm Password':
                    user_8.delete(0,'end')
                user_8.config(show='*')
            def on_leave_1(e):
                if user_8.get()=='':
                    user_8.insert(0,'     Confirm Password')
                    user_8.config(show ='')


            user_8=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_8.place(x=65,y=449)

            def showPswd():
                global pswdButtonClicked
                pswdButtonClicked += 1
                if pswdButtonClicked%2 !=0:
                    passwordHideButton.config(text='H')
                    user_7.config(show='')
                elif pswdButtonClicked%2 ==0:
                    passwordHideButton.config(text='S')
                    user_7.config(show='*')

            def showConfirmPswd():
                global confirmPswdButtonClicked
                confirmPswdButtonClicked += 1
                if confirmPswdButtonClicked % 2 != 0:
                    confirmPasswordHideButton.config(text='H')
                    user_8.config(show='')
                elif confirmPswdButtonClicked % 2 == 0:
                    confirmPasswordHideButton.config(text='S')
                    user_8.config(show='*')

            passwordHideButton= Button(frame_2,text='S',command=showPswd)
            passwordHideButton.place(x=375,y=404)
            confirmPasswordHideButton= Button(frame_2,text='S',command=showConfirmPswd)
            confirmPasswordHideButton.place(x=375,y=449)
            user_8.insert(0,'     Confirm Password')
            user_8.bind("<FocusIn>",on_enter_1)
            user_8.bind("<FocusOut>",on_leave_1)


            def signup_function():
                if user_1.get() == '     First Name'  or user_2.get() == '     Last Name' or user_3.get() == ' Year' or user_4.get() == ' Month' or user_5.get() == ' Day' or user_6.get() == '     Username' or user7_var.get() == '     New Password' or user_8.get() == '     Confrim Passsword':
                    messagebox.showerror('Error', 'All fields are required')
                    print('inside if ')
                    return

                elif len(user_7.get()) < 7:
                    messagebox.showerror("Error", "Password should contain at least 6 character", parent=window)
                    return
                elif user_7.get() != user_8.get():
                    messagebox.showerror("Error", "password and confirm password entry did not match", parent=window)
                    return
                elif user_7.get() == user_8.get():
                    # messagebox.showinfo("Welcome", f"Welcome {user_6.get()}\nYour Password: {user_7.get()}", parent=window)
                    conn = sqlite3.connect('learners.db')
                    c = conn.cursor()
                        # Create table
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
                    print("Table created successfully")


                    # Extract the values entered by the user
                    first_name = user_1.get()
                    last_name = user_2.get()
                    gender = gender_var.get()
                    dob=str(user_3.get())+'-'+str(user_4.get())+'-'+str(user_5.get())
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
                    print(query)

                    try:
                        c.execute(query)
                        conn.commit()
                        print("Data added successfully")
                    except Exception as e:
                        print(f"Error:{str(e)}")
                        conn.rollback()
                    c.close()
                    conn.close()
                    window.destroy()


                    # Show a success message
                    messagebox.showinfo("Success", "Data inserted successfully")

                    # to view the database
                    def query():
                        # create a databases or connect to one
                        conn = sqlite3.connect('learners.db')

                        # create cursor
                        c = conn.cursor()

                        # query of the database
                        c.execute("SELECT *, oid FROM college_system")

                        records = c.fetchall()
                        print(records)

                        # loop through the results
                        print_record = ''
                        for record in records:
                            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(
                                record[8]) + '\n'

                        conn.commit()
                        conn.close()


                        # create query button
                        query_btn = Button(window, text='Show Records', command=query)
                        query_btn.grid(row=11, column=2, columnspan=2, pady=10, padx=10, ipadx=100)

            button_register=Button(frame_2,pady=3,width=8,height=-9,border=0,text="Register",bg="#39339B",fg="White",font=("Inter Normal",16),command=signup_function)
            button_register.place(x=180,y=495)

            self.image_2 = PhotoImage(file='Rectangle 6.png')
            self.image_2 = self.image_2.zoom(30)
            self.image_2 = self.image_2.subsample(32)
            self.why = Label(window, image=self.image_2, bg="#F3EEE5")
            self.why.place(x=720, y=115)


        # def runOtherFile():

        def login_authentication():
                conn= sqlite3.connect("learners.db")
                c = conn.cursor

                if self.username_1.get() == '' and password_1.get() == '':
                    errorLabel.config(text='Username and Password is empty!', bg="#F3EEE5", fg='Red',
                                      font=('calibri', 13))
                    return
                elif self.username_1.get() == '':
                    errorLabel.config(text='Username is empty')
                    return
                elif password_1.get() == '':
                    errorLabel.config(text='Password is empty')
                    return
                else:
                    conn = sqlite3.connect('learners.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM college_system where username=? and password=?",
                              (self.username_1.get(), password_1.get()))
                    record = c.fetchone()

                    if record is None:
                        messagebox.showerror('Error', 'invalid username or password')
                    else:
                        global currentUser
                        currentUser =self.username_1.get()
                        print(currentUser)

                        loginWindow.destroy()
                        call(["python3", "HomeWindow.py"])
                        #home page will be created if record exists

                    conn.commit()
                    conn.close()

                
        


        

    
    
        log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=login_authentication)
        
        
        log_in.place(x=103,y=252)

        


        sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
        sign_in.place(x=115,y=323)

if __name__=='__main__' :
    loginWindow=Tk()
    obj=Login(loginWindow)
    loginWindow=mainloop()
        
    

    # def login_function(self):
    #     if self.username_1.get()=="" or self.username_1.get()=="":
    #         messagebox.showerror("Error","Fill the both fields",parent=self.window)
    #     elif self.username_1.get()!="r" or self.username_1.get()!="1":
    #         messagebox.showerror("Invalid username",parent=self.window)
    #     else:
    #         messagebox.showinfo("Welcome",f"Welcome {self.username_1.get()}\nYour Password: {self.username_1.get()}",parent=self.window)










    
    
    