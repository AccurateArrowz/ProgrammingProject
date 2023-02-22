from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
from PIL import ImageTk,Image


def lineBreaker(text):
    words = 0
    refactoredText = ''
    for i in text:
        refactoredText += i
        if i == ' ':
            words += 1
            if words % 22 == 0:  # break line at every multiple of 22
                refactoredText += '\n'
    # print(refactoredText)
    return refactoredText

def homePage():
    homePageWindow= Tk()
    homePageWindow.geometry('1280x1200')

    currentUser='Hari Kumar'
    currentUser_type= 'teacher'

    #CREATING THE NAVIGATION
    navigationBg = '#BE63D9'
    profileImage=PhotoImage(file='profile.png')

    def subjectsData(subjectName):
        subjectsDataWindow = Tk()
        subjectsDataWindow.geometry('1600x1000')
        subjectsDataWindow.title(subjectName)
        myNotebook = ttk.Notebook(subjectsDataWindow)
        myNotebook.pack(pady=(20, 0))

        day1Frame = Frame(myNotebook, bg='white', width=1600, height=1000)
        day1_contentLabel = Label(day1Frame, font=('x', 16), justify=LEFT, wraplength=1000, text='''

                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod quam ac venenatis sodales. Nunc interdum leo id urna sagittis imperdiet. Pellentesque semper nunc et tellus ullamcorper, a vulputate est dictum. Aenean porttitor diam urna, quis blandit nunc iaculis in. Duis eu consectetur neque. Sed egestas neque dui, non maximus diam rhoncus ac. Nulla in condimentum massa, convallis efficitur dui. Fusce molestie tincidunt lorem in interdum. Etiam ut mattis lectus, ac vehicula massa. Proin sit amet lorem at leo semper maximus vel vel neque. Donec nisl tortor, bibendum non orci vitae, pulvinar pretium ante. Donec vel commodo sapien. Duis nec tortor id mi iaculis viverra. Curabitur sit amet nunc porta, feugiat nunc at, convallis dolor. Suspendisse potenti.

                                    Integer purus enim, rhoncus hendrerit risus sit amet, vestibulum condimentum magna. Duis eget metus commodo dolor dictum aliquam lacinia vel urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce ac gravida turpis. Donec scelerisque nulla vitae ante venenatis ullamcorper. Ut iaculis molestie auctor. Phasellus in ex tortor. In scelerisque aliquam nibh vitae mollis. Nam in nisi rutrum nibh sodales congue. Integer massa libero, finibus nec venenatis ac, hendrerit a lacus. In id lectus in tellus rhoncus placerat. Vivamus mollis massa ac velit ullamcorper, vel finibus ligula congue. Nulla in massa id justo interdum auctor. Quisque at orci ut ligula molestie feugiat. Nullam porttitor eget massa ac mollis.

                                    Sed aliquam consequat rhoncus. Cras consequat nibh leo, non mattis ante gravida vel. Sed commodo magna quis justo aliquam tincidunt. Aliquam porttitor faucibus venenatis. Etiam at nisi in massa iaculis tempor. Maecenas cursus neque urna, varius iaculis ex scelerisque non. In at varius libero. Vivamus mollis, ipsum pretium ultricies gravida, enim ante posuere sem, sed imperdiet justo sem vel mauris.

                                    Quisque mollis porta neque, at bibendum est tempor vel. Curabitur tempor at velit vel aliquam. Cras gravida lorem vel purus vehicula sollicitudin. Mauris ut velit ac neque aliquet vestibulum. In dignissim orci ut placerat feugiat. Pellentesque nisi urna, ultrices ac facilisis vitae, hendrerit id nibh. Pellentesque ut velit eu ante imperdiet sodales. Nam diam quam, gravida id feugiat sed, condimentum eget quam. Nam ac risus purus. Nulla facilisi. Nullam ac aliquet lectus. Donec sodales vehicula ex, mollis convallis ante bibendum vel.

                                    Nam at sapien a felis congue blandit. Vivamus in tempus magna, ultrices rhoncus est. Duis iaculis sagittis mi nec feugiat. Nulla porta lobortis mauris vel malesuada. Curabitur sed consequat metus. Suspendisse potenti. Aenean a dignissim lectus, et euismod ligula. in massa. Donec vitae tortor quis nulla fermentum feugiat. Morbi vehicula rutrum magna non
                                    ''')
        day1_contentLabel.pack()
        day1Frame.pack(fill=BOTH, expand=TRUE)

        day2Frame = Frame(myNotebook, )
        day2_contentLabel = Label(day2Frame, font=('x', 16), justify=LEFT, wraplength=1000, text='''
                                      Sed aliquam consequat rhoncus. Cras consequat nibh leo, non mattis ante gravida vel. Sed commodo magna quis justo aliquam tincidunt. Aliquam porttitor faucibus venenatis. Etiam at nisi in massa iaculis tempor. Maecenas cursus neque urna, varius iaculis ex scelerisque non. In at varius libero. Vivamus mollis, ipsum pretium ultricies gravida, enim ante posuere sem, sed imperdiet justo sem vel mauris.

                                    Quisque mollis porta neque, at bibendum est tempor vel. Curabitur tempor at velit vel aliquam. Cras gravida lorem vel purus vehicula sollicitudin. Mauris ut velit ac neque aliquet vestibulum. In dignissim orci ut placerat feugiat. Pellentesque nisi urna, ultrices ac facilisis vitae, hendrerit id nibh. Pellentesque ut velit eu ante imperdiet sodales. Nam diam quam, gravida id feugiat sed, condimentum eget quam. Nam ac risus purus. Nulla facilisi. Nullam ac aliquet lectus. Donec sodales vehicula ex, mollis convallis ante bibendum vel.

                                    Nam at sapien a felis congue blandit. Vivamus in tempus magna, ultrices rhoncus est. Duis iaculis sagittis mi nec feugiat. Nulla porta lobortis mauris vel malesuada. Curabitur sed consequat metus. Suspendisse potenti. Aenean a dignissim lectus, et euismod ligula. in massa. Donec vitae tortor quis nulla fermentum feugiat. Morbi vehicula rutrum magna non

                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod quam ac venenatis sodales. Nunc interdum leo id urna sagittis imperdiet. Pellentesque semper nunc et tellus ullamcorper, a vulputate est dictum. Aenean porttitor diam urna, quis blandit nunc iaculis in. Duis eu consectetur neque. Sed egestas neque dui, non maximus diam rhoncus ac. Nulla in condimentum massa, convallis efficitur dui. Fusce molestie tincidunt lorem in interdum. Etiam ut mattis lectus, ac vehicula massa. Proin sit amet lorem at leo semper maximus vel vel neque. Donec nisl tortor, bibendum non orci vitae, pulvinar pretium ante. Donec vel commodo sapien. Duis nec tortor id mi iaculis viverra. Curabitur sit amet nunc porta, feugiat nunc at, convallis dolor. Suspendisse potenti.

                                    Integer purus enim, rhoncus hendrerit risus sit amet, vestibulum condimentum magna. Duis eget metus commodo dolor dictum aliquam lacinia vel urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce ac gravida turpis. Donec scelerisque nulla vitae ante venenatis ullamcorper. Ut iaculis molestie auctor. Phasellus in ex tortor. In scelerisque aliquam nibh vitae mollis. Nam in nisi rutrum nibh sodales congue. Integer massa libero, finibus nec venenatis ac, hendrerit a lacus. In id lectus in tellus rhoncus placerat. Vivamus mollis massa ac velit ullamcorper, vel finibus ligula congue. Nulla in massa id justo interdum auctor. Quisque at orci ut ligula molestie feugiat. Nullam porttitor eget massa ac mollis.

                                  ''')
        day2_contentLabel.pack()
        day2Frame.pack(fill=BOTH, expand=TRUE)

        day3Frame = Frame(myNotebook, )
        day3_contentLabel = Label(day3Frame, font=('x', 16), justify=LEFT, wraplength=1000, text='''
                                    Sed aliquam consequat rhoncus. Cras consequat nibh leo, non mattis ante gravida vel. Sed commodo magna quis justo aliquam tincidunt. Aliquam porttitor faucibus venenatis. Etiam at nisi in massa iaculis tempor. Maecenas cursus neque urna, varius iaculis ex scelerisque non. In at varius libero. Vivamus mollis, ipsum pretium ultricies gravida, enim ante posuere sem, sed imperdiet justo sem vel mauris.

                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod quam ac venenatis sodales. Nunc interdum leo id urna sagittis imperdiet. Pellentesque semper nunc et tellus ullamcorper, a vulputate est dictum. Aenean porttitor diam urna, quis blandit nunc iaculis in. Duis eu consectetur neque. Sed egestas neque dui, non maximus diam rhoncus ac. Nulla in condimentum massa, convallis efficitur dui. Fusce molestie tincidunt lorem in interdum. Etiam ut mattis lectus, ac vehicula massa. Proin sit amet lorem at leo semper maximus vel vel neque. Donec nisl tortor, bibendum non orci vitae, pulvinar pretium ante. Donec vel commodo sapien. Duis nec tortor id mi iaculis viverra. Curabitur sit amet nunc porta, feugiat nunc at, convallis dolor. Suspendisse potenti.

                                    Integer purus enim, rhoncus hendrerit risus sit amet, vestibulum condimentum magna. Duis eget metus commodo dolor dictum aliquam lacinia vel urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce ac gravida turpis. Donec scelerisque nulla vitae ante venenatis ullamcorper. Ut iaculis molestie auctor. Phasellus in ex tortor. In scelerisque aliquam nibh vitae mollis. Nam in nisi rutrum nibh sodales congue. Integer massa libero, finibus nec venenatis ac, hendrerit a lacus. In id lectus in tellus rhoncus placerat. Vivamus mollis massa ac velit ullamcorper, vel finibus ligula congue. Nulla in massa id justo interdum auctor. Quisque at orci ut ligula molestie feugiat. Nullam porttitor eget massa ac mollis.

                                    Quisque mollis porta neque, at bibendum est tempor vel. Curabitur tempor at velit vel aliquam. Cras gravida lorem vel purus vehicula sollicitudin. Mauris ut velit ac neque aliquet vestibulum. In dignissim orci ut placerat feugiat. Pellentesque nisi urna, ultrices ac facilisis vitae, hendrerit id nibh. Pellentesque ut velit eu ante imperdiet sodales. Nam diam quam, gravida id feugiat sed, condimentum eget quam. Nam ac risus purus. Nulla facilisi. Nullam ac aliquet lectus. Donec sodales vehicula ex, mollis convallis ante bibendum vel.

                                    Nam at sapien a felis congue blandit. Vivamus in tempus magna, ultrices rhoncus est. Duis iaculis sagittis mi nec feugiat. Nulla porta lobortis mauris vel malesuada. Curabitur sed consequat metus. Suspendisse potenti. Aenean a dignissim lectus, et euismod ligula. in massa. Donec vitae tortor quis nulla fermentum feugiat. Morbi vehicula rutrum magna non
                                    ''')
        day3_contentLabel.pack()
        day3Frame.pack(fill=BOTH, expand=TRUE)

        myNotebook.add(day1Frame, text='day 1')
        myNotebook.add(day2Frame, text='day 2')
        myNotebook.add(day3Frame, text='day 3')
        subjectsDataWindow.mainloop()

    def subjectPage():
        subjectPageFrame= Frame(mainFrame,bg='#FFF1F0')
        #images and making them global
        global mathsImg,programmingImg,softwareDesignImg
        mathsImg= PhotoImage(file='Mathscard.png')
        programmingImg = PhotoImage(file='Programmingcard.png')
        softwareDesignImg = PhotoImage(file='SoftwareDesignCard.png')

        mathsButton = Button (subjectPageFrame,image=mathsImg,bd=0,bg='white',command=lambda: subjectsData('Mathematics'))
        mathsButton.pack(side=LEFT,padx=(100,0))
        programmingButton = Button(subjectPageFrame, bd=0,bg='white',image=programmingImg,command=lambda: subjectsData('Programming'))
        programmingButton.pack(side=LEFT,padx=66)
        softwareDesignButton = Button(subjectPageFrame,bd=0, bg='white',image=softwareDesignImg,command=lambda: subjectsData('Software Design'))
        softwareDesignButton.pack(side=LEFT,padx=(0,100))

        subjectPageFrame.pack()
        subjectPageFrame.pack_propagate(False)
        subjectPageFrame.config(width=1280,height=640,)

    def requestPage():
        requestPageFrame= Frame(mainFrame,bg='#FFF1F0')



        # fonts,bg,images
        global newRequestButtonImage, calendarImage,editButtonImage,deleteButtonImage
        newRequestButtonImage = PhotoImage(file='Project_images/NewRequestButton.png')
        userIconImg = ImageTk.PhotoImage(Image.open('Project_images/Vector.png'))
        calendarImage = PhotoImage(file='Project_images/calendar.png')
        editButtonImage = PhotoImage(file='Project_images/EditB.png')
        deleteButtonImage = PhotoImage(file='Project_images/DeleteB.png')
        requestFrames_titleFontSize = 22
        requestFrames_descriptionFontSize = 16
        requestFrames_bg = '#B8B0F3'
        requestFrames_fg = 'black'
        edit_FrameBg = '#FFF5F1'
        edit_entryBg = '#BCC6BF'


        # connecting to db and collection
        address = "mongodb://localhost:27017"
        client = MongoClient(address)
        database = client.AppProject  # or client['AppProject']
        requestCollection = database['Requests']



        class Request:
            def __init__(self, master, id, date, title, description, sender, currentUser_type):

                # creating properties so that we can acess it later
                # arguments in constructor function can't be used elsewhere directly
                self.id = id
                self.date = date
                self.title = title
                self.description = description
                self.sender = sender
                self.currentUser_type = currentUser_type

                self.requestFrame = Frame(master, bg=requestFrames_bg, padx=56, pady=18)  #
                self.miniDateFrame = Frame(self.requestFrame, bg=requestFrames_bg)
                self.dateLabel = Label(self.miniDateFrame, text=date, bg=requestFrames_bg, fg='#4A4A4A', )
                self.dateLabel.pack(side=RIGHT, )
                self.calenderImgLabel = Label(self.miniDateFrame, image=calendarImage, bg=requestFrames_bg)  #
                self.calenderImgLabel.pack(side=RIGHT, pady=(2, 0))

                self.miniDateFrame.pack(anchor=NE)
                if currentUser_type == 'teacher':
                    self.senderLabel = Label(self.requestFrame, text='- ' + sender, bg=requestFrames_bg, fg='#4A4A4A')
                    self.senderLabel.pack(anchor=E)
                self.titleLabel = Label(self.requestFrame, text=title,
                                        font=('x', requestFrames_titleFontSize), bg=requestFrames_bg,
                                        fg=requestFrames_fg)
                self.titleLabel.pack(anchor=W)
                self.orgText = description
                self.newText = lineBreaker(self.orgText)
                self.descriptionLabel = Label(self.requestFrame, text=self.newText,
                                              font=('x', requestFrames_descriptionFontSize),
                                              bg=requestFrames_bg, fg=requestFrames_fg)
                self.descriptionLabel.pack(anchor=W)
                self.viewRepliesButton = Button(self.requestFrame, text='View Replies', fg='#13009B',
                                                bg=requestFrames_bg, command=self.chat)
                self.viewRepliesButton.pack(anchor=SE)
                self.requestFrame.pack(padx=100, pady=(40, 10), fill=X, anchor=N)  #

            def chat(self):
                chatWindow = Tk()
                chatWindow.geometry('957x404')
                marginLeftRight = 50
                chatWindow.config(bg='white')

                def clearPlaceholder(e):
                    replyEntry.config(state=NORMAL)
                    if replyEntry.get() == 'Add your reply..':
                        replyEntry.delete(0, END)

                replyEntry = Entry(chatWindow, width=600, font=('x', 16), bg='white', fg='#000000', borderwidth=.1)
                replyEntry.pack(padx=marginLeftRight, pady=(20, 0), ipady=5)
                replyEntry.insert(0, 'Add your reply..')
                replyEntry.config(state=DISABLED)
                replyEntry.bind("<Button-1>", clearPlaceholder)

                def replyFrameCreator(replier, replyMessage):

                    if replyMessage == 'Add your reply..' or replyMessage == None:
                        return
                    marginLeftRight = 50
                    replyFrame = Frame(chatWindow, padx=15, pady=10)
                    replierLabel = Label(replyFrame, text=replier, font=('x', 16), )
                    replierLabel.pack()
                    replyMessage = Label(replyFrame, text=replyMessage, font=('x', 16))
                    replyMessage.pack()
                    replyFrame.pack(padx=marginLeftRight, anchor=CENTER, pady=(10, 0))

                def reply_saver(replySender, reply):
                    replyEntry.delete(0, END)
                    # saving to db first
                    previousReplies = repliesData  # repliesData is defined below locally in this method
                    newReply = {replySender: reply}
                    previousReplies.append(newReply)
                    requestCollection.update_one({'_id': ObjectId(self.id)}, {'$set': {'replies': previousReplies}})

                    # calling replyFrameCreator to add new reply to window
                    replyFrameCreator(replySender, reply)

                sendReplyButton = Button(chatWindow, text='Send', bg='#B8B0F3', fg='white',
                                         command=lambda: reply_saver(currentUser, replyEntry.get()))
                sendReplyButton.pack(padx=marginLeftRight, anchor=E, pady=5)

                # getting previousReplies from db
                correspondingRequestData = requestCollection.find_one(
                    {'_id': ObjectId(self.id)})  # contains title,desc, replies,etc
                repliesData = correspondingRequestData['replies']  # an array containing dictionaries of replies
                for dictReplies in repliesData:  # looping inside the array
                    for key in dictReplies:
                        replyFrameCreator(key, dictReplies[key])  # key,key-value

                chatWindow.mainloop()

        if currentUser_type == 'student':
            datas = requestCollection.find({'sender': currentUser})
        elif currentUser_type == 'teacher':
            datas = requestCollection.find()

        for data in datas:
            frameObject = Request(master=requestPageFrame, id=data['_id'], date=data['date'], title=data['title'],
                                  description=data['description'], sender=data['sender'],
                                  currentUser_type=currentUser_type)
            # print(data['replies'])

        # again checking if it is student in requestPage then newRequestButton and its function will also be created
        # not combining it with above elif statement as newRequestButton should be packed last
        if currentUser_type == 'student':
            def newRequestWindow():
                # local bg
                newRequest_FrameBg = 'white'
                newRequest_entryBg = 'white'

                newRequestWindow = Tk()
                newRequestWindow.geometry('957x404')

                def send():
                    if newRequest_titleEntry.get() == '' or newRequest_descriptionText.get(1.0, END) == '':
                        return

                    # inserting to db first
                    todaysDate = datetime.datetime.today()
                    todaysDateShortened = todaysDate.strftime("%d %B,%Y")
                    newRequestData = {'title': newRequest_titleEntry.get(),
                                      'description': newRequest_descriptionText.get(1.0, END),
                                      'date': todaysDateShortened, 'sender': currentUser}
                    requestCollection.insert_one(newRequestData)

                    # inserting to the request requestPageFrame
                    newDataFromDB = requestCollection.find_one(newRequestData)  # getting id from db
                    refactored_newRequestText = lineBreaker(newRequest_descriptionText.get(1.0, END))
                    newRequestObj = Request(master=requestPageFrame, id=newDataFromDB['_id'],
                                            date=todaysDateShortened,
                                            title=newRequest_titleEntry.get(), description=refactored_newRequestText,
                                            sender=currentUser, currentUser_type=currentUser_type)
                    newRequestWindow.destroy()

                newRequestFrame = Frame(newRequestWindow, bg=newRequest_FrameBg, )
                newRequestHeading = Label(newRequestFrame, text='Create New Request', font=('x', 40),
                                          bg=newRequest_FrameBg, fg='black')
                newRequestHeading.place(x=360, y=17)
                newRequest_titleLabel = Label(newRequestFrame, text='Title', font=('x', requestFrames_titleFontSize),
                                              bg=newRequest_FrameBg,
                                              fg='black')
                newRequest_titleLabel.place(x=75, y=95)
                newRequest_titleEntry = Entry(newRequestFrame, bg=newRequest_entryBg, fg='black', width=50,
                                              borderwidth=.1,
                                              font=('x', requestFrames_titleFontSize))
                newRequest_titleEntry.place(x=180, y=95)
                newRequest_descriptionLabel = Label(newRequestFrame, text='Description',
                                                    font=('x', requestFrames_titleFontSize),
                                                    bg=newRequest_FrameBg, fg='black', )
                newRequest_descriptionLabel.place(x=54, y=158)
                newRequest_descriptionText = Text(newRequestFrame, bg=newRequest_entryBg,
                                                  fg='black', font=('x', requestFrames_descriptionFontSize), width=70,
                                                  height=7)  #
                newRequest_descriptionText.place(x=183, y=158)
                sendButton = Button(newRequestFrame, text='Send', bg='#B9E5FF', font=('x', 20), command=send)
                sendButton.place(x=440, y=316)

                newRequestFrame.pack(fill=BOTH, expand=True)
                newRequestWindow.mainloop()

            newRequestButton = Button(requestPageFrame, image=newRequestButtonImage, padx=37, pady=18, font=('x', 16),
                                      command=newRequestWindow, bg=requestFrames_bg, borderwidth=0)
            # newRequestButton.pack(anchor=SW,padx=100 ) s
            newRequestButton.place(x=100, y=535)

        # Creating dummy requests
        # dummyRequest = { 'title':'Lack of Curtain',
        #                  'description':'Dear Sir , we have problem of lack of curtains in the classroom due to which we cannot see the materials displayed in the screen during the class',
        #                  'date':'30 January,2022',
        #                  'sender':'Prabin Tiwari',
        #                  'replies': {'hari kumar':'We will try to fix it as soon as possible'}
        #                 }

        # requestCollection.insert_one(dummyRequest)



        requestPageFrame.pack()
        requestPageFrame.pack_propagate(False)
        requestPageFrame.config(width=1280,height=640)

    def noticePage():
        noticePageFrame = Frame(mainFrame,bg='white')


        # fonts,bg,images
        global calendarImage,editButtonImage,deleteButtonImage
        calendarImage = PhotoImage(file='Project_images/calendar.png')
        editButtonImage = PhotoImage(file='Project_images/EditB.png')
        deleteButtonImage = PhotoImage(file='Project_images/DeleteB.png')
        noticeFrames_titleFontSize = 22
        noticeFrames_descriptionFontSize = 16
        noticeFrames_bg = '#FFECE4'
        noticeFrames_fg = 'black'
        edit_FrameBg = '#FFF5F1'
        edit_entryBg = '#BCC6BF'


        # connecting to db and collection
        address = "mongodb://localhost:27017"
        client = MongoClient(address)
        database = client.AppProject  # or client['AppProject']
        noticeCollection = database['Notices']





        class Notice:
            def __init__(self, master, id, date, title, description, sender, currentUser_type):

                # creating properties so that we can acess it later
                # arguments in constructor function can't be used elsewhere directly
                self.id = id
                self.date = date
                self.title = title
                self.description = description
                self.sender = sender
                self.currentUser_type = currentUser_type

                self.noticeFrame = Frame(master, bg=noticeFrames_bg, padx=56, pady=18)  #
                self.miniDateFrame = Frame(self.noticeFrame, bg=noticeFrames_bg)
                self.dateLabel = Label(self.miniDateFrame, text=date, bg=noticeFrames_bg, fg='#4A4A4A', )
                self.dateLabel.pack(side=RIGHT, )
                self.calenderImgLabel = Label(self.miniDateFrame, image=calendarImage, bg=noticeFrames_bg)  #
                self.calenderImgLabel.pack(side=RIGHT, pady=(2, 0))

                self.miniDateFrame.pack(anchor=NE)
                if currentUser_type == 'student':
                    self.senderLabel = Label(self.noticeFrame, text='~ ' + sender, bg=noticeFrames_bg, fg='#4A4A4A')
                    self.senderLabel.pack(anchor=E)
                self.titleLabel = Label(self.noticeFrame, text=title,
                                        font=('x', noticeFrames_titleFontSize), bg=noticeFrames_bg,
                                        fg=noticeFrames_fg)
                self.titleLabel.pack(anchor=W)
                self.orgText = description
                self.newText = lineBreaker(self.orgText)
                print(self.newText)
                self.descriptionLabel = Label(self.noticeFrame, text=self.newText,
                                              font=('x', noticeFrames_descriptionFontSize),
                                              fg=noticeFrames_fg, justify="center",bg=noticeFrames_bg)  # bg=noticeFrames_bg,
                self.descriptionLabel.pack(anchor=W,pady=10)  #
                if currentUser_type == 'teacher':
                    self.editButton = Button(self.noticeFrame, image=editButtonImage,
                                             borderwidth=0, command=self.editor)  # padx=26,pady=9,
                    self.editButton.pack(side=RIGHT)
                    self.deleteButton = Button(self.noticeFrame, image=deleteButtonImage, borderwidth=0,
                                               command=lambda: self.deleter(id=id, frame=self.noticeFrame))  # id=id,
                    self.deleteButton.pack(side=RIGHT, padx=17)
                self.noticeFrame.pack(anchor=N,padx=100, pady=(20, 0), fill=X, expand=True)  #

            # deleter method
            def deleter(self, id, frame):
                print('frame is ', frame)
                print('id is ', id)
                noticeCollection.delete_one({"_id": ObjectId(id)})
                frame.destroy()

            def editor(self, ):
                self.editWindow = Tk()
                self.editWindow.geometry('957x404')

                def saver():
                    # udpadting the database first
                    editedData = {'title': self.edit_titleEntry.get(),
                                  'description': self.edit_descriptionText.get(1.0, END)}
                    filter = {'_id': ObjectId(self.id)}
                    noticeCollection.update_one(filter, {'$set': editedData})

                    # updating in the notice noticePageFrame
                    self.titleLabel.config(text=self.edit_titleEntry.get())
                    editDescriptionRefactored = lineBreaker(self.edit_descriptionText.get(1.0, END))
                    self.descriptionLabel.config(text=editDescriptionRefactored)
                    self.editWindow.destroy()

                self.editFrame = Frame(self.editWindow, bg=edit_FrameBg, )
                self.editHeading = Label(self.editFrame, text='Edit Your Notice', font=('x', 40), bg=edit_FrameBg,
                                         fg='black')
                self.editHeading.place(x=360, y=17)
                self.edit_titleLabel = Label(self.editFrame, text='Title', font=('x', noticeFrames_titleFontSize),
                                             bg=edit_FrameBg,
                                             fg='black')
                self.edit_titleLabel.place(x=75, y=95)
                self.edit_titleEntry = Entry(self.editFrame, bg=edit_entryBg, fg='black', width=50,
                                             font=('x', noticeFrames_titleFontSize))
                self.edit_titleEntry.place(x=180, y=95)
                self.edit_descriptionLabel = Label(self.editFrame, text='Description',
                                                   font=('x', noticeFrames_titleFontSize),
                                                   bg=edit_FrameBg, fg='black', )
                self.edit_descriptionLabel.place(x=54, y=158)
                self.edit_descriptionText = Text(self.editFrame, bg=edit_entryBg,
                                                 fg='black', font=('x', noticeFrames_descriptionFontSize), width=70,
                                                 height=7)  #
                self.edit_descriptionText.place(x=183, y=158)
                self.saveButton = Button(self.editFrame, text='Save', bg='#B9E5FF', font=('x', 20), command=saver)
                self.saveButton.place(x=440, y=316)

                # Inserting the data to the entry noticePageFrame
                self.edit_titleEntry.insert(0, self.title)
                self.edit_descriptionText.insert(1.0, self.description)

                self.editFrame.pack(fill=BOTH, expand=TRUE)
                self.editWindow.mainloop()



        if currentUser_type == 'student':
            datas = noticeCollection.find()
        elif currentUser_type == 'teacher':
            datas = noticeCollection.find({'sender': currentUser})

        for data in datas:
            frameObject = Notice(master=noticePageFrame, id=data['_id'], date=data['date'], title=data['title'],
                                 description=data['description'], sender=data['sender'],
                                 currentUser_type=currentUser_type)
            print(data['description'])

        # again checking if it is teacher then postNewButton and its function will also be created
        # not combining it with above elif statement as postNewButton should be packed last
        if currentUser_type == 'teacher':
            def postNewWindow():
                # local bg
                postNew_FrameBg = '#FFF5F1'
                postNew_entryBg = '#D3DCE1'

                postNewWindow = Tk()
                postNewWindow.geometry('957x404')

                def post():
                    if postNew_titleEntry.get() == '' or postNew_descriptionText.get(1.0, END) == '':
                        print('enter smth')
                        return

                    # inserting to db first
                    todaysDate = datetime.datetime.today()
                    todaysDateShortened = todaysDate.strftime("%d %B,%Y")
                    newPostData = {'title': postNew_titleEntry.get(),
                                   'description': postNew_descriptionText.get(1.0, END),
                                   'date': todaysDateShortened, 'sender': 'Ram Bahadur'}
                    noticeCollection.insert_one(newPostData)

                    # inserting to the notice noticePageFrame
                    newDataFromDB = noticeCollection.find_one(newPostData)  # getting id from db
                    refactored_PostNewText = lineBreaker(postNew_descriptionText.get(1.0, END))
                    newPostObj = Notice(master=noticePageFrame, id=newDataFromDB['_id'], date=todaysDateShortened,
                                        title=postNew_titleEntry.get(), description=refactored_PostNewText,
                                        sender=currentUser, currentUser_type=currentUser_type)
                    postNewWindow.destroy()

                postNewFrame = Frame(postNewWindow, bg=postNew_FrameBg, )
                postNewHeading = Label(postNewFrame, text='Create New Notice', font=('x', 40), bg=postNew_FrameBg,
                                       fg='black')
                postNewHeading.place(x=360, y=17)
                postNew_titleLabel = Label(postNewFrame, text='Title', font=('x', noticeFrames_titleFontSize),
                                           bg=postNew_FrameBg,
                                           fg='black')
                postNew_titleLabel.place(x=75, y=95)
                postNew_titleEntry = Entry(postNewFrame, bg=postNew_entryBg, fg='black', width=50,
                                           font=('x', noticeFrames_titleFontSize))
                postNew_titleEntry.place(x=180, y=95)
                postNew_descriptionLabel = Label(postNewFrame, text='Description',
                                                 font=('x', noticeFrames_titleFontSize),
                                                 bg=postNew_FrameBg, fg='black', )
                postNew_descriptionLabel.place(x=54, y=158)
                postNew_descriptionText = Text(postNewFrame, bg=postNew_entryBg,
                                               fg='black', font=('x', noticeFrames_descriptionFontSize), width=70,
                                               height=7)  #
                postNew_descriptionText.place(x=183, y=158)
                postButton = Button(postNewFrame, text='Post', bg='#B9E5FF', font=('x', 20), command=post)
                postButton.place(x=440, y=316)

                postNewFrame.pack(fill=BOTH, expand=True)
                postNewWindow.mainloop()

            postNewButton = Button(noticePageFrame, text='Post New', padx=37, pady=18, bg='#B9E5FF', font=('x', 16),
                                   command=postNewWindow)
            postNewButton.place(x=100,y=535)

        # Creating dummy notices
        # dummyNotices = [
        #     # { 'title':'Regarding Phase Test',
        #     #              'description':'Test will be conducted on college premises. Please be there 15 minutes prior to the test. Thank you ',
        #     #              'date':'4 February,2022',
        #     #              'sender':'Ram Bahadur'},
        #                 {'title': 'Notice Regarding Examination Slip',
        #                  'description': 'Dear Students, This is to inform you all that your examination slip has been generated in the app. Kindly go through your Learners account. If your examination slip has not been generated because of your dues, please clear it within your due date. It is mandatory to have learners app in your mobile and printed examination slip with you to enter in examination hall and scan for your attendance in exam. Thank you ',
        #                  'date': '5 February,2022',
        #                  'sender': 'Hari Kumar'},
        #                   {'title': 'New Notice by Hari Kumar',
        #                  'description': 'Dear Students, This is to inform you all that your examination slip has been generated in the app. Kindly go through your Learners account. If your examination slip has not been generated because of your dues, please clear it within your due date. It is mandatory to have learners app in your mobile and printed examination slip with you to enter in examination hall and scan for your attendance in exam. Thank you ',
        #                  'date': '5 February,2022',
        #                  'sender': 'Hari Kumar'}
        #                 ]
        # noticeCollection.insert_many(dummyNotices)
        # print(noticesFramesDict['2'])


        noticePageFrame.pack()
        noticePageFrame.pack_propagate(False)
        noticePageFrame.config(width=1280, height=640)

    def indicatorAndPage(indicator,page):
        subjectsIndicator.config(bg=navigationBg)
        requestsIndicator.config(bg=navigationBg)
        noticesIndicator.config(bg=navigationBg)

        for frame in mainFrame.winfo_children():
            frame.destroy()
        indicator.config(bg='#FFFFFF')
        page()


    navigationFrame = Frame(homePageWindow,bg=navigationBg,height=67,pady=10)
    learnersLabel = Label(navigationFrame,text='Learners',font=('Brush Script MT',28),fg='black',bg=navigationBg)
    learnersLabel.grid(row=0,column=0,padx=(25,0))
    subjectsButton = Button(navigationFrame,text='Subjects',font=('x',25),fg='black',bg=navigationBg,bd=0,command=lambda:indicatorAndPage(subjectsIndicator,subjectPage))
    subjectsButton.grid(row=0,column=1,padx=(159,0))
    subjectsIndicator = Frame(navigationFrame,width=180,height=6,bg=navigationBg)
    subjectsIndicator.place(x=245,y=40)


    requestsButton = Button(navigationFrame,text='Requests',font=('x',25),fg='black',bg=navigationBg,bd=0,command=lambda:indicatorAndPage(requestsIndicator,requestPage))
    requestsButton.grid(row=0,column=2,padx=(159,0))
    requestsIndicator = Frame(navigationFrame, width=180, height=6, bg=navigationBg,)
    requestsIndicator.place(x=535, y=40)

    noticesButton = Button(navigationFrame,text='Notices',font=('x',25),fg='black',bg=navigationBg,bd=0,command=lambda:indicatorAndPage(noticesIndicator,noticePage))
    noticesButton.grid(row=0,column=3,padx=159)
    noticesIndicator = Frame(navigationFrame, width=180, height=6, bg=navigationBg,)
    noticesIndicator.place(x=820, y=40)
    profileButton = Button(navigationFrame,bg=navigationBg,image=profileImage)
    profileButton.grid(row=0,column=4)
    navigationFrame.pack(fill=X)

