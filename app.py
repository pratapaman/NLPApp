import tkinter
from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API
from PIL import Image, ImageTk


class NLPApp:
    def __init__(self):

        # create db object
        self.dbo = Database()
        self.apio = API()

        self.root = tkinter.Tk()
        # self.root is variable that is object of tk class 
        self.root.title('NLPApp')
        #self.root.iconbitmap('resources/image.ico')
        # self.root.configure(bg='#34495E')
        

        self.root.geometry("500x500")

        # Load the image
        #img = Image.open("OIP.jpg")
        # Resize the image to fit the window
        #img = img.resize((500, 500), Resampling.LANCZOS)
        # Create a PhotoImage object from the resized image
        #photo = ImageTk.PhotoImage(img)

        # Create a label with the PhotoImage as the background
        #label = Label(self.root, image=photo)
        #label.pack()



        image = Image.open("OIP.jpg")
        photo = ImageTk.PhotoImage(image)

        # create a label with the image
        label = Label(self.root, image=photo)
        label.pack()

        # configure the window background to be the image
        self.root.configure(background='black')
        self.root.attributes("-transparentcolor", 'black')
        self.root.wm_attributes("-alpha", 0.9)




# load the image file
        # img = Image.open("OIP.jpg")
        # img = img.resize((1000, 1000), Image.NEAREST)

# create a PhotoImage object from the image
        # photo = ImageTk.PhotoImage(img)

# create a label widget with the PhotoImage as the background
        # bg_label = Label(self.root, image=photo)
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.login_gui()

        self.root.mainloop()


    def login_gui(self):

        self.clear()


        heading = Label(self.root,text='NLPApp',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn = Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(5,10))

        label3=Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn =Button(self.root,text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(5,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        label1 = Label(self.root,text='Enter Name')
        label1.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        register_btn = Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(5,10))

        label3=Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn =Button(self.root,text='Resister Now',command=self.register_gui)
        redirect_btn.pack(pady=(5,10))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success','Registration successful. you can login now')
        else:
            messagebox.showinfo('Error','Email already exists')

            
    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)
        
        if response:
            messagebox.showinfo('success','login successful')
            self.home_gui()
        else: 
            messagebox.showerror('error','Incorrect email/password')



    def home_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))
        
        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=30,height=2,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(5,10))
        
        ner_btn = Button(self.root,text='Name Entity Recognition',width=30,height=2,command=self.perform_registration)
        ner_btn.pack(pady=(5,10))        
        
        emotion_btn = Button(self.root,text='Emotion Prediction',width=30,height=2,command=self.perform_registration)
        emotion_btn.pack(pady=(5,10))

        logout_btn = Button(self.root,text='Logout',width=30,height=2,command=self.login_gui)
        logout_btn.pack(pady=(5,10))

    def sentiment_gui(self):

        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        heading = Label(self.root,text='Sentiment Analysis',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10,10))
        
        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(10,10))
        
        sentiment_btn = Button(self.root,text='Analysis Sentiment',width=30,height=2,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(5,10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root,text='Go Back',width=30,height=2,command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' +str(result['sentiment'][i]) + '\n'
        
        print(txt)
        self.sentiment_result['text'] = txt

    def ner_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        heading = Label(self.root,text='Name Entity Recognition',bg='#34495E', fg='white')
        heading.pack(pady=(10,30))
        heading.configure(font = ('version',24,'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10,10))
        
        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(10,10))
        
        ner_btn = Button(self.root,text='Analysis Text',width=30,height=2,command=self.do_Name_Entity_Recognition)
        ner_btn.pack(pady=(5,10))

        self.ner_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root,text='Go Back',width=30,height=2,command=self.home_gui)
        goback_btn.pack(pady=(10,10))


    def do_Name_Entity_Recognition(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)

        txt = ''
        for i in result['ner']:
            txt = txt + i + ' -> ' +str(result['ner'][i]) + '\n'
        
        print(txt)
        self.ner_result['text'] = txt


nlp = NLPApp()
