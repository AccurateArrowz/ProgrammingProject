
# marks=int(input("enter your marks : "))
# if marks<25:
#     print("F")
# elif 25<marks<45:
#     print("E")
# elif 45<marks<50:





# (1)
# Costprice=int(input("enter the cost price of the bike"))
# if Costprice>100000:
#     tax=15/100*Costprice 
# elif 50000<Costprice<100000:
#     tax=10/100*Costprice
# elif Costprice<=50000:
#     print=5/100*Costprice
# print("the amount of tax is :",tax)

# (2)
# Gita=input("enter your age")
# Sita=input("enter your age")
# Rita=input("enter your age")
# Mita=input("enter your age")
# age=min(Gita,Sita,Rita,Mita)
# print("The youngest child is :",age)

# (3)
# Ram=input("enter your age")
# Shyam=input("enter your age")
# Hari=input("enter your age")
# Pritam=input("enter your age")
# age=max(Ram,Shyam,Hari,Pritam)
# print("The oldest child is:", age)

# (4)
# Grade=int(input("enter your marks"))
# if Grade<25:
#     print("D")
# elif 25<Grade<45:
#     print("C")
# elif 45<Grade<50:
#     print("B")
# elif 50<Grade<60:
#     print("B+")
# elif 60<Grade<80:
#     print("A")
# elif Grade>80:
#     print("A+")

# (5)

# service=int(input("enter your bonus"))
# if service>10:
#     bonus=10/100*service
# elif 6<=service<=10:
#     bonus=8/100*service
# elif servive<6:
#     bonus=5/10*service
# print("your bonus is:", bonus)

# (6)
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# k=[a,b,c]
# k.sort()
# print(k)
# print(k[1])

# (7)
 
# a=int(input("enter the number of days: "))
# if a<=5:
#     k=a*2
# elif 6<a<10:
#     k=a*3
# elif 11<a<15:
#     k=a*4
# elif a>15:
#     k=a*5
# print("the charge for library :",k)

# (8)
# salary=int(input("enter your salary"))
# service=int(input("enter your year of service"))
# bonus=0
# if (service>5):
#     bonus=5/100*salary
#     print(bonus)
# else:
#     print("out of service")

# (10)
# grades=int(input("enter your grades"))
# if grades<25:
#     print("F")
# elif 25<grade<45:
# #     print('E')
# # elif 45<grade<50:
# #     print('D')
# # elif 50<grade<60:
# #     print('C')
# # elif 60<grade<80:
# #     print('B')
# # elif grade>80:
# #     print('A')


# age=int(input("enter your age; "))
# sex=(input("enter your sex; "))
# days=int(input("enter numebr of days; "))
# if (sex=='M'):
#     if 18<age<30:
#         wages=days*500
#     elif 30<age<40:
#         wages=days*600
# if (sex=='F'):
#     if 18<age<30:
#          wages=days*550
#     elif 30<age<40:
#         wages=days*6650
# print("the wages is ; ",wages)

#  loop
# a="python"
# b=len(a)
# for i in range(b):
#     print(i, "=",a[i])

# a="bipasha"
# b=len(a)
# for i in range(b):
#     print(a)

# a="bipasha"
# b=len(a)
# for i in range(b):
#     print(a[i])

# a=3
# for i in range(1,11):
#     print(a,'*',i,'=',a*i)

# a=3
# for i in range(10,0,-1):
#     print(a,'*',i,'=',a*i)

# sum=0
# a=123
# b=str(a)
# for i in b:  
#     sum=sum+int(i)
# print(sum)


# sum=1
# a=123
# b=str(a)
# for i in b:
#     sum=sum*int(i)
# print(sum)

# a="madam"
# reverse=""
# for i in a:
#     reverse=i+ reverse
# if reverse==a:
#     print("palindrome")
# else:
#     print("not palindrome")

# factorial of given number
# a=5
# factorial=1
# for i in range(1,6):
#     factorial=factorial*i
# print(factorial)


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

# num=1634
# order=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp//=0
#     if num==sum:
#         print(num,"is an armstrong")
#     else:
#         print(num,"is not an armstrong")


# for i in range(1,11):
#     print("softwarica")

# a=[1,2,3,4,5,6]   eval would be easier if we need to input data from user
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# a="hasina"
# b=len(a)
# for i in range(b):
#     print(i,"=",a[i])


# a=[1,2,3,4,5,6]
# for i in range(1,7):
#     print(i)


