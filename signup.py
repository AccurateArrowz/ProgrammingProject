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
# class BalanceException(Exception):
#     pass
# def checkbalance():
#     money=10000
#     withdraw=int(input("Enter amount you want to withdraw = "))
#     try:
#         balance=money-withdraw
#         if (balance<2000):
#             raise BalanceException("Insufficient balance")
#         print(balance)
#     except BalanceException as be:
#         print (be)
# checkbalance()

# x=input("Enter any : ")
# try:
#     if type(x) is int:
#         raise TypeError("Only integers are allowed")
# except TypeError as TE:
#     print(TE)


# print("Use of assert statement")
# numbers=int(input("Enter a number: "))
# assert(numbers>=0),"oops...negative number"
# print("Number is positive")

# f=open('student.txt',mode='r')
# print("File Name: ",f.name)

# f1=open("Student.txt",mode='r')
# f2=open("student1.txt",mode='w')
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# print("completed")

# f=open('student,txt',mode='r')
# data=f.readlines()


# with ma by default nei file close bhairako hunxa\

# naya file ma kam garna paryo bhane x use garne
# normsl obj lai binary ma ocnvert garxa bytearray le

# with open("student.txt") as f:
#     data=f.read
#     print(data)
# print(f.closed)

import pickle
list=[1,2,3]
dict1={1:"abc",2:"hari"}
pickle_dict1=pickle.dumps(dict1)
