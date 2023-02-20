
from tkinter import *
from tkinter import messagebox ,ttk
import sqlite3
import datetime
from PIL import ImageTk,Image
import ast
# window= Tk()
# window.geometry('1250x1000')
# window.title("Learners")
# window.configure(bg='#E2C5ED')
# window.minsize(width=900,height=600)   
# window.maxsize(width=1600,height=1000)


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
        

        Label(window,image=self.img,bg='#E2C5ED').place(x=10,y=55)


# Main___Frame of log in page---------------------------------------------------------
        frame=Frame(self.window,width=320,height=390,bg='#F3EEE5')
        frame.place(x=835,y=195)


# label of log in page for learners title--------------------------------------------
        heading=Label(text="Learners",fg="red",bg='#E2C5ED',font=("Brush Script MT",76,'bold'))
        heading.place(x=500,y=-5)


        details=Label(frame,text="Your Hub for learning",font=("Calibiri",18,"bold"),bg='#F3EEE5',fg="black")
        details.place(x=29,y=26)

# UserName of log in page----------------------------------------------------                                       
        username=Label(frame,text="Username",font=('Inter Normal',14),bg='#F3EEE5',fg="black")
        username.place(x=25,y=80)
        self.username_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0)
        self.username_1.place(x=30,y=120)






# username_______icon------------------------------------------------------
        self.imgpath_1 = 'user (2).png'
        self.Username_image = PhotoImage(file=self.imgpath_1)
        

        Label(window,image=self.Username_image,bg='#F3EEE5').place(x=950,y=275)