# factorial=1
# for i in range(1,6):
#     factorial=factorial*i
# print(factorial)


# for i in range(1,11):
#     print(a,'*',i,'=',a*i)


# n=input("enter any number")
# b=1
# for i in (n):
#     b=b*int(i)
# print(b)

# n=int(input("enter any number"))
# for i in range(1,11):
#     print("multiplication of table of")
#     for j in range(1,11):
#         print(j,'*',i,'=',i*j)


# a=[1,2,3,4,5]
# rev=[]
# for i in (a):
#     rev=[i]+rev
# print(rev)


# a=int(input("enter any number"))
# bac=1
# for i in range(1,a):
# bac=bac*i
# print(bac)

# a="Haseena"
# b="123"
# jj=""
# for i in range(1,4):
# username=input("enter your username")
# password=input("enter your password")
# if a==username and b==password:
# print("welcome ,successfully logged in")
# break
# else:
# print("invalid credentials")
# print("3 attempt is finished")

# """ p=int(input("enter any number"))
# l=0
# for i in range(1,p):
# if(i*i==p):
# l=1
# if l==1 :
# print("its perfect square")
# else :
# print("it isnot perfect square")
# """
# n=i

# a=6
# b=0
# for i in range(1,a):
#     if a%i==0:
#         sum=sum+i
# if a==sum:
#     print("perfect number")
# else:
#     print("not perfect number")

# for row in range(7):
#     for column in range(4):
#         print('*',end='')
#     print()

# for row in range(7):
#     for column in range(5):
#         if ((column==0)and(row==0)):
#             print('*',end='')

# for row in range(7):
#     for column in range(5):
#         if ((column==0) and (row!=0) or (column==1) and (row==0 or row==4) or (column==2) and (row==0 or row==4) or (column==3) and (row==0 or row==4) or (column==4) and (row!=0)):
#         print("*",end=" ")
#         else:
#         print(end="  ")
  #   print()

# for row in range(6):
#     for column in range(4):
#         if ((column==0) and (row!=0) or (column==1) and (row==0 or row==3 or row==5) or (column==2) and (row==0 or row==3 or row==5) or (column==3) and (row!=0 and row!=5)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# for row in range(6):
#     for column in range(4):
#         if ((column==0) and (row!=0) and (row!=5) or (column==1) and (row==0 or row==5) or (column==2) and (row==0 or row==5) or (column==3) and (row==0 or row==5)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# for row in range(6):
#     for column in range(4):
#         if ((column==0) or (column==1) and (row==0 or row==5) or (column==2) and (row==0 or row==5) or (column==3) and (row!=0 and row!=5) or (column==3) and (row!=0 and row!=5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()

# for row in range(5):
#   for column in range(4):
#     if ((column==0) or (row==0) or (row==2) or (row==4)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

# for row in range(5):
#   for column in range(4):
#     if ((column==0) or (row==0) or (row==2)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()
       

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) or (row!=6) or (row!=1 and column==2) and (row!=3 and row!=4) and (column==5) or (row==6)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()


#   for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2) and (column==3) and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()



#   for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()


#   for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()




#   for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()


#   for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()


  # for row in range(7):
  # for column in range(5):
  #   if ((column==0) and (row!=0) and (row!=6) or (row!=2 and column==3) (row==6 and row==5)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()

  # for row in range(7):
  # for column in range(5):
  #   if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2 and row!=3 and row!=4 and row!=5)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()

# for row in range(7):
  # for column in range(5):
  #   if ((column==0) and (row!=0) and (row==6) or (row!=5 and row==4 and row!=3) and (column=5)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=6) or (row==3 and row==4 and row==5)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=6) or (row==1 and column==2) (row!=3 and row!=4)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

  # for row in range(7):
  # for column in range(5):
  #   if ((column==0) and (row!=0) and (row!=6) or (row!=1 and row!=2)  (row==4 and row!=5)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) and (row!=4) or (column==1 and row!=2) and (row!=3 and row!=4) and (column==5) or row==6)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

# for row in range(7):
#   for column in range(5):
#     if ((column==0) and (row!=0) or (row!=6) or (row!=1 and column==2) and (row!=3 and row!=4) and (column==5) or (row==6)):
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

  # for row in range(7):
  #   for column in range(5):
  #    if ((column==0) and (row!=0) and (column==6) or (row!=1) and (column==4) and (row!=3 and row!=6 and row!=2)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()

  # # for row in range(7):
  #   for column in range(5):
  #    if ((column==0) and (row!=6) or (row!=1 and row!=2 and row!=3) or (row!=6 and row!=7)):
  #     print('*',end='  ')
  #   else:
  #     print(end=' ')
  # print()


