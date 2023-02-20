from tkinter import *
from tkinter import messagebox ,ttk
from PIL import ImageTk,Image
import ast
window= Tk()
window.title("Learners")
window.configure(bg='#E2C5ED')
window.minsize(width=900,height=600)   
window.maxsize(width=1600,height=1000)
img=PhotoImage(file="icon.png")
window.iconphoto(False,img)


# Main___Photo
imgpath = 'Rectangle 1.png'
img = PhotoImage(file=imgpath)
img = img.zoom(33) #with 250, I ended up running out of memory
img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel = Label(window, image = img)

Label(window,image=img,bg='#E2C5ED').place(x=10,y=55)

# Main___Frame
frame=Frame(window,width=320,height=390,bg='#F3EEE5')
frame.place(x=835,y=195)

heading=Label(text="Learners",fg="red",bg='#E2C5ED',font=('Ink Free',70,'bold'))
heading.place(x=500,y=-5)


details=Label(frame,text="Your Hub for learning",font=("Calibiri",18,"bold"),bg='#F3EEE5',fg="black").place(x=29,y=26)

# UserName                                            

username=Label(frame,text="Username",font=('Inter Normal',14),bg='#F3EEE5',fg="black").place(x=25,y=80)
username_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0).place(x=30,y=120)

# username_______image
imgpath_1 = 'Group.png'
Username_image = PhotoImage(file=imgpath_1)
Username_image = Username_image.zoom(29) #with 250, I ended up running out of memory
Username_image = Username_image.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel_1 = Label(window, image = Username_image,bg='#F3EEE5')

Label(window,image=Username_image,bg='#F3EEE5').place(x=952,y=280)

# Password

password=Label(frame,text="Password",font=("Inter Normal",14),bg='#F3EEE5',fg="black").place(x=25,y=160)
password_1=Entry(frame,bg="White",width=21,font=('Inter Normal',16),bd=0).place(x=30,y=199)

# password____Image
imgpath_2 = 'ABC.png'
password_image = PhotoImage(file=imgpath_2)
password_image = password_image.zoom(30) #with 250, I ended up running out of memory
password_image = password_image.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel_1 = Label(window, image = password_image,bg='#F3EEE5')

Label(window,image=password_image,bg='#F3EEE5').place(x=952,y=356)




# def on_enter(e):
#     user.delete(0,'end')
# def on_leave(e):
#     if user.get()=='':
#         user.insert(0,'Username')

# user=Entry(frame,width=25,fg='black',border=0,bg='#F3EEE5',font=('Consolas',13))
# user.place(x=20,y=89)
# user.insert(0,'Username')
# user.bind("<FocusIn>",on_enter)
# user.bind("<FocusOut>",on_leave)

# Frame(frame,width=260,height=2,bg='black').place(x=15,y=112)

# def on_enter(e):
#     code.delete(0,'end')
# def on_leave(e):
#     if code.get()=='':
#         code.insert(0,'Password')

# code=Entry(frame,width=25,fg='black',border=0,bg='#F3EEE5',font=('Consolas',13))
# code.place(x=20,y=134)
# code.insert(0,'Password')
# code.bind("<FocusIn>",on_enter)
# code.bind("<FocusOut>",on_leave)

# Frame(frame,width=260,height=2,bg='black').place(x=15,y=159)






# def on_enter(e):
#     c_code.delete(0,'end')
# def on_leave(e):
#     if c_code.get()=='':
#         c_code.insert(0,'Conform Password')

# c_code=Entry(frame,width=25,fg='black',border=0,bg='Light blue',font=('Consolas',11))
# c_code.place(x=30,y=220)
# c_code.insert(0,'Conform Password')
# c_code.bind("<FocusIn>",on_enter)
# c_code.bind("<FocusOut>",on_leave)

# Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


# forget password;;;;;;;;;
# def forget_password():
#     window=Toplevel()
#     window.title("Forget Password")
#     window.maxsize(width=700,height=600)
#     window.minsize(width=700,height=600)
#     window.config(bg="silver")
#     window.focus_force()
#     window.grab_set()

