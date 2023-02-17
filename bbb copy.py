
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

# ----------------------------------------------------------------------

# list=["bipasha","sila","hii"]
# for i in list:
#   print(i,end=' ')

# data=["Rosh","sii","hi"]
# print(data[1])   using indexing

# data=["hi","si","li"]
# print(data[0:1])

# data=list(range(0,10,1))
# print(data)

# data=["sunil","bi",20]
# print(data)
# data.append(9)
# data.append("programming")
# data.append([1,2])
# print(data)

# data=["hi","pa"]
# print(data)
# data.extend([10,8])
# print(data)

# data=["paa","hhaha","ha"]
# data.insert(3,"funny")
# print(data)

# mixed_list=[{1,2},[5,6,7],{"a":"r"}]
# number_tuple=(3,4)
# # inseting a tuple to the list
# mixed_list.insert(1,number_tuple)
# print("updated list: ",mixed_list)

# updating the elements of the list
# data=["haha","hi",20]
# print(data)
# data[0]=1
# data[1]=2
# data[2]=100
# print(data)

# data=["hi","pp",90]
# print(data)
# del data[2]
# print(data)

# data=["hi","pp",90]
# print(data)
# data.remove(90)
# print(data)

# data=["hi","pp",90]
# print(data)
# data.pop() 
                       # pop le last ko element lai delete garxa
# print(data)

# data=["sun","ros",90]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)

# data=["hi","si"]
# data.clear()
# print(data)

# tuple=(1,2,3,4)               turning tuple into list and then adding 5 to the tuple
# print(tuple) 
# data=list(tuple)
# data.insert(4,5)
# print(data)

# data=("sun","h",9)       tuple
# print(data)

# data=("sum","hi",9)
# print(data[0])

# data=("sum","hi",9)
# print(data[0:1])


# a=[1,2,3,1,1,4,1,1,1,1]
# b=[]
# for i in range(len(a)):
#   if a[i]==1:
#     b.append(i)         append use gareko le b ko empty set ma gayera add garxaa    
# print(b)

# set ma accending order ma value auxa

# dubai ko match nabhako value auxa in symmetric difference

# {}-dictionary
# {1,2,3}-set
# extend ma integer pass garna paune bho

# a={1,2,3,4}
# a.add((5,6))
# print(a)

# pop le set ma first ko element hatauxa
# discard bata nabhako element hatauna khojyo bhane error audeina but remove bata chai error auxa.

# a={"hawa","sii","kk"}
# # a.discard("khi")
# a.remove("khi")
# print(a)

# a={1,2,3,"hi","si"}
# print(dir(a))
# if "hi" in a:
#   print('present')
# else:
#   print('not present')

# a={1,2,3,4}
# a.clear()
# print(a)

# a={1,2,3,4}
# a2=[]
# a2=a.copy
# print(a)

# a={'a','n'}
# b={'c','d'}
# a.update(b)
# print(a)    random ma auxa set ma

# a={1,2,3,4}
# b={3,4,5,6}
# union_set= a|b
# union_set= a^b
# print(union_set)

# Write a Python program to get the smallest number from a list.
# list=[1,2,3,4,5,0]
# print("smallest element is: ",min(list))

# Write a Python function to check a list is empty or not.
# list=[1]
# if not list:
#   print('empty list')
# else:
#   print('not empty list')

# Write a Python program to select an item randomly from a list.
# import random
# list=['hi','si','ki']
# print(random.choice(list))

# Write a Python program to copy a list.
# list=[1,2,3,4]
# list1=list.copy()
# print('list:',list)
# print('list1:',list1)

# Write a Python program to find the 2nd largest number in a list.
# list=[1,2,3,4,5]
 
# # new_list is a set of list1
# new_list = set(list)
 
# # Removing the largest element from temp list
# new_list.remove(max(new_list))
 
# # Elements in original list are not changed
# # print(list1)
# print(max(new_list))

# Write a Python program to print a specified list after removing the 3rd elements.
# list=[1,2,'hi','ki']
# # list.remove('hi')
# print(list)

