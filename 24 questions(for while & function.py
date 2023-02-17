# 24 questions:
# print "softwarica" 10 times

# def ye():
#   for i in range(1,11):
#     print("softwarica")
# ye()

# def a(b):
#     i=1
#     while i<11:
#         print(b)
#         i=i+1
# a("softwarica")


# Sum of a list 
# a=[1,2,3,4,5]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# def a():
#     a=[1,2,3,4,5]
#     sum=0
#     i=0
#     b=len(a)
#     while i<b:
#       sum=sum+a[i]
#       i=i+1
#     print(sum)
# a()

# print each character using indexing
# def a():
#   a="python"
#   b=len(a)
#   for i in range(b):
#     print(i,"=",a[i])
# a()

# def a():
#   i=0
#   a="python"
#   b=len(a)
#   while i<b:
#     print(i,"=",a[i])
#     i=i+1
# a()

# program to display each element of a list
# def a():
#   a=[1,2,3,4,5]
#   for i in range(len(a)):
#     print(a[i])
# a()
 
# def a():
#   a=[1,2,3,4,5]
#   b=len(a)
#   i=0
#   while i<b:
#     print(a[i])
#     i=i+1
# a()

# multiplication of each element
# def a():
# n=input("enter any number")
# b=1
# for i in (n):
#     b=b*int(i)
# print(b)
# a()

# def a():
#   n=input("enter any number")
#   i=1 
#   while i<=3:
#     b=b*int(i)
#     i=i+1
#   print(b)
# a()

# multiplication table of a given number
# def b():
#   a=int(input("enter any number"))
#   for i in range(1,11):
#     print(a,"*",i,"=",i*a)
# b()

# def b():
#   a=3
#   i=1
#   while i<11:
#     print(a,"*",i,"=",a*i)
#     i=i+1
# b()

# reverse a list
# def a():
#     a=[1,2,3,4,5]
#     rev=[]
#     for i in (a):
#         rev=[i]+rev
#     print(rev)
# a()

# def a():
#     a=[1,2,3,4,5]
#     rev=[]
#     i=1
#     while i<=5:
#         rev=[i]+rev
#         i=i+1
#     print(rev)
# a()

                # program to count the total number of digits in a number
# def a():
#     num =1234
#     count=0
#     for i in num:
#         count=(count)+i
#         print(count)
# a()

# def a():
#     num=1234
#     count=0
#     while num!=0:
#         num//=10
#         count=count+1
#     print("total num of digits: ",str(count))
# a()

#  given number is prime or not
# num = 11
#    # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n / 2
#     for i in range(2, int(num/2)+1):
#            # If num is divisible by any number between
#            # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# num = int(input("Enter a number ( greater than 1)"))  
# f = 0
# i = 2
# while i <= num / 2:
#     if num % i == 0:
#         f=1
#         break
#     i=i+1
    
# if f==0:
#     print("The entered number is a prime number")
# else:
#     print("The entered number is not a prime number")

# Python program to count the number of even and odd numbers from a series of numbers
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2:
#      count_even+=1
#     else:
#      count_odd+=1
# print("Number of even numbers :",count_even)
# print("Number of odd numbers :",count_odd)

# tuple=(10, 21, 4, 45, 66, 93, 11)
  # even_count, odd_count = 0, 0
# num = 0
   # using while loop     
# while(num < len(tuple)):
         # checking condition
#     if tuple[num] % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
     # increment num 
#     num += 1
      
# print("Even numbers : ", even_count)
# print("Odd numbers : ", odd_count)

# Python program that accepts a string and calculate the number of digits and letters
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

# Python program to check the validity of username and password input by users
# username='bipasha'
# password='123'
# for i in range(3):
#     username1=input("enter username")
#     password1=input("enter password")
#     if username==username1 and password==password1:
#         print("succesfully login")
#         break
#     else:
#         print("invalid credentials")
# print("3 attempts finished")

# username='bipasha'
# password='123'
# i=1
# while i<5:
#     username1=input("enter username")
#     password1=input("enter password")
#     if username==username1 and password==password1:
#         print("succesfully login")
#         break
#     else:
#         print("invalid credentials")
# print("3 attempts finished")


# program to print the given number is odd or even
# def a():
#     num = int(input("Enter any number to test whether it is odd or even: "))

#     if (num % 2) == 0:

#         print("The number is even")

#     else:

#      print ("The provided number is odd")
# a()

# num=int(input("enter any number"))
# i=1
# while i<:
#     print()


# factorial of a given number
# def a():
#     # factorial=1
#     # for i in range(1,6):
#     #     factorial=factorial*i
#     # print(factorial)
# a()

# def a():
#     factorial=1
#     i=1
#     while i<=5:
#         factorial=factorial*i
#     print(factorial)
# a()


# program to check given number is palindrome or not
# def b():
#     # a="madam"
#     # reverse=""
#     # for i in a:
#     #     reverse=i+reverse
#     # if reverse == a:
#     #     print("palindrome")
#     # else:
#     #     print("not palindrome")
# b()

# program to check given number is armstrong or not
# def a():
#     # num=1634
#     # order=len(str(num))
#     # sum=0
#     # temp=num
#     # while temp>0:
#     #     digit=temp%10
#     #     sum+=digit**order
#     #     temp//=0
#     #     if num==sum:
#     #         print(num,"is an armstrong")
#     #     else:
#     #         print(num,"is not an armstrong")
# a()

# database;;;;;;;

from tkinter import *
import sqlite3

root=Tk()
# root.title('Database Address Book')
# conn=sqlite3.connect('address_book.db')
# c=conn.cursor()

# c.execute("""CREATE TABLE addresses(
#   first_name text,
#   last_name text,
#   address text,
#   city text,
#   state text,
#   zipcode integer
#   )""")
# print("Table created succesfully")
def submit():
  conn=sqlite3.connect('address_book.db')
  c=conn.cursor()
  c.execute("INSERT INTO addresses values(:f_name, :l_name, :address, :city, :state, :zipcode)",{
    'f_name':f_name.get(),
    'l_name':l_name.get(),
    'address':address.get(),
    'city':city.get(),
    'state':state.get(),
    'zipcode':zipcode.get()
  
    })

  conn.commit()
  conn.close()


  f_name.delete(0,END)
  l_name.delete(0,END)
  address.delete(0,END)
  city.delete(0,END)
  state.delete(0,END)
  zipcode.delete(0,END)

def query():
  conn=sqlite3.connect('address_book.db')
  c=conn.cursor()
  c.execute("SELECT *, oid FROM addresses")
  records=c.fetchall()
  print(records)
  print_record=''
  for record in records:
    print_record+=str(record[0]) + str(record[1])+ ''+'\t'+str(record[6])+"\n"
  query_label=Label(root,text=print_record)
  query_label.grid(row=8,column=0,columnspan=2)

def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    print("Deleted Succesfully")

    conn.commit()
    conn.close()
# query lai execute garna cursor method le help garxa

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

submit_btn=Button(root,text="Add Records",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=1,ipadx=100)

# create query button

query_btn=Button(root,text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

delete_box=Entry(root,width=30)
delete_box.grid(row=8,column=1,pady=5)

delete_box_label=Label(root,text="Delete ID")
delete_box_label.grid(row=8,column=0,pady=5)

delete_btn=Button(root,text="Delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=120)



def edit():
  global editor
  editor=Tk()
  editor.title('Update data')
  editor.geometry("300x480")

  conn=sqlite3.connect('address_book.db')
  c=conn.cursor()
  record_id=delete_box.get()
  c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
  records=c.fetchall()



# create a update button


# create textboxes

  global f_name_editor
  global l_name_editor
  global address_editor
  global city_editor
  global state_editor
  global zipcode_editor


  f_name_editor=Entry(editor,width=30)
  f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
  l_name_editor=Entry(editor,width=30)
  l_name_editor.grid(row=1,column=1)

  address_editor=Entry(editor,width=30)
  address_editor.grid(row=2,column=1)

  city_editor=Entry(editor,width=30)
  city_editor.grid(row=3,column=1)

  state_editor=Entry(editor,width=30)
  state_editor.grid(row=3,column=1)

  zipcode_editor=Entry(editor,width=30)
  zipcode_editor.grid(row=4,column=1)

# create textboxes label
  f_name_label=Label(editor,text="First name")
  f_name_label.grid(row=0,column=0,pady=(10,0))

  l_name_label=Label(editor,text="Last name")
  l_name_label.grid(row=1,column=0)

  address_label=Label(editor,text="Address")
  address_label.grid(row=2,column=0)

  city_label=Label(editor,text="City")
  city_label.grid(row=3,column=0)

  state_label=Label(editor,text="State")
  state_label.grid(row=3,column=0)

  zipcode_label=Label(editor,text="Zip code")
  zipcode_label.grid(row=4,column=0)

# edit_btn=Button(root,text="Update",command=edit)
# edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

  for record in records:
    f_name_editor.insert(0,record[0])
    l_name_editor.insert(0,record[1])
    address_editor.insert(0,record[2])
    city_editor.insert(0,record[3])
    state_editor.insert(0,record[4])
    zipcode_editor.insert(0,record[5])

  # conn.commit()
  # conn.close()

  edit_btn=Button(editor,text="Save",command=query)
  edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)
  conn.commit()
  conn.close()
# records ko data record maa auxa
# fetchall : all record
edit_btn=Button(root,text="Update",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=120)



def update():
  conn=sqlite3.connect('address_book.db')
  c=conn.cursor
  record_id=delete_box.get()
  c.execute("""UPDATE addresses SET
    first_name=:first,
    last_name=:last,
    address=:address,
    city=:city,
    state=:state,
    zipcode=:zipcode
    WHERE OID=:oid""",
    {'first':f_name_editor.get(),
    'last':l_name_editor.get(),
    'address':address_editor.get(),
    'city':city_editor.get(),
    'state':state_editor.get(),
    'zipcode':zipcode_editor.get(),
    'oid':record_id
      }
  )
  conn.commit()
  conn.close()
edit_btn=Button(editor,text="Save",command=update)
edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)



# conn.commit()
# conn.close()



root.mainloop()