def signup():
    window=Toplevel()
    window.title("Sign Up")
    window.maxsize(width=1290,height=1000)
    window.minsize(width=900,height=600)
    window.config(bg='#F3EEE5')
    window.focus_force()
    window.grab_set()




   


    


    
    frame_2=Frame(window,width=500,height=583,bg='#E2C5ED')
    frame_2.place(x=80,y=68)

    text=Label(frame_2,text="CREATE YOUR ACCOUNT",fg='#4F1D63',bg='#E2C5ED',font=('Calibri',29,'bold'))
    text.place(x=60,y=35)

    def on_enter_1(e):
        x=user_1.get()
        if x=='First Name':
            user_1.delete(0,'end')
    def on_leave_1(e):
        if user_1.get()=='':
         user_1.insert(0,'First Name')

    user_1=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_1.place(x=80,y=110)
    user_1.insert(0,'First Name')
    user_1.bind("<FocusIn>",on_enter_1)
    user_1.bind("<FocusOut>",on_leave_1)

    # Frame(frame_2,width=285,height=2,bg='black').place(x=15,y=130)


# Frame(frame,width=295,height=2,bg='black').place(x=15,y=192)

    def on_enter_1(e):
        x=user_2.get()
        if x=='Last Name':
            user_2.delete(0,'end')
    def on_leave_1(e):
        if user_2.get()=='':
         user_2.insert(0,'Last Name')

    user_2=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_2.place(x=80,y=155)
    user_2.insert(0,'Last Name')
    user_2.bind("<FocusIn>",on_enter_1)
    user_2.bind("<FocusOut>",on_leave_1)
    
    gender=Label(frame_2,text="Gender",fg='black',bg='#E2C5ED',font=('Inter Normal',15))
    gender.place(x=85,y=200)

    var=IntVar()
    ca=Checkbutton(window,text=("Male"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var)
    ca.place(x=240,y=265)
    var_1=IntVar
    ca_1=Checkbutton(window,text=("Female"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_1)
    ca_1.place(x=309,y=265)
    var_2=IntVar
    ca_2=Checkbutton(window,text=("Others"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_2)
    ca_2.place(x=399,y=265)
    
    def on_enter_1(e):
        user_3.delete(0,'end')
    def on_leave_1(e):
        if user_2.get()=='':
         user_3.insert(0,'Year')

    user_3=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
    user_3.place(x=95,y=276)
    user_3.insert(0,'Year')
    user_3.bind("<FocusIn>",on_enter_1)
    user_3.bind("<FocusOut>",on_leave_1)
    
    dob=Label(frame_2,text="Date of Birth",font=('Inter Normal',15),bg='#E2C5ED',fg="black")
    dob.place(x=85,y=237)

    
    

    def on_enter_1(e):
        user_4.delete(0,'end')
    def on_leave_1(e):
        if user_4.get()=='':
         user_4.insert(0,'Month')

    user_4=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=6)
    user_4.place(x=170,y=276)
    user_4.insert(0,'Month')
    user_4.bind("<FocusIn>",on_enter_1)
    user_4.bind("<FocusOut>",on_leave_1)

    def on_enter_1(e):
        user_5.delete(0,'end')
    def on_leave_1(e):
        if user_5.get()=='':
         user_5.insert(0,'Date')

    user_5=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
    user_5.place(x=248,y=276)
    user_5.insert(0,'Date')
    user_5.bind("<FocusIn>",on_enter_1)
    user_5.bind("<FocusOut>",on_leave_1)
    
    def on_enter_1(e):
        user_6.delete(0,'end')
    def on_leave_1(e):
        if user_6.get()=='':
         user_6.insert(0,'Username')

    
    user_6=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_6.place(x=75,y=360)
    user_6.insert(0,'Username')
    user_6.bind("<FocusIn>",on_enter_1)
    user_6.bind("<FocusOut>",on_leave_1)
    
    # def on_enter_1(e):
    #     user_7.delete(0,'end')
    # def on_leave_1(e):
    #     if user_7.get()=='':
    #      user_7.insert(0,'Type')

    
    # user_7=Label(frame_2,text="   Type",fg='black',bg='#E2C5ED',font=('Calibri',16),width=32)
    # user_7.place(x=85,y=392)
    # user_7.insert(0,'Type')
    # user_7.bind("<FocusIn>",on_enter_1)
    # user_7.bind("<FocusOut>",on_leave_1)


    hi=Label(frame_2,text="Type",width=15,bg="#E2C5ED",font=("Inter Normal",16))
    hi.place(x=20,y=316)
    user7_var=StringVar(value='Student')
    user7_combobox=ttk.Combobox(frame_2,values=['Teacher','Student','Admin'],font=('Inter Normal',15),width=8, textvariable=user7_var)
    user7_combobox.place(x=158,y=316)
    

    def on_enter_1(e):
        user_7.delete(0,'end')
    def on_leave_1(e):
        if user_7.get()=='':
         user_7.insert(0,'New Password')

    
    user_7=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_7.place(x=75,y=404)
    user_7.insert(0,'New Password')
    user_7.bind("<FocusIn>",on_enter_1)
    user_7.bind("<FocusOut>",on_leave_1)
    
    def on_enter_1(e):
        user_8.delete(0,'end')
    def on_leave_1(e):
        if user_8.get()=='':
         user_8.insert(0,'Confirm Password')

    
    user_8=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
    user_8.place(x=75,y=449)
    user_8.insert(0,'Confirm Password')
    user_8.bind("<FocusIn>",on_enter_1)
    user_8.bind("<FocusOut>",on_leave_1)

    button_register=Button(frame_2,pady=3,width=8,height=-9,border=0,text="Register",bg="#AE08ED",fg="White",font=("Inter Normal",16))
    button_register.place(x=200,y=495)



# Photo__Of__Signup__window

    
    image_2=PhotoImage(file='Rectangle 6.png')
    image_2=image_2.zoom(30) #with 250, I ended up running out of memory
    image_2=image_2.subsample(32) #mechanically, here it is adjusted to 32 instead of 320

    why=Label(window,image=image_2,bg="#F3EEE5")
    why.place(x=720,y=115)
    Label(window,image=image_2,command=signup)

    


# details=Label(frame,text="Enter your details",font=("Calibiri",20,"bold"),bg="#D9FBFB",fg="black").place(x=40,y=32)


   
# t=Label(window,text="Forgot Password",font=("Calibri",20,"bold"),bg="silver",fg="Purple").place(x=240,y=10)



    # question=Label(window,text="Security question",font=("Calibri",14,"bold"),bg="silver",fg="Black").place(x=88,y=94)
    


    # # title_lablel=Label(window,text="Security questions")
    # title_combobox=ttk.Combobox(window,values=["","Your first pet name","Your Birth place","Your Best friend name","Your father name"

    # ])
    # # title_lablel.grid(row=3,column=0)
    # title_combobox.place(x=55,y=121,width=230,height=30)

    # answer=Label(window,text="Answer",font=("Calibri",14,"bold"),bg="silver",fg="black").place(x=120,y=166)
    # txt_answer=Entry(window,font=("new times roman",15),bg="white").place(x=55,y=193,width=230,height=30)

    # new_pww=Label(window,text="New password",font=("Calibri",14,"bold"),bg="silver",fg="black").place(x=96,y=238)
    # pww=Entry(window,font=("new times roman",15),bg="white").place(x=45,y=267,width=230,height=30)
    
    # change_pw=Button(window,text="Reset password",font=("Calibri",16,"bold"),bg="Light Blue",fg="Black").place(x=82,y=320,width=172,height=40)

# f_p=Button(frame,text="Forgot password?",border=0,pady=1,padx=2,width=14,fg="Black",cursor='hand2',bg='#D9FBFB',font=('Calibri',12))
# f_p.place(x=100,y=258)

label=Label(frame,text="Don't have an account?",fg='black',bg='#F3EEE5',font=('Inter Normal',14),   padx=20,pady=20)
label.place(x=45,y=280)
sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
sign_in.place(x=125,y=323) 



# 5 ota circle dif axis ma ani color cha difr fill hunaparxa;;;;;;;hw


# password visiblity,,,,
# def show_hide_password():
#     if code['show']=='*':
#         code.configure(show='')
#         show_hide_btn.configure(text=show_face)
#     else:
#         code.configure(show='*')
#         show_hide_btn.configure(text=hide_face)
# show_hide_btn=Button(window,text=(hide_face,),bg='light blue',font=('bold',11),bd=0,command=show_hide_password).place(x=1070,y=269)

# Dashboard
def home_page():
    
    window=Toplevel()
    window.title("Home Page")
    window.maxsize(width=1290,height=1000)
    window.minsize(width=900,height=600)
    window.config(bg='white')
    window.focus_force()
    window.grab_set()


    frame_home=Frame(window,width=1280,height=66,bg="#BE63D9")
    frame_home.place(x=0,y=0)

    learners=Label(frame_home,text="Learners",font=("Ink Free",24,'bold'),bg="#BE63D9",fg="#221C35")
    learners.place(x=8,y=20)

    image1= PhotoImage(file='p.png')
    image2= PhotoImage(file='math.png')
    image3= PhotoImage(file='math.png')
    frame=Frame(window,)
    frame.pack(pady=100)
    button1=Button(frame,image=image1,bg='black')
    button1.grid(row=0,column=0)
    button2=Button(frame,image=image2,bg='black')
    button2.grid(row=0,column=1,padx=30)
    button3=Button(frame,image=image3,bg='black')
    button3.grid(row=0,column=2)
    
    

        # frame of programming
    
    def subject():

       
#         Label(window, text = 'GeeksforGeeks', font =( 'Verdana', 15)).pack(side = TOP, pady = 10)
  
# # Creating a photoimage object to use image
#         photo = PhotoImage(file = "math.png")
  
# # here, image option is used to
# # set image on button
#         Button(window, text = 'Click Me !', image = photo,cursor='hand2').pack(side = TOP)
        
       


        
       
        # # imgpath_4 = 'p.png'
        # # img_4 = PhotoImage(file=imgpath_4)
        # # img_4= img_4.zoom(20) #with 250, I ended up running out of memory
        # # img_4 = img_4.subsample(20) #mechanically, here it is adjusted to 32 instead of 320
        # # panel_4 = Label(window,image = img_4)
        # # panel_4.place(x=10,y=5)
        # # Label(window,image=img_4)
        

        # # frame_prog=Button(window,width=44,height=25,bg="#FFF1F0",activebackground="#FFF1F0",bd=0,command=subject)
        # # frame_prog.place(x=470,y=166)
        
        
    
        # prog_text=Label(window,text="Programming and Algorithms",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
        # prog_text.place(x=470,y=330)
    
        # prog_text_1=Label(window,text="This subject explains various",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
        # prog_text_1.place(x=470,y=360)
        # prog_text_2=Label(window,text="concepts of programming and",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
        # prog_text_2.place(x=470,y=400)
        # prog_text_3=Label(window,text="algorithms",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
        # prog_text_3.place(x=470,y=440)

    #     # frame of software design
        
    #     frame_sd=Button(window,width=44,height=25,bg="#FFF1F0",activebackground="#FFF1F0",bd=0,command=subject)
    #     frame_sd.place(x=860,y=166)
    #     sd_text1=Label(window,text="Software Design",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    #     sd_text1.place(x=930,y=330)
    
    
    #     sd_text2=Label(window,text="This subject explains about the",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     sd_text2.place(x=870,y=380)
    #     sd_text3=Label(window,text="principles of designing a ",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     sd_text3.place(x=870,y=410)
    #     sd_text4=Label(window,text="software and best practices",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     sd_text4.place(x=870,y=440)
        

    

    

    # # frame of math part
    #     frame_math=Button(window,width=42,height=24,bg="#FFF1F0",activebackground="#FFF1F0",bd=0,command=subject)
    #     frame_math.place(x=100,y=166)

        
        
    #     imgpath_4 = 'p.png'
    #     img_4 = PhotoImage(file=imgpath_4)
    #     img_4= img_4.zoom(50) #with 250, I ended up running out of memory
    #     img_4 = img_4.subsample(600)
        
    #     m_text=Label(window,text="Mathematics",font=("Inter Normal",16,"bold"),bg="#FFF1F0",fg="black")
    #     m_text.place(x=150,y=340)
    
    #     m_text_1=Label(window,text="This subject teaches about",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     m_text_1.place(x=115,y=390)
    #     m_text_2=Label(window,text="ways of combining maths with",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     m_text_2.place(x=115,y=430)
    #     m_text_3=Label(window,text="programming",font=("Inter Normal",15),bg="#FFF1F0",fg="black")
    #     m_text_3.place(x=115,y=465)

        


    # photo of programmming part
    #     imgpath_5 = 'math.png'
    #     img_5 = PhotoImage(file=imgpath_5)
    #     img_5= img_5.zoom(30) #with 250, I ended up running out of memory
    #     img_5 = img_5.subsample(40) #mechanically, here it is adjusted to 32 instead of 320
    #     panel_5 = Label(frame_prog,image = img_5,bg="#FFF1F0",command=image)
    #     panel_5.place(x=110,y=200)
    #     Label(frame_prog,image=img_5)
        
        def onbutton(e):
             Button1['bg']='#E2C5ED'
        def leavebutton(e):
             Button1['bg']="#BE63D9"
        
        Button1=Button(frame_home,text="Subjects",font=('Inter Normal',20),bg='#BE63D9',fg="black",bd=0,command=subject)
        Button1.place(x=360,y=20)

    # bind methods
        Button1.bind('<Enter>',onbutton)
        Button1.bind('<Leave>',leavebutton)
        labell=Label(frame_home,text=None,font=10)
        labell.place(x=3,y=30)
   

    def onbutton2(e):
        Button2['bg']='#E2C5ED'
    def leavebutton2(e):
        Button2['bg']="#BE63D9"
    Button2=Button(frame_home,text="Tickets",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0,activebackground="#FF7F50")
    Button2.place(x=627,y=20)

    # bind methods
    Button2.bind('<Enter>',onbutton2)
    Button2.bind('<Leave>',leavebutton2)
    labell2=Label(frame_home,text=None,font=10)
    labell2.place(x=3,y=30)

    
    def onbutton3(e):
        Button3['bg']='#E2C5ED'
    def leavebutton3(e):
        Button3['bg']="#BE63D9"
        
    Button3=Button(frame_home,text="Notices",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0,activebackground="#FF7F50")
    Button3.place(x=905,y=20)

    # bind methods
    Button3.bind('<Enter>',onbutton3)
    Button3.bind('<Leave>',leavebutton3)
    labell3=Label(frame_home,text=None,font=10)
    labell3.place(x=3,y=30)
 

        

    #  photo of mathematics part
    

    
    # Button1=Button(frame_home,text="Subjects",font=('Inter Normal',20),bg="#FF7F50",fg="black",bd=0,activebackground="#FF7F50",command=subject)
    # Button1.place(x=340,y=18)
   

log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=home_page)
log_in.place(x=113,y=242)


window.mainloop()

# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# next window for signup/register page--------------------------------------------------------
        # def signup():
        #     window=Toplevel()
        #     window.title("Sign Up")
        #     window.maxsize(width=1290,height=1000)
        #     window.minsize(width=900,height=600)
        #     window.config(bg='#F3EEE5')
        #     window.focus_force()
        #     window.grab_set()


    
            

        
    # frame for register--------------------------------------------------------------------------
        # frame_2=Frame(window,width=500,height=583,bg='#E2C5ED')
        # frame_2.place(x=80,y=68)

    
    # # labels of register page frame--------------------------------------------------------------
    #     text=Label(frame_2,text="CREATE YOUR ACCOUNT",fg='#4F1D63',bg='#E2C5ED',font=('Calibri',29,'bold'))
    #     text.place(x=40,y=35)

        # sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
        # sign_in.place(x=125,y=323) 

    

window=Tk()
obj=Login(window)
window=mainloop()

    # labels and entry box for first name---------------------------------------------------------
#     def on_enter_1(e):
#         x=user_1.get()
#         if x=='     First Name':
#             user_1.delete(0,'end')
#     def on_leave_1(e):
#         if user_1.get()=='':
#          user_1.insert(0,'     First Name')

#     user_1=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
#     user_1.place(x=65,y=110)
#     user_1.insert(0,'     First Name')
#     user_1.bind("<FocusIn>",on_enter_1)
#     user_1.bind("<FocusOut>",on_leave_1)


#     # labels and entry box for last name--------------------------------------------------
#     def on_enter_1(e):
#         x=user_2.get()
#         if x=='     Last Name':
#             user_2.delete(0,'end')
#     def on_leave_1(e):
#         if user_2.get()=='':
#          user_2.insert(0,'     Last Name')

#     user_2=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
#     user_2.place(x=65,y=155)
#     user_2.insert(0,'     Last Name')
#     user_2.bind("<FocusIn>",on_enter_1)
#     user_2.bind("<FocusOut>",on_leave_1)


#     #gender--------------------------------------------------------
#     gender=Label(frame_2,text="Gender",fg='black',bg='#E2C5ED',font=('Inter Normal',15))
#     gender.place(x=75,y=200)

    # var=IntVar()
    # ca=Checkbutton(window,text=("Male"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var)
    # ca.place(x=230,y=265)
    # var_1=IntVar
    # ca_1=Checkbutton(window,text=("Female"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_1)
    # ca_1.place(x=299,y=265)
    # var_2=IntVar
    # ca_2=Checkbutton(window,text=("Others"),bg='#E2C5ED',fg='Black',font=('Arial',14),variable=var_2)
    # ca_2.place(x=389,y=265)
    

#     # labels and entry box for date of birth---------------------------------
#     def on_enter_1(e):
#         user_3.delete(0,'end')
#     def on_leave_1(e):
#         if user_2.get()=='':
#          user_3.insert(0,' Year')

#     user_3=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
#     user_3.place(x=85,y=276)
#     user_3.insert(0,' Year')
#     user_3.bind("<FocusIn>",on_enter_1)
#     user_3.bind("<FocusOut>",on_leave_1)
    
#     dob=Label(frame_2,text="Date of Birth",font=('Inter Normal',15),bg='#E2C5ED',fg="black")
#     dob.place(x=75,y=237)

#     DOBimage=PhotoImage(file='DOB.png')
#     DOBimage= DOBimage.zoom(15) #with 250, I ended up running out of memory
#     DOBimage = DOBimage.subsample(20)
#     imageofdob=Label(window,image=DOBimage,bg='#E2C5ED')
#     imageofdob.place(x=271,y=306)
    
#     def on_enter_1(e):
#         user_4.delete(0,'end')
#     def on_leave_1(e):
#         if user_4.get()=='':
#          user_4.insert(0,' Month')

#     user_4=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=6)
#     user_4.place(x=160,y=276)
#     user_4.insert(0,' Month')
#     user_4.bind("<FocusIn>",on_enter_1)
#     user_4.bind("<FocusOut>",on_leave_1)

#     def on_enter_1(e):
#         user_5.delete(0,'end')
#     def on_leave_1(e):
#         if user_5.get()=='':
#          user_5.insert(0,' Date')

#     user_5=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',14),width=5)
#     user_5.place(x=238,y=276)
#     user_5.insert(0,' Date')
#     user_5.bind("<FocusIn>",on_enter_1)
#     user_5.bind("<FocusOut>",on_leave_1)
    
#     #labels and entry box for user name---------------------------------
#     def on_enter_1(e):
#         x=user_6.get()
#         if x=='     Username':
#             user_6.delete(0,'end')
        
#     def on_leave_1(e):
#         if user_6.get()=='':
#          user_6.insert(0,'     Username')

#     user_6=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
#     user_6.place(x=65,y=360)
#     user_6.insert(0,'     Username')
#     user_6.bind("<FocusIn>",on_enter_1)
#     user_6.bind("<FocusOut>",on_leave_1)
    
#     # userimage=PhotoImage(file='Group.png')
#     # userimage= userimage.zoom(16) #with 250, I ended up running out of memory
#     # userimage = userimage.subsample(20)
#     # imageofuser=Label(window,image=userimage,bg='white')
#     # imageofuser.place(x=150,y=432)


#     # labels and entry box for Type(student,teacher)--------------------------------------
#     hi=Label(frame_2,text="Type",width=15,bg="#E2C5ED",font=("Inter Normal",16))
#     hi.place(x=10,y=316)
#     user7_var=StringVar(value='  Student')
#     user7_combobox=ttk.Combobox(frame_2,values=['Teacher','Student'],font=('Inter Normal',15),width=8, textvariable=user7_var)
#     user7_combobox.place(x=148,y=316)
    
#     # labels and entry box for new password----------------------------------------------------
#     def on_enter_1(e):
#         x=user_7.get()
#         if x=='     New Password':
#             user_7.delete(0,'end')
#     def on_leave_1(e):
#         if user_7.get()=='':
#          user_7.insert(0,'     New Password')

#     user_7=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
#     user_7.place(x=65,y=404)
#     user_7.insert(0,'     New Password')
#     user_7.bind("<FocusIn>",on_enter_1)
#     user_7.bind("<FocusOut>",on_leave_1)
    
#     # labels and entry box for confirm password--------------------------------------------
#     def on_enter_1(e):
#         x=user_8.get()
#         if x=='     Confirm Password':
#             user_8.delete(0,'end')
#     def on_leave_1(e):
#         if user_8.get()=='':
#          user_8.insert(0,'     Confirm Password')

#     user_8=Entry(frame_2,fg='black',bg='white',font=('Inter Normal',16),width=29)
#     user_8.place(x=65,y=449)
#     user_8.insert(0,'     Confirm Password')
#     user_8.bind("<FocusIn>",on_enter_1)
#     user_8.bind("<FocusOut>",on_leave_1)


#     # button of register----------------------------------------------------------------
#     button_register=Button(frame_2,pady=3,width=8,height=-9,border=0,text="Register",bg="#39339B",fg="White",font=("Inter Normal",16),command=window.destroy)
#     button_register.place(x=180,y=495)


#     # Photo__Of__Signup__window-------------------------------------------------------------------
#     image_2=PhotoImage(file='Rectangle 6.png')
#     image_2=image_2.zoom(30) #with 250, I ended up running out of memory
#     image_2=image_2.subsample(32) #mechanically, here it is adjusted to 32 instead of 320

#     why=Label(window,image=image_2,bg="#F3EEE5")
#     why.place(x=720,y=115)
#     Label(window,image=image_2,command=signup)


#     # if len(user_7.get()) <6 :
#     #     errorDisplayFunction()


# # # labels of don't have an account in log in page frame-----------------------------------------------
# #         label=Label(frame,text="Don't have an account?",fg='black',bg='#F3EEE5',font=('Inter Normal',14),   padx=20,pady=20)
# #         label.place(x=45,y=280)

# # # labels of sign up in log in page frame-----------------------------------------------------------
# #         sign_in=Button(frame,width=6,text='Sign up',border=0,bg='#F3EEE5',cursor='hand2',fg="Blue",font=("Calibri",15,'bold',UNDERLINE),command=signup)
# #         sign_in.place(x=125,y=323) 


# # window of main home page/dashboard-------------------------------------------------
# def home_page():
    
#     window=Toplevel()
#     window.title("Home Page")
#     window.geometry('1250x1000')
#     window.config(bg='white')
#     window.focus_force()
#     window.grab_set()


#     # navigation frame-------------------------------------------------------------
#     frame_home=Frame(window,width=1280,height=66,bg="#BE63D9")
#     frame_home.place(x=0,y=0)


#     # profile image-----------------------------------------------------------------
#     circleimage=PhotoImage(file="circle.png")
#     circleimage= circleimage.zoom(20) #with 250, I ended up running out of memory
#     circleimage = circleimage.subsample(20)
#     panel_11= Button(frame_home,image = circleimage,bg="#BE63D9",bd=0,activebackground="#BE63D9")
#     panel_11.place(x=1140,y=15)

#     # profileimage=PhotoImage(file="profile.png")
#     # profileimage= profileimage.zoom(16) #with 250, I ended up running out of memory
#     # profileimage = profileimage.subsample(23)
#     # panel_11= Label(frame_home,image = profileimage,bg="white")
#     # panel_11.place(x=1151,y=19)
#     # profilelabel=Label(frame_home,text="Profile",font=("calibri",7,"bold"),bg="white",fg="black")
#     # profilelabel.place(x=1150,y=40)
    
#     # labels of learners in navigation frame------------------------------------------------------
#     learners=Label(frame_home,text="Learners",font=("Brush Script MT",28,'bold'),bg="#BE63D9",fg="#221C35")
#     learners.place(x=17,y=12)

    
#     # frame which is in white bg that is located where the button of software design,math and programming is-------
#     frameofhomepage=Frame(window,width=1300,height=1600,bg="white")
#     frameofhomepage.place(x=0,y=66)

    
    

#     # button of mathematics-------------------------------------------------------------------
#     math_img=PhotoImage(file="MathsCard.png")
#     math_img.image=math_img
#     math_img_lbl=Button(frameofhomepage,bg="white",image=math_img,bd=0,activebackground="white",borderwidth=0)
#     math_img_lbl.place(x=90,y=70)

#     # button of programming---------------------------------------------------------------
#     prog_img=PhotoImage(file="Programmingcard.png")
#     prog_img.image=prog_img
#     prog_img=Button(frameofhomepage,bg="white",image=prog_img,bd=0,activebackground="white",borderwidth=0)
#     prog_img.place(x=467,y=70)

#     # button of software design----------------------------------------------------
#     software_img=PhotoImage(file="SoftwareDesignCard.png")
#     software_img.image=software_img
#     software_img=Button(frameofhomepage,bg="white",image=software_img,bd=0,activebackground="white",borderwidth=0)
#     software_img.place(x=820,y=70)
    
#     # button of subjects in navigation part------------------------------------------------------
#     def onbutton1(e):
#         subj['bg']='#E2C5ED'
#     def leavebutton1(e):
#         subj['bg']="#BE63D9"
        
#     subj=Button(frame_home,text="Subjects",font=('Inter Normal',20),bd=0,bg='#BE63D9',fg="black")
#     subj.place(x=360,y=20)

#     # bind methods
#     subj.bind('<Enter>',onbutton1)
#     subj.bind('<Leave>',leavebutton1)
    
#     # button of ticketss in navigation part------------------------------------------------------
#     def onbutton3(e):
#         Button2['bg']='#E2C5ED'
#     def leavebutton3(e):
#         Button2['bg']="#BE63D9"
#     Button2=Button(frame_home,text="Tickets",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0)
#     Button2.place(x=627,y=20)

#     # bind methods
#     Button2.bind('<Enter>',onbutton3)
#     Button2.bind('<Leave>',leavebutton3)
    
#     # button of notices in navigation part------------------------------------------------------
#     def onbutton3(e):
#         Button3['bg']='#E2C5ED'
#     def leavebutton3(e):
#         Button3['bg']="#BE63D9"
        
#     Button3=Button(frame_home,text="Notices",font=('Inter Normal',20),bg="#BE63D9",fg="black",bd=0)
#     Button3.place(x=905,y=20)

#     # bind methods
#     Button3.bind('<Enter>',onbutton3)
#     Button3.bind('<Leave>',leavebutton3)
    

#     #frame of footer part------------------------------------------------------
#     frameofblack=Frame(window,width=1280,height=200,bg="black")
#     frameofblack.place(x=0,y=630)



#     # label of footer parts----------------------------------------------------------------------
#     aboutus=Label(frameofblack,text="About Us",font=("Inter Normal",13,"bold"),bg="black",fg="white")
#     aboutus.place(x=100,y=2)

#     y=Label(frameofblack,text="We are dedicated to making the students",font=("Calibri",11),bg="black",fg="white")
#     y.place(x=100,y=25)

#     y1=Label(frameofblack,text="learn various subjects and topics",font=("Calibri",11),bg="black",fg="white")
#     y1.place(x=100,y=45)

#     y2=Label(frameofblack,text="in an easy and fun way",font=("Calibri",11),bg="black",fg="white")
#     y2.place(x=100,y=65)

#     contactus=Label(frameofblack,text="Contact Us",font=("Calibri",15,"bold"),bg="black",fg="White")
#     contactus.place(x=550,y=2)

#     email=Label(frameofblack,text="learners@gmail.com",font=("Calibri",11),bg="black",fg="White")
#     email.place(x=550,y=27)

#     phonenumber=Label(frameofblack,text="0012653/0127358",font=("Calibri",11),bg="black",fg="White")
#     phonenumber.place(x=550,y=50)

#     followus=Label(frameofblack,text="Follow Us",font=("Calibri",15,"bold"),bg="black",fg="White")
#     followus.place(x=800,y=2)



#     # photos downwards the follow us part----------------------------------------------------------------
#     instaimage=PhotoImage(file="insta.png")
#     instaimage= instaimage.zoom(16) 
#     instaimage = instaimage.subsample(20)
#     panel_7 = Label(frameofblack,image = instaimage,bg="black")
#     panel_7.place(x=805,y=35)
 
#     fbimage=PhotoImage(file="facebook.png")
#     fbimage= fbimage.zoom(16) 
#     fbimage = fbimage.subsample(20)
#     panel_8 = Label(frameofblack,image = fbimage,bg="black")
#     panel_8.place(x=825,y=35)

#     limage=PhotoImage(file="linkedin.png")
#     limage= limage.zoom(16)
#     limage = limage.subsample(20)
#     panel_9 = Label(frameofblack,image = limage,bg="black")
#     panel_9.place(x=845,y=35)

#     timage=PhotoImage(file="twitter.png")
#     timage= timage.zoom(16) 
#     timage = timage.subsample(20)
#     panel_10 = Label(frameofblack,image = timage,bg="black")
#     panel_10.place(x=865,y=35)


#     #new window when clicked in the images used part-------------------------------------------------------
#     def imagesused():
#         window=Toplevel()
#         window.geometry('1250x1000')
#         window.title("Images Used")
    
#         window.config(bg='white')
#         window.focus_force()
#         window.grab_set()
    
#     # button of images used in footer part-----------------------------------------------------------
#     def onbuttonimages(e):
#         iused['bg']='gray'
#     def leavebuttonimages(e):
#         iused['bg']="black"
#     iused=Button(frameofblack,text="Images Used",font=("Calibri",15,"bold"),bd=0,bg="black",fg="White",command=imagesused)
#     iused.place(x=1000,y=0)
#     iused.bind('<Enter>',onbuttonimages)
#     iused.bind('<Leave>',leavebuttonimages)


    
        
    

# yo eroor ayepaxi balla photo visible bhayoo---------------------------------------------------------
# def onbutton(e):
#              Button1['bg']='#E2C5ED'
# def leavebutton(e):
#              Button1['bg']="#BE63D9"
        
# Button1=Button(text="Subjects",font=('Inter Normal',20),bg='white',fg="black",bd=0,command=subject)
# Button1.place(x=360,y=20)

 

#     window=mainloop()

    
    
# log in button in the log in page----------------------------------------------------------
# log_in=Button(frame,width=9,pady=3,text="Log in",bg="#2586DA",fg="White",border=0,font=('Calibri',13),command=home_page)
# log_in.place(x=113,y=242)

# creating database for registrations
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