# Write a Python program to count the number of even and odd numbers from a series of numbers.
# using Bitwise OR
 
# list of numbers
# list1 = [10, 21, 4, 45, 66, 93, 1]
 
# even_count, odd_count = 0, 0
# for num in list1:
       
#     # checking condition
#     if num | 1 > num:
#         even_count += 1
   
#     else:
#         odd_count += 1
           
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

# program to add an item in tuple
# tuple=(1,2,'hi','si')
# tuple=tuple+(60,)
# print(tuple)

# Write a Python program to convert tuple to list.
# tuple=(1,2,3,4,5,"hi")
# data=list(tuple)
# print(data)

# to convert a tuple to string.

# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str =  ''.join(tup)
# print(str)

# write a Python program to convert a list to a tuple.
# list=[1,2,3]
# list1=tuple(list)
# print(list1)

# Write a Python program to find the 3nd largest number in a list.
# list1 = [20,63,32,54,89,10] 
 
# #This statement sorts list1 in ascending order 
# print(sorted(list1))  
# # output - [10, 20, 32, 54, 63, 89] 
# #This statement prints third largest number from list1 
# print(sorted(list1)[-3]) 

# Write a Python program to create a set.
# set1 = set("GeeksForGeeks")
# print("\nSet with the use of String: ")
# print(set1)

# Creating a set using string
# test_set = set("geEks")
 
# # Iterating using for loop
# for val in test_set:
#     print(val)

# Write a Python program to add member(s) in a set.
# set of letters
# GEEK = {'g', 'e', 'k'}
 
# # adding 's'
# GEEK.add('s')
# print("Letters are:", GEEK)
 
# # adding 's' again
# GEEK.add('s')
# print("Letters are:", GEEK)

# to remove items for set
# num_set = set([0, 1, 3, 4, 5])
# print("Original set:")
# print(num_set)
# num_set.pop()
# print("\nAfter removing the first element from the said set:")
# print(num_set)

# Write a Python program to create an intersection of sets. 
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# print("Original set elements:")
# print(setx)
# print(sety)
# print("\nIntersection of two said sets:")
# setz = setx & sety
# print(setz)


# my_dict={}
# my_dict={1:'apple',2:'ball'}
# my_dict={'name':'john' ,1 : [2, 4, 3]}
# my_dict=dict({1:'apple',2:'ball'})
# my_dict =dict([(1,'apple'),(2,'ball'),(3,'umbrella')])
# print(my_dict)

# data={'name':'sunil','age':17}
# print(data)

# data1=dict(name='sunil rawat',age=12)
# print(data1)

# data={'name':'sunil rawat','age':17}
# print(data)
# for i in data:
#   print(i)

# for i in data.values():
#   print(i)

# for i in data.items():
#   print(i)

# access value using key
# data={'name':'sunil','age':1}
# print(data['name'])
# print(data['age'])

# updating
# a={1:'a',2:'b'}
# b={3:'c'}
# a.update(b)
# print(a)

# get ma none falxa
# dictionary ma indexing garna paudaina



# data={}
# print(data)
# data['name']='sunil'
# data['age']=20
# print(data)

# data={'name':'sunil rawat','age':20}
# if 'name' in data:
#   print('present')
# else:
#   print('not present')
# if 'sunil rawat' in data.values():
#   print('present')
# else:
#   print('not present')

# data={'name':'sunil','age':2}
# del data['name']
# print(data)

# data={'name':'danish','age':2}
# print(data)
# data=data.pop('age')
# # data=data.get('name')
# # print(data)




# # pop item ma argument dina mildaina


# # a_dict={"a":1,"b":2,"c":3}
# # new_key="A"
# # old_key="a"
# # a_dict[new_key]=a_dict.pop(old_key)
# # print(a_dict)


# # this_dict= {
# #   "brand":"ford",
# #   "model":"mustang",
# #   "year":1964
# # }
# # print(this_dict)
# # this_dict["year"]=2018
# # print(this_dict)