# printing your name
# for row in range(6):
#     for column in range(4):
#         if ((column==0) and (row!=0) or (column==1) and (row==0 or row==3 or row==5) or (column==2) and (row==0 or row==3 or row==5) or (column==3) and (row!=0 and row!=5)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# for row in range(5):
#   for column in range(5):
#     if ((column==0 and row!=0) 
#       print('*',end='  ')
#     else:
#       print(end=' ')
#   print()

# a='python'
# i=0
# while i<10:
#   print(a)
#   i=i+1


# a='python'
# b=len(a)
# i=0
# while i<b:
#   print(i,'=',a[i])
#   i=i+1


# a=[1,2,3,4,5,6]
# b=len(a)
# i=0
# sum=0
# while i<b:
#   sum=sum+a[i]
#   i=i+1
# print(sum)

# a=10
# i=0
# while i<10:
#   if i==3:
#     break
#   print(i)
#   i=i+1

# a=10
# i=0
# while i<10:
#   i=i+1
#   if i==2:
#     continue
#   print(i)

# i=1
# while i<=10:
#   print("multiplication of table of : ",i)
#   j=1
#   while j<=10:
#      i=i+1
#      j=j+1
#      print(i,'*',i,'=',i*j)
  

# num=1634
# order=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp//=0
#     if num==sum:
#         print(num,"is an armstrong")
#     else:
#         print(num,"is not an armstrong")
# def add():
#   x=10
#   y=20
#   z=30
#   ans=x+y+z
#   print("the sum is", ans)
# add()


# def add(*num,**akk):
#   print(num)
#   print(akk)
# add(1,2,3,4,a=5,b=6,c=7,d=8)


# with argument and with return type
# def add(x,y):
#   return(x+y)
# print(add(10,20)) 


# from math import pi
# pi=20
# def sum():
#   pi=30
#   def add():
#     pi=40
#     print(pi)
#   add()
# sum()





# import time
# strt_time=time.time()
# x=lambda x:x+2
# print(x(20))
# print


# li=[1,2,3,4]      typecasting list
# x=list(map(lambda x:x+2,li))   
# print(x)


# li=[1,2,3,4]
# x=functools.reduce(lambda x,y=x+y)
# print(x)

# li=[1,2,3,4]
# filter(lambda x:x%2==0)


# def add(a,b)
#    return a+b
# If name == ‘  main  ’:
#   print(add(10,20))
#   print("Hi")


# import math
# ceil fabs floor sqrt pow

# Random()
# uniform()
# randint()
# randrange()
# shuffle()
# choice()
# Math modules
# Module

# W3 school


# root.title("Login".center(400))
# root.configure(bg="red")


# bln=''
# root.title(80*bln+" ")


# from tkinter import *
# win=Tk()
# win.title("System")
# win.iconbitmap('icon.')
# win.geometry('600*300')
# win.mainloop()


# (11)
# sal=int(input("enter your salary"))
# if(sal<20000):
#     tax=15/100*sal

# elif(50000>sal<20000):
#     tax=25/100*sal

# elif(sal>100000):
#     tax=35/100*sal
# print("its your tax :" , tax)

# (1)
# a=50
# b=40
# if a==b:
#     print("1")
# elif a>b: 
#     print("2")
# else:
#     print("3")

# (2)
# a=10
# b=10
# if a==b:
#     print("hello")
# if a==b:
#     print("hello")


# (3)
# a=20
# b=20
# if a==b:
#     print("Hello")
# elif a==b:
#     print("Hello")

 
# (4)

# num=float(input("Enter a number: "))
# if num>0:
#     print("true")
# elif num==0: 
#     print("zero")
# else:
#     print("false")

# (5)
# num=int(input("enter any number to test whether it is odd or even"))
# if (num %2) == 0 :
#     print("the number is even")
# else:
#     print("the provided number is odd")

# (6)
# marks=int(input("enter the marks: "))
# if marks>70:
#     print("distinction")
# elif marks>60:
#     print("first")
# elif marks>40:
#     print("pass")
# else:
#     print("fail")

# (7)

# output  =int(input("apple: "))
# if output



# (8)
# name=input("what is your  name?: ")
# age=input("what is your age?: ")
# address=input("where is your address?: ")
# print("my name is " + name)
# print("my age is "+age)
# print("my address is "+address)

