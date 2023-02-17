def on_enter(e):
    c_code.delete(0,'end')
def on_leave(e):
    if c_code.get()=='':
        c_code.insert(0,'Conform Password')

c_code=Entry(frame,width=25,fg='black',border=0,bg='Light blue',font=('Consolas',11))
c_code.place(x=30,y=220)
c_code.insert(0,'Conform Password')
c_code.bind("<FocusIn>",on_enter)
c_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)