# # print("study tonight",end=" ")
# # print("b")

# # class pokemon:
# #   def __init__(self,name,Type,health):
# #     print(f'Pokemon {name} of type {Type} has been created')
# #     print(f'health:{health}')
# #   __init__("Pokemon","pikachu","electric type",100)

# # list1=[0,2,5,1,7]
# # str1="7"
# # for i in list1:
# #   str1=int(str1)+1
# # print(str1)  


# from _ast import Lambda
# from tkinter import *
#  # # yeuta matra expression ma kam garna paryo bhane lamda use garne
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

# def button_substract():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)

# def button_multiply():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)


# def button_equal():
#   second_number=e.get()
#   e.delete(0,END)
#   e.insert(0,f_num-int(second_number))

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
# button_substract=Button(root,text='-',padx=39,pady=20,command=button_substract)
# button_add=Button(root,text='+',padx=39,pady=20,command=button_add)
# button_multiply=Button(root,text='*',padx=39,pady=20,command=button_multiply)

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
# button_substract.grid(row=6,column=0)
# button_multiply.grid(row=7,column=0)


# button_equal.grid(row=5,column=1,columnspan=2)

# root.mainloop()

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

# def button_multiply():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)

# def button_equal():
#   second_number=e.get()
#   e.delete(0,END)
#   e.insert(0,f_num*int(second_number))

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
# button_multiply=Button(root,text='*',padx=39,pady=20,command=button_multiply)
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
# button_multiply.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)
# root.mainloop()

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
#   e.insert(0,f_num/int(second_number))

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
# button_divide=Button(root,text='/',padx=39,pady=20,command=button_divide)
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
# button_divide.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)
# root.mainloop()

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

# ----------------------------------------------------------------------

# list=["bipasha","sila","hii"]
# for i in list:
#   print(i,end=' ')

# data=["Rosh","sii","hi"]
# print(data[1])   using indexing

# data=["hi","si","li"]
# print(data[0:1])

# data=list(range(0,10,1))
# print(data)

# data=["sunil","bi",20]
# print(data)
# data.append(9)
# data.append("programming")
# data.append([1,2])
# print(data)

# data=["hi","pa"]
# print(data)
# data.extend([10,8])
# print(data)

# data=["paa","hhaha","ha"]
# data.insert(3,"funny")
# print(data)

# mixed_list=[{1,2},[5,6,7],{"a":"r"}]
# number_tuple=(3,4)
# # inseting a tuple to the list
# mixed_list.insert(1,number_tuple)
# print("updated list: ",mixed_list)

# updating the elements of the list
# data=["haha","hi",20]
# print(data)
# data[0]=1
# data[1]=2
# data[2]=100
# print(data)

# data=["hi","pp",90]
# print(data)
# del data[2]
# print(data)

# data=["hi","pp",90]
# print(data)
# data.remove(90)
# print(data)

# data=["hi","pp",90]
# print(data)
# data.pop() 
                       # pop le last ko element lai delete garxa
# print(data)

# data=["sun","ros",90]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)

# data=["hi","si"]
# data.clear()
# print(data)

# tuple=(1,2,3,4)               turning tuple into list and then adding 5 to the tuple
# print(tuple) 
# data=list(tuple)
# data.insert(4,5)
# print(data)

# data=("sun","h",9)       tuple
# print(data)

# data=("sum","hi",9)
# print(data[0])

# data=("sum","hi",9)
# print(data[0:1])


# a=[1,2,3,1,1,4,1,1,1,1]
# b=[]
# for i in range(len(a)):
#   if a[i]==1:
#     b.append(i)         append use gareko le b ko empty set ma gayera add garxaa    
# print(b)

# set ma accending order ma value auxa

# dubai ko match nabhako value auxa in symmetric difference

# {}-dictionary
# {1,2,3}-set
# extend ma integer pass garna paune bho

# a={1,2,3,4}
# a.add((5,6))
# print(a)