# (9)

# radius = float(input ("the radius of the circle : "))
# print ("The area of the circle with radius " + str(radius) + " is: " + str("pi * radius**2"))

# (10)
# a=int(input())
# b=int(input())
# c=int(input())
# print(a//2+b//2+c//2+a%2+b%2+c%2)

# (12)
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
# smallest=0
# if a < b and a < c :
#     smallest = a
# elif b < c :
#     smallest = b
# else :
#     smallest = c

# print(smallest, "is the smallest of three numbers.")

#(15)

# num=int(input("enter the number: "))
# if num==1:
#     print("january")
# elif num==2:
#     print("febraury")
# elif num==3:
#     print("march")
# elif num==4:
#     print("april")
# elif num==5:
#     print("may")
# elif num==6:
#     print("june")
# elif num==7:
#     print("july")
# elif num==8:
#     print("august")
# elif num==9:
#     print("september")
# elif num==10:
#     print("october")
# elif num==11:
#     print("november")
# elif num==12:
#     print("december")
# else:
#     print("the number is invalid")

# (16)

# x=5
# x+=3
# print("x")

# (17)
# grade=int(input("enter your marks: "))
# if grade<25:
#     print('F')
# elif 25<grade<45:
#     print('E')
# elif 45<grade<50:
#     print('D')
# elif 50<grade<60:
#     print('C')
# elif 60<grade<80:
#     print('B')
# elif grade>80:
#     print('A')

# (18)

# person1 = eval(input("Enter age of person 1 : "))
# person2 = eval(input("Enter age of person 2 : "))
# person3 = eval(input("Enter age of person 3 : "))

# if person1 > person2 and person1 > person3:
#     print("Person 1 is oldest")
# elif person2 > person1 and person2 > person3:
#     print("Person 2 is oldest")
# elif person3 > person1 and person3 > person2:
#     print("Person 3 is oldest")

# if person1 < person2 and person1 < person3:
#     print("Person 1 is youngest")
# elif person2 < person1 and person2 < person3:
#     print("Person 2 is youngest")
# elif person3 < person1 and person3 < person2:
#     print("Person 3 is youngest")

# (19)
# age=int(input("enter your age : "))
# if age>=18:
#     print("eligible for voting")
# else:
#     print("not eligible for voting")

# (24)
# if (condition):
#     statement

# (21)
# city=input("enter your city : ")
# if city=="delhi":
#     print("red fort")
# elif city=="agra":
#     print("taj mahal")
# elif city=="jaipur":
#     print("jal mahal")
# else:
#     print("enter the valid city")

# (35)
# num1=int(input("enter first number : "))
# num2=int(input("enter second number : "))
# num3=int(input("enter your third number : "))

# largest=0
# smallest=0

# #find largest number
# if num1>num2 and num1>num3:
#     largest=num1
# elif num2>num1 and num2>num3:
#     largest=num2
# else:
#     largest=num3

# #find smallest number
# if num1<num2 and num1<num3:
#     smallest=num1
# elif num2<num1 and num2<num3:
#     smallest=num2
# else:
#     smallest=num3

# secondlargest=num1+num2+num3-(largest+smallest)
# print("the second largest number:",secondlargest)

# (36)
# days=int(input("enter the number of days : "))
# if days==5:
#     print("Rs 2/day")
# elif 6<days>10:
#     print("Rs 3/day")
# elif 11<days<15:
#     print("Rs 4/day")
# elif days>15:
#     print("Rs5/day")
# else:
#     print("enter the valid days")

# (29)

# age=int(input("enter your age : "))
# if age>=60:
#     print("you are senior citizen")
# else:
#  print("you are not a senior citizen")

# (31)
# elif is the correct statement in python

# days=int(input("enter the number of days : "))
# if days==5:
#     print("Rs 2/day")
# elif 6<days<10:
#     print("Rs 3/day")
# elif 11<days<15:
#     print("Rs 4/day")
# elif days>15:
#     print("Rs5/day")
# else:
#     print("enter the valid days")


# from _ast import Lambda
# from tkinter import *
# # yeuta matra expression ma kam garna paryo bhane lamda use garne
# root=Tk()
# root.title("simple calculator")
# e=Entry(root,width=35,borderwidth=5)
# e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# def button_click(number):
#   current = e.get()
#   e.delete(0,END)
#   e.insert(0,str(current)+str(number))

