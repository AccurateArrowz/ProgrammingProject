
from tkinter import *
from tkinter import messagebox ,ttk
import sqlite3
from PIL import ImageTk,Image
import ast
# window= Tk()
# window.geometry('1250x1000')
# window.title("Learners")
# window.configure(bg='#E2C5ED')
# window.minsize(width=900,height=600)   
# window.maxsize(width=1600,height=1000)

pswdButtonClicked=0
confirmPswdButtonClicked=0


def homePage():
    window = Toplevel()
    window.title("Home Page")
    window.geometry('1250x1000')
    window.config(bg='white')
    window.focus_force()
    window.grab_set()

    # navigation frame-------------------------------------------------------------
    frame_home = Frame(window, width=1280, height=66, bg="#BE63D9")
    frame_home.place(x=0, y=0)

    # profile image-----------------------------------------------------------------
    #             circleimage=PhotoImage(file="circle.png")
    #             circleimage= circleimage.zoom(20) #with 250, I ended up running out of memory
    #             circleimage = circleimage.subsample(20)
    # panel_11= Button(frame_home,image = circleimage,bg="#BE63D9",bd=0,activebackground="#BE63D9")
    # panel_11.place(x=1140,y=15)

    # profileimage=PhotoImage(file="profile.png")
    #     # profileimage= profileimage.zoom(16) #with 250, I ended up running out of memory
    #     # profileimage = profileimage.subsample(23)
    #     # panel_11= Label(frame_home,image = profileimage,bg="white")
    #     # panel_11.place(x=1151,y=19)
    #     # profilelabel=Label(frame_home,text="Profile",font=("calibri",7,"bold"),bg="white",fg="black")
    #     # profilelabel.place(x=1150,y=40)

    # labels of learners in navigation frame------------------------------------------------------
    learners = Label(frame_home, text="Learners", font=("Brush Script MT", 28, 'bold'), bg="#BE63D9",
                     fg="#221C35")
    learners.place(x=17, y=12)

    # frame which is in white bg that is located where the button of software design,math and programming is-------
    frameofhomepage = Frame(window, width=1300, height=1600, bg="white")
    frameofhomepage.place(x=0, y=66)

    #     # button of mathematics-------------------------------------------------------------------
    math_img = PhotoImage(file="MathsCard.png")
    math_img.image = math_img
    math_img_lbl = Button(frameofhomepage, bg="white", image=math_img, bd=0, activebackground="white",
                          borderwidth=0)
    math_img_lbl.place(x=90, y=70)

    # button of programming---------------------------------------------------------------
    prog_img = PhotoImage(file="Programmingcard.png")
    prog_img.image = prog_img
    prog_img = Button(frameofhomepage, bg="white", image=prog_img, bd=0, activebackground="white",
                      borderwidth=0)
    prog_img.place(x=467, y=70)

    # button of software design----------------------------------------------------
    software_img = PhotoImage(file="SoftwareDesignCard.png")
    software_img.image = software_img
    software_img = Button(frameofhomepage, bg="white", image=software_img, bd=0, activebackground="white",
                          borderwidth=0)
    software_img.place(x=820, y=70)

    # def login_function(self):
    #     if self.username_1.get()=="" or self.username_1.get()=="":
    #         messagebox.showerror("Error","Fill the both fields",parent=self.window)
    #     elif self.username_1.get()!="r" or self.username_1.get()!="1":
    #         messagebox.showerror("Invalid username",parent=self.window)
    #     else:
    #         messagebox.showinfo("Welcome",f"Welcome {self.username_1.get()}\nYour Password: {self.username_1.get()}",parent=self.window)

    # button of subjects in navigation part------------------------------------------------------
    def onbutton1(e):
        subj['bg'] = '#E2C5ED'

    def leavebutton1(e):
        subj['bg'] = "#BE63D9"

    subj = Button(frame_home, text="Subjects", font=('Inter Normal', 20), bd=0, bg='#BE63D9', fg="black")
    subj.place(x=360, y=20)

    # bind methods
    subj.bind('<Enter>', onbutton1)
    subj.bind('<Leave>', leavebutton1)

    # button of ticketss in navigation part------------------------------------------------------
    def onbutton3(e):
        Button2['bg'] = '#E2C5ED'

    def leavebutton3(e):
        Button2['bg'] = "#BE63D9"

    Button2 = Button(frame_home, text="Tickets", font=('Inter Normal', 20), bg="#BE63D9", fg="black", bd=0)
    Button2.place(x=627, y=20)

    # bind methods
    Button2.bind('<Enter>', onbutton3)
    Button2.bind('<Leave>', leavebutton3)

    # button of notices in navigation part------------------------------------------------------
    def onbutton3(e):
        Button3['bg'] = '#E2C5ED'

    def leavebutton3(e):
        Button3['bg'] = "#BE63D9"

    Button3 = Button(frame_home, text="Notices", font=('Inter Normal', 20), bg="#BE63D9", fg="black", bd=0)
    Button3.place(x=905, y=20)

    # bind methods
    Button3.bind('<Enter>', onbutton3)
    Button3.bind('<Leave>', leavebutton3)

    # frame of footer part------------------------------------------------------
    frameofblack = Frame(window, width=1280, height=200, bg="#1D1D1D")
    frameofblack.place(x=0, y=630)

    # label of footer parts----------------------------------------------------------------------
    aboutus = Label(frameofblack, text="About Us", font=("Inter Normal", 15, "bold"), bg="#1D1D1D", fg="white")
    aboutus.place(x=100, y=2)

    y = Label(frameofblack, text="We are dedicated to making the students", font=("Calibri", 11), bg="#1D1D1D",
              fg="white")
    y.place(x=100, y=25)

    y1 = Label(frameofblack, text="learn various subjects and topics", font=("Calibri", 11), bg="#1D1D1D",
               fg="white")
    y1.place(x=100, y=45)

    y2 = Label(frameofblack, text="in an easy and fun way", font=("Calibri", 11), bg="#1D1D1D", fg="white")
    y2.place(x=100, y=65)

    contactus = Label(frameofblack, text="Contact Us", font=("Calibri", 15, "bold"), bg="#1D1D1D", fg="White")
    contactus.place(x=550, y=2)

    email = Label(frameofblack, text="learners@gmail.com", font=("Calibri", 11), bg="#1D1D1D", fg="White")
    email.place(x=550, y=27)

    phonenumber = Label(frameofblack, text="0012653/0127358", font=("Calibri", 11), bg="#1D1D1D", fg="White")
    phonenumber.place(x=550, y=50)

    followus = Label(frameofblack, text="Follow Us", font=("Calibri", 15, "bold"), bg="#1D1D1D", fg="White")
    followus.place(x=800, y=2)

    # photos downwards the follow us part----------------------------------------------------------------
    instaimage = PhotoImage(file="insta.png")
    instaimage = instaimage.zoom(16)
    instaimage = instaimage.subsample(20)
    panel_7 = Label(frameofblack, image=instaimage, bg="#1D1D1D")
    panel_7.place(x=805, y=35)

    fbimage = PhotoImage(file="facebook.png")
    fbimage = fbimage.zoom(16)
    fbimage = fbimage.subsample(20)
    panel_8 = Label(frameofblack, image=fbimage, bg="#1D1D1D")
    panel_8.place(x=825, y=35)

    limage = PhotoImage(file="linkedin.png")
    limage = limage.zoom(16)
    limage = limage.subsample(20)
    panel_9 = Label(frameofblack, image=limage, bg="#1D1D1D")
    panel_9.place(x=845, y=35)

    timage = PhotoImage(file="twitter.png")
    timage = timage.zoom(16)
    timage = timage.subsample(20)
    panel_10 = Label(frameofblack, image=timage, bg="#1D1D1D")
    panel_10.place(x=865, y=35)

    # new window when clicked in the images used part-------------------------------------------------------
    def imagesused():
        window = Toplevel()
        window.geometry('1250x1000')
        window.title("Images Used")

        window.config(bg='white')
        window.focus_force()
        window.grab_set()

    # button of images used in footer part-----------------------------------------------------------
    def onbuttonimages(e):
        iused['bg'] = 'gray'

    def leavebuttonimages(e):
        iused['bg'] = "black"

    iused = Button(frameofblack, text="Images Used", font=("Calibri", 15, "bold"), bd=0, bg="#1D1D1D", fg="White",
                   command=imagesused)
    iused.place(x=1000, y=0)
    iused.bind('<Enter>', onbuttonimages)
    iused.bind('<Leave>', leavebuttonimages)

    # yo eroor ayepaxi balla photo visible bhayoo---------------------------------------------------------
    def onbutton(e):
        Button1['bg'] = '#E2C5ED'

    def leavebutton(e):
        Button1['bg'] = "#BE63D9"

    Button1 = Button(frame_home, text="Subjects", font=('Inter Normal', 20), bg='white', fg="black", bd=0,
                     command=subject)
    Button1.place(x=360, y=20)


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
        password_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0,fg='black')
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
                    passwordHideButton.config(text='H')
                    user_8.config(show='')
                elif confirmPswdButtonClicked % 2 == 0:
                    passwordHideButton.config(text='S')
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
                        homePage() #home page will be created if record exists
                        self.loginWindow.destroy()
                    conn.commit()
                    conn.close()

                
        


        

    
    
        log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=login_authentication)
        
        
        log_in.place(x=103,y=252)

        


        sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
        sign_in.place(x=115,y=323)

        
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










    
    
    