# pop le set ma first ko element hatauxa
# discard bata nabhako element hatauna khojyo bhane error audeina but remove bata chai error auxa.

# a={"hawa","sii","kk"}
# # a.discard("khi")
# a.remove("khi")
# print(a)

# a={1,2,3,"hi","si"}
# print(dir(a))
# if "hi" in a:
#   print('present')
# else:
#   print('not present')

# a={1,2,3,4}
# a.clear()
# print(a)

# a={1,2,3,4}
# a2=[]
# a2=a.copy
# print(a)

# a={'a','n'}
# b={'c','d'}
# a.update(b)
# print(a)    random ma auxa set ma

# a={1,2,3,4}
# b={3,4,5,6}
# union_set= a|b
# union_set= a^b
# print(union_set)

# Write a Python program to get the smallest number from a list.
# list=[1,2,3,4,5,0]
# print("smallest element is: ",min(list))

# Write a Python function to check a list is empty or not.
# list=[1]
# if not list:
#   print('empty list')
# else:
#   print('not empty list')

# Write a Python program to select an item randomly from a list.
# import random
# list=['hi','si','ki']
# print(random.choice(list))

# Write a Python program to copy a list.
# list=[1,2,3,4]
# list1=list.copy()
# print('list:',list)
# print('list1:',list1)

# Write a Python program to find the 2nd largest number in a list.
# list=[1,2,3,4,5]
 
# # new_list is a set of list1
# new_list = set(list)
 
# # Removing the largest element from temp list
# new_list.remove(max(new_list))
 
# # Elements in original list are not changed
# # print(list1)
# print(max(new_list))

# Write a Python program to print a specified list after removing the 3rd elements.
# list=[1,2,'hi','ki']
# # list.remove('hi')
# print(list)

# Write a Python program to count the number of even and odd numbers from a series of numbers.
# using Bitwise OR
 
# list of numbers
# list1 = [10, 21, 4, 45, 66, 93, 1]
 
# even_count, odd_count = 0, 0
# for num in list1:
       
#     # checking condition
#     if num | 1 > num:
#         even_count += 1
   
#     else:
#         odd_count += 1
           
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

# program to add an item in tuple
# tuple=(1,2,'hi','si')
# tuple=tuple+(60,)
# print(tuple)

# Write a Python program to convert tuple to list.
# tuple=(1,2,3,4,5,"hi")
# data=list(tuple)
# print(data)

# to convert a tuple to string.

# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str =  ''.join(tup)
# print(str)

# write a Python program to convert a list to a tuple.
# list=[1,2,3]
# list1=tuple(list)
# print(list1)

# Write a Python program to find the 3nd largest number in a list.
# list1 = [20,63,32,54,89,10] 
 
# #This statement sorts list1 in ascending order 
# print(sorted(list1))  
# # output - [10, 20, 32, 54, 63, 89] 
# #This statement prints third largest number from list1 
# print(sorted(list1)[-3]) 

# Write a Python program to create a set.
# set1 = set("GeeksForGeeks")
# print("\nSet with the use of String: ")
# print(set1)

# Creating a set using string
# test_set = set("geEks")
 
# # Iterating using for loop
# for val in test_set:
#     print(val)

# Write a Python program to add member(s) in a set.
# set of letters
# GEEK = {'g', 'e', 'k'}
 
# # adding 's'
# GEEK.add('s')
# print("Letters are:", GEEK)
 
# # adding 's' again
# GEEK.add('s')
# print("Letters are:", GEEK)

# to remove items for set
# num_set = set([0, 1, 3, 4, 5])
# print("Original set:")
# print(num_set)
# num_set.pop()
# print("\nAfter removing the first element from the said set:")
# print(num_set)

# Write a Python program to create an intersection of sets. 
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# print("Original set elements:")
# print(setx)
# print(sety)
# print("\nIntersection of two said sets:")
# setz = setx & sety
# print(setz)