# def button_clear():
#   e.delete(0,END)

# def button_add():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)

# def button_equal():
#   second_number=e.get()
#   e.delete(0,END)
#   e.insert(0,f_num+int(second_number))

# button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
# button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
# button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
# button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
# button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
# button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
# button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
# button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
# button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
# button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
# button_add=Button(root,text='+',padx=39,pady=20,command=button_add)
# button_equal=Button(root,text='=',padx=39,pady=20,command=button_equal)
# button_clear=Button(root,text='Clear',padx=39,pady=20,command=button_clear)

# button_1.grid(row=3,column=0)
# button_2.grid(row=3,column=1)
# button_3.grid(row=3,column=2)

# button_4.grid(row=2,column=0)
# button_5.grid(row=2,column=1)
# button_6.grid(row=2,column=2)
# button_7.grid(row=1,column=0)
# button_8.grid(row=1,column=1)
# button_9.grid(row=1,column=2)

# button_0.grid(row=4,column=0)
# button_clear.grid(row=4,column=1,columnspan=2)
# button_add.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)

# from tkinter import *

# root = Tk()
# root.title("Simple Calculator")

# e=Entry(root,width=35, borderwidth=5)
# e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

# def button_click(number):
# current = e.get()
# e.delete(0,END)
# e.insert(0,str(current)+str(number))

# def button_clears():
# e.delete(0,END)

# def button_addition():
# first_number=e.get()
# global f_num
# global math
# math= "addition"
# f_num = int(first_number)
# e.delete(0,END)

# def button_equals():
# sec_num=e.get()
# e.delete(0,END)
# if math=="addition":
# e.insert(0,f_num + int(sec_num))
# elif math=="subraction":
# e.insert(0,f_num - int(sec_num))
# elif math=="division":
# e.insert(0,f_num / int(sec_num))
# elif math=="multiplication":
# e.insert(0,f_num * int(sec_num))


# def button_sub():
# first_number=e.get()
# global f_num
# global math
# math= "subraction"
# f_num = int(first_number)
# e.delete(0,END)

# def button_multi():
# first_number=e.

# root.mainloop()



 

from tkinter import *
 
# globally declare the expression variable
expression = ""
 

def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light green")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("270x150")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()



# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# win=Tk()
# win.title('bipasha')
# win.configure(bg="Light yellow")
# # win.geometry('600*600')     window ko size , label bhaneko text lekhna lai
# win.minsize(width=900,height=600)   
# win.maxsize(width=1600,height=1000)
# win.iconbitmap('hotel.ico')

# # redbutton = Button(win, text = "LEFT", fg = "purple")
# # redbutton.pack(side=TOP)
# # redbutton=Button(win,text="RIGHT",fg="green")
# # redbutton.pack(side=LEFT)
# # redbutton=Button(win,text="TOP",fg="BLUE")
# # redbutton.pack(side=RIGHT)
# # redbutton=Button(win,text="BUTTOM",fg="PINK")
# # redbutton.pack(side=BOTTOM)


# # name=Label(win,text="Name").grid(row=0,column=0)
# # e=Entry(win).grid(row=0,column=1)
# # password=Label(win,text="Password").grid(row=1,column=0)
# # a=Entry(win).grid(row=1,column=1)
# # submitButton=Button(win,text="Submit").grid(row=4,column=1)

# HeadLabel=Label(win,text="ENTER YOUR DETAILS :")
# HeadLabel.place(x=-1,y=15)
# HeadLabel.configure(fg="Blue")

# name=Label(win,text="USERNAME").place(x=30,y=50)
# e=Entry(win).place(x=100,y=50)
# password=Label(win,text="PASSWORD").place(x=30,y=90)
# a=Entry(win).place(x=100,y=90)
# submitButton=Button(win,text="Submit").place(x=150,y=120)


# win.title('GUI')
# myLabel = Label (win,text="Tkinter",fg="Dark Green",font=("Arial Bold",17),bg="Light pink")
# myLabel.pack()
# # mybutton=Button(win,text="Tkinter")
# # mybutton.pack()

# # def func():
# #     print("Button is clicked")
# # btn=Button(win,text="Login",command=func)
# # btn.pack(side="top")
# # widget ko border manage garnda horizontal and vertical ko lagi we use padx and pady