#creating the main frame
    mainFrameBg= 'white'
    mainFrame = Frame(homePageWindow,bg=mainFrameBg)
    global growImg,bookImg,personImg,textImg
    growImg = PhotoImage(file='Project_images/grow.png')
    bookImg= PhotoImage(file='Project_images/Vector-2.png')
    personImg =PhotoImage(file='Project_images/Vector-1.png')
    textImg=PhotoImage(file='Project_images/Vector.png')

    growImgLabel= Label(mainFrame,bg=mainFrameBg,image=growImg)#this is column1
    growImgLabel.pack(padx=(75,50),side=LEFT)
    bigColumn2=Frame(mainFrame,bg=mainFrameBg)
    valueLabel = Label(bigColumn2,justify=LEFT,text='We provide Students & Teachers\na platfrom to',font=('Inter',38,'bold'),fg='black',bg=mainFrameBg)
    valueLabel.pack()
    growLabel = Label(bigColumn2, text='GROW', font=('Inter', 38, 'bold'),fg='#40A17B',bg=mainFrameBg)
    growLabel.place(x=260,y=50)
    subHeading = Label(bigColumn2,font=('Inter', 20),fg='black',bg=mainFrameBg,justify=LEFT,text='Trusted by hundreds of  organiztions to host their learning \nmaterials and create portal for managing\ntheir system')
    subHeading.place(x=16,y=133)
    bookImgLabel=Label(bigColumn2,image=bookImg,bg=mainFrameBg)
    bookImgLabel.place(x=68,y=300)
    subjectDescLabel= Label(bigColumn2,fg='black',bg=mainFrameBg,font=('Inter',16),justify=LEFT,text='Acees subjects you\nare enrolled to ')
    subjectDescLabel.place(x=20,y=360)
    personImgLabel = Label(bigColumn2,image=personImg, bg=mainFrameBg)
    personImgLabel.place(x=295, y=300)
    personDescLabel = Label(bigColumn2,fg='black', bg=mainFrameBg, font=('Inter', 16), justify=LEFT,
                             text='Acees subjects you\nare enrolled to ')
    personDescLabel.place(x=240, y=360)
    textImgLabel=Label(bigColumn2,image=textImg, bg=mainFrameBg)
    textImgLabel.place(x=508, y=300)
    noticeDescLabel = Label(bigColumn2, fg='black', bg=mainFrameBg, font=('Inter', 16), justify=LEFT,
                             text='View the notices and\nimportant anouncements ')
    noticeDescLabel.place(x=445, y=360)

    bigColumn2.pack(side=LEFT)
    bigColumn2.pack_propagate(False)
    bigColumn2.config(width=653,height=453)

    mainFrame.pack()
    mainFrame.pack_propagate(False)
    mainFrame.config(width=1280,height=640)



    # frame of footer part------------------------------------------------------
    frameofblack = Frame(homePageWindow, width=1280,height=100, bg="#1D1D1D")


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
    frameofblack.pack()

    # #Creating the black footer
    # footerBg = '#1D1D1D'
    # instaImg=PhotoImage(file='insta.png')
    # facebookImg=PhotoImage(file='facebook.png')
    # linkedinImg=PhotoImage(file='linkedin.png')
    # twitterImg=PhotoImage(file='twitter.png')
    #
    #
    #
    # footerFrame = Frame(homePageWindow,bg=footerBg)
    #
    # aboutUsFrame = Frame(footerFrame,)
    # aboutUsHeading = Label(aboutUsFrame,font=('x',16,'bold'),justify=LEFT,text='About Us',)
    # aboutUsHeading.pack(anchor=W)
    # aboutUsContent = Label(aboutUsFrame,font=('x',14),justify=LEFT,text='We are dedicated to making the students\nlearn various subjects and topics\nin an easy and fun way')
    # aboutUsContent.pack()
    # aboutUsFrame.grid(row=0,column=0)
    #
    # contactUsFrame = Frame(footerFrame,)
    # contactUsHeading = Label(contactUsFrame,justify=LEFT,text='Contact Us',font=('x',16,'bold'))
    # contactUsHeading.pack(anchor=W)
    # emailLabel = Label(contactUsFrame,font=('x',14),justify=LEFT,text='learners10@gmail.com')
    # emailLabel.pack()
    # phoneNoLabel = Label(contactUsFrame,font=('x',14),text='015532319 / 015542913')
    # phoneNoLabel.pack()
    # contactUsFrame.grid(row=0,column=1)
    #
    # followUsFrame = Frame(footerFrame,bg=footerBg)
    # followUsHeading = Label(followUsFrame,justify=LEFT,text='Follow Us',font=('x',16,'bold'))
    # followUsHeading.pack()
    # instagramImg = Label (followUsFrame,image=instaImg,bg=footerBg)
    # instagramImg.place(x=0,y=20)
    # # facebookImg = Label(followUsFrame, image=facebookImg, bg=footerBg)
    # # facebookImg.place(x=0,y=0)
    # # linkedinImg = Label(followUsFrame, image=linkedinImg, bg=footerBg)
    # # linkedinImg.place(x=0,y=0)
    # # twitterImg = Label(followUsFrame, image=twitterImg, bg=footerBg)
    # # twitterImg.place(x=0,y=0)
    #
    # followUsFrame.grid(row=0,column=2)
    #
    # imageUsedButton = Button(footerFrame,justify=LEFT,text='Images Used',font=('x',16,'bold'),bg=footerBg)
    # imageUsedButton.grid(row=0,column=3)
    #
    # footerFrame.pack()
    homePageWindow.mainloop()

homePage()