# my_dict={}
# my_dict={1:'apple',2:'ball'}
# my_dict={'name':'john' ,1 : [2, 4, 3]}
# my_dict=dict({1:'apple',2:'ball'})
# my_dict =dict([(1,'apple'),(2,'ball'),(3,'umbrella')])
# print(my_dict)

# data={'name':'sunil','age':17}
# print(data)

# data1=dict(name='sunil rawat',age=12)
# print(data1)

# data={'name':'sunil rawat','age':17}
# print(data)
# for i in data:
#   print(i)

# for i in data.values():
#   print(i)

# for i in data.items():
#   print(i)

# access value using key
# data={'name':'sunil','age':1}
# print(data['name'])
# print(data['age'])

# updating
# a={1:'a',2:'b'}
# b={3:'c'}
# a.update(b)
# print(a)

# get ma none falxa
# dictionary ma indexing garna paudaina



# data={}
# print(data)
# data['name']='sunil'
# data['age']=20
# print(data)

# data={'name':'sunil rawat','age':20}
# if 'name' in data:
#   print('present')
# else:
#   print('not present')
# if 'sunil rawat' in data.values():
#   print('present')
# else:
#   print('not present')

# data={'name':'sunil','age':2}
# del data['name']
# print(data)

# data={'name':'danish','age':2}
# print(data)
# data=data.pop('age')
# data=data.get('name')
# print(data)




# pop item ma argument dina mildaina


# a_dict={"a":1,"b":2,"c":3}
# new_key="A"
# old_key="a"
# a_dict[new_key]=a_dict.pop(old_key)
# print(a_dict)


# this_dict= {
#   "brand":"ford",
#   "model":"mustang",
#   "year":1964
# }
# print(this_dict)
# this_dict["year"]=2018
# print(this_dict)

# print("study tonight",end=" ")
# print("b")

# class pokemon:
#   def __init__(self,name,Type,health):
#     print(f'Pokemon {name} of type {Type} has been created')
#     print(f'health:{health}')
#   __init__("Pokemon","pikachu","electric type",100)

# list1=[0,2,5,1,7]
# str1="7"
# for i in list1:
#   str1=int(str1)+1
# print(str1)  


# from _ast import Lambda
# from tkinter import *
#  # # yeuta matra expression ma kam garna paryo bhane lamda use garne
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

# def button_substract():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)

# def button_multiply():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)


# def button_equal():
#   second_number=e.get()
#   e.delete(0,END)
#   e.insert(0,f_num-int(second_number))

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
# button_substract=Button(root,text='-',padx=39,pady=20,command=button_substract)
# button_add=Button(root,text='+',padx=39,pady=20,command=button_add)
# button_multiply=Button(root,text='*',padx=39,pady=20,command=button_multiply)

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
# button_substract.grid(row=6,column=0)
# button_multiply.grid(row=7,column=0)


# button_equal.grid(row=5,column=1,columnspan=2)

# root.mainloop()

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

# def button_multiply():
#   first_number=e.get()
#   global f_num
#   f_num=int(first_number)
#   e.delete(0,END)

# def button_equal():
#   second_number=e.get()
#   e.delete(0,END)
#   e.insert(0,f_num*int(second_number))

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
# button_multiply=Button(root,text='*',padx=39,pady=20,command=button_multiply)
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
# button_multiply.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)
# root.mainloop()

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
#   e.insert(0,f_num/int(second_number))

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
# button_divide=Button(root,text='/',padx=39,pady=20,command=button_divide)
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
# button_divide.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)
# root.mainloop()


# fibonacci number

n=int(input("Enter number: "))
x=0
y=1
z=0
while(z<=n):
  print(z)
  x=y
  y=z
  z=x+y

# recursionfunction
def fact(num):
  """This function call itself to find the factorial of a number"""
  if num==1:
    return 1
  else:
    return(num*fact(num-1))
num=5
print("Factorial of ",num,"is: ",fact(num))

# def a(num):
#   if num==1:
#     return 1
#   else:
#     return(num+fact(num))
# num=10

# HW: REVERSE A STRING USING RECURSION