# Password of log in page---------------------------------------------------

        password=Label(frame,text="Password",font=("Inter Normal",14),bg='#F3EEE5',fg="black")
        password.place(x=25,y=160)
        password_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0)
        password_1.place(x=30,y=199)

        # labels of don't have an account in log in page frame-----------------------------------------------
        label=Label(frame,text="Don't have an account?",fg='black',bg='#F3EEE5',font=('Inter Normal',14),   padx=20,pady=20)
        label.place(x=45,y=280)


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

            var=IntVar()
            ca=Checkbutton(window,text=("Male"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var)
            ca.place(x=230,y=265)
            var_1=IntVar
            ca_1=Checkbutton(window,text=("Female"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_1)
            ca_1.place(x=299,y=265)
            var_2=IntVar
            ca_2=Checkbutton(window,text=("Others"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_2)
            ca_2.place(x=389,y=265)

        
    

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


#     # labels and entry box for Type(student,teacher)--------------------------------------
            hi=Label(frame_2,text="Type",width=15,bg="#E2C5ED",font=("Inter Normal",16))
            hi.place(x=10,y=316)
            user7_var=StringVar(value='  Student')
            user7_combobox=ttk.Combobox(frame_2,values=['Teacher','Student'],font=('Inter Normal',15),width=8, textvariable=user7_var)
            user7_combobox.place(x=148,y=316)
    
#     # labels and entry box for new password----------------------------------------------------
            def on_enter_1(e):
                x=user_7.get()
                if x=='     New Password':
                    user_7.delete(0,'end')
            def on_leave_1(e):
                if user_7.get()=='':
                    user_7.insert(0,'     New Password')

            user_7=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_7.place(x=65,y=404)
            user_7.insert(0,'     New Password')
            user_7.bind("<FocusIn>",on_enter_1)
            user_7.bind("<FocusOut>",on_leave_1)
    
#     # labels and entry box for confirm password--------------------------------------------
            def on_enter_1(e):
                x=user_8.get()
                if x=='     Confirm Password':
                    user_8.delete(0,'end')
            def on_leave_1(e):
                if user_8.get()=='':
                    user_8.insert(0,'     Confirm Password')

            user_8=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
            user_8.place(x=65,y=449)
            user_8.insert(0,'     Confirm Password')
            user_8.bind("<FocusIn>",on_enter_1)
            user_8.bind("<FocusOut>",on_leave_1)





            def signup_function():
                if (user_7.get()=='') or (user_8.get()==''):

                    messagebox.showerror("Error","This field is required",parent=window)
                
                elif len(user_7.get())<6 or len(user_7.get())<6:
                    messagebox.showerror("Error","Password should contain at least 6 character",parent=window)
                else:
                    messagebox.showinfo("Welcome",f"Welcome {user_7.get()}\nYour Password: {user_7.get()}",parent=window)

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


                    def insert_data():
                        # Extract the values entered by the user
                        first_name_value = user_1.get()
                        last_name_value = user_2.get()
                        gender_value = var.get()
                        year = user_3.get()
                        month = user_4.get()
                        date = user_5.get()
                        user_type_value = user7_var.get()
                        username_value = user_7.get()
                        password_value = user_8.get()
                        confirm_password_value = user_8.get()

                        # Store the values in a dictionary
                        data = {
                            "first_name": first_name_value,
                            "last_name": last_name_value,
                            "gender": gender_value,
                            "date_of_birth": [year,month, date],
                            "user_type": user_type_value,
                            "username": username_value,
                            "password": password_value,
                            "confirm_password": confirm_password_value
                        }

                        c.execute(
                            "INSERT INTO users_details (first_name, last_name, gender, date_of_birth, user_type, username, password, confirm_password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (data["first_name"], data["last_name"], data["gender"], data["date_of_birth"],
                             data["user_type"],
                             data["username"], data["password"], data["confirm_password"]))
                        conn.commit()
                        conn.close()

                        # Show a success message
                        messagebox.showinfo("Success", "Data inserted successfully")

                        submit_button = Button(frame_2, text="Submit", command=insert_data)
                        submit_button.grid(row=10, column=3)

                        # to view the database
                        def query():
                            # create a databases or connect to one
                            conn = sqlite3.connect('user_detail.db')

                            # create cursor
                            c = conn.cursor()

                            # query of the database
                            c.execute("SELECT *, oid FROM user_details")

                            records = c.fetchall()
                            print(records)

                            # loop through the results
                            print_record = ''
                            for record in records:
                                print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(
                                    record[8]) + '\n'

                            query_label = Label(window, text=print_record)
                            query_label.grid(row=13, column=0, columnspan=2)

                            conn.commit()
                            conn.close()

                        # create query button
                        query_btn = Button(window, text='Show Records', command=query)
                        query_btn.grid(row=11, column=2, columnspan=2, pady=10, padx=10, ipadx=100)


            button_register=Button(frame_2,pady=3,width=8,height=-9,border=0,text="Register",bg="#39339B",fg="White",font=("Inter Normal",16),command=signup_function)
            button_register.place(x=180,y=495)
        

# # window of main home page/dashboard-------------------------------------------------
        def home_page():
                import sqlite3

                from tkinter import messagebox


                if self.username_1.get()=='' and password_1.get()=='':
                    errorLabel.config(text='Username and Password is empty!',bg="#F3EEE5",fg='Red',font=('calibri',13))
                    return
                elif self.username_1.get()=='':
                    errorLabel.config(text='Username is empty')
                    return
                elif password_1.get()=='':
                    errorLabel.config(text='Password is empty')
                    return
                else:
                    conn = sqlite3.connect('user_detail.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM users_details where username=? and password=?",
                              (self.username_1.get(), password_1.get()))
                    record = c.fetchone()

                    if record is None:
                        messagebox.showerror('Error', 'invalid username or password')
                    else:
                        messagebox.showinfo('Success', 'login is successful')

                    conn.commit()
                    conn.close()


                
        
               
                window=Toplevel()
                window.title("Home Page")
                window.geometry('1250x1000')
                window.config(bg='white')
                window.focus_force()
                window.grab_set()

        

    
    
        log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=home_page)
        
        
        log_in.place(x=113,y=252)

        


        sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
        sign_in.place(x=125,y=323) 

        
window=Tk()
obj=Login(window)
window=mainloop()











    
    
    