# def myclick():
#     myLabel=Label(win,text="Look! I clicked a button",fg="red",bg="purple",font=20)
#     myLabel.pack()
# my_button=Button(win,text="Click me",padx=10,pady=10,command=myclick,fg="red",bg="Blue")
# # my_button=Button(win,text="Click me",padx=10,pady=10,command=myclick,fg="red",bg="Blue",state=DISABLED) 
# # button le kam nagarna ko lagi disabled use garne

# e=Entry(win,width=50,bg="Blue",fg="Red",borderwidth=5,font=20)
# e.pack()
# def myclick():
#     myLabel=Label(win,text="Hello "+e.get())
#     myLabel.pack()
#     e.delete(0,END)
# btn=Button(win,text="Click me",padx=10,pady=10,command=myclick)
# btn.pack()




# # my_button.pack()

# def add():
#     x = var.get()
#     print(x)
#     Labell.config(text=x,bg="green")
# # Label1
# MyLabel=Label(win,text="user name",fg="red",bg="yellow")
# MyLabel.place(x=10,y=10)
# # Label2
# Labell=Label(win,text="Nothing",fg="red",bg="yellow")
# Labell.place(x=40,y=120)
# # entry
# var=StringVar()
# ent=Entry(win,bg="Black",fg="White",textvariable=var)
# ent.place(x=80,y=10)
# # button
# btn=Button(win,text="Submit",bg="green",fg="white",command=add)
# btn.place(x=20,y=80)


# # widget ko value change garna config use garne

# def click():
#     text1="Address: "+ mytext.get('1.0',END)
#     lbl.config(text=str(text1))
# mytext=Text(win,font=20,width=20,height=10)
# mytext.place(x=0,y=50)
# btn=Button(win,text="Click me",font=30,command=click)
# btn.place(x=400,y=300)
# lbl=Label(win,text="",font=30)
# lbl.place(x=200,y=300)

# # frame chai organised way ma rakhna laii kam lagxa
# frame=LabelFrame(win,text="This is my frame",padx=30,pady=30)
# frame.pack(padx=30,pady=30)
# b=Button(frame,text="Don't click here")
# b2=Button(frame,text="....here")
# b.grid(row=0,column=0)
# b2.grid(row=1,column=1)


# def add():
#    selection="you have selected the option :"+str(var.get())
#    l.config(text=selection)
# var=IntVar()
# r1=Radiobutton(win,text="Male",variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(win,text="Female",variable=var,value=2,command=add)
# r2.pack(anchor=W)
# l=Label(win,text="",font=40)
# l.place(x=10,y=10)



# # yek line chaiyo bhane entry widget use
# # double chaiyo bhane text widget


# # def getvals():
# #     print("your form have been submitted")
# # Label (win, text="Python Registration form",font="15 times bold").place(x=0,y=10)
# # Name=Label(win,text="Name")
# # Name.place(x=-5,y=5)

# def add():
#     label.config(text=CheckVar1.get())
# CheckVar1=IntVar()
# C1=Checkbutton(win,text="Music",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)

# C1.pack()
# btn=Button(win,text="Click",command=add)
# label=Label(win,text="")
# label.pack()
# btn.pack()

# from PIL import Image, ImageTk
# win.title("LOGIN")
# # define image
# my_image=ImageTk.PhotoImage(Image.open("z.jpg"))
# resized_image=my_image.resize(300,250)
# converted_image=ImageTk.PhotoImage(resized_image)
# my_label=Label(win,image=converted_image,width=300,height=180)
# # create a label

# yo correct garna parne xa

# my_label.pack()
# # Button quit option
# button_quit=Button(win,text="Exit",command=win.quit,width=2)
# button_quit.pack()

# from tkinter import messagebox
# def popup():
#     messagebox.showinfo("this is my popup","hello world")
# btn=Button(win,text="Popup",command=popup).pack()

# def popup():
#     response=messagebox.askyesno("this is my popup","hello world")
#     Label(win,text=response).pack()

#     if response == 1:
#         Label(win,text="clicked yes").pack()
#     else:
#         Label(win,text="Clicked No").pack()

# btn=Button(win,text="Popup",command=popup).pack()
# win.mainloop()

import turtle
b=turtle.Screen()
t=turtle.Turtle()
# t.shape("turtle")
b.bgcolor("green")
b.title("Turtle")
t.color("red","green")
t.color("red")
t.forward(100)
t.pensize(4)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
turtle.mainloop()


# import turtle
# t=turtle.Turtle()
# turtle.bgcolor("black")
# turtle.pensize(2)
# turtle.speed(0)
# while (True):
# while ko tara brek garne


















