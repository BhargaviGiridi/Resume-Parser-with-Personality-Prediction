from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image,ImageTk
#import User
#import p3
import sqlite3
import os

def adminloginpage():
    f = ('Times', 14)
    F= ('Times New Roman', 20)
    g=('Cooper Black',16)
    con = sqlite3.connect('admindata.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text,
                    email text,
                    contact number,
                    gender text,
                    country text,
                    password text) ''')
    con.commit()
    ws = Tk()
    ws.title('PythonGuides')
    #ws.geometry('1366x768')
    ws.geometry('1920x1080')
    ws.config(bg='#0B5A81')

    def insert_record():
        check_counter=0
        warn = ""
        if register_name.get() == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1

        if register_email.get() == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1
        if register_mobile.get() == "":
            warn = "Contact can't be empty"
        else:
            check_counter += 1
   
        if  var.get() == "":
            warn = "Select Gender"
        else:
            check_counter += 1

        if variable.get() == "":
            warn = "Select Country"
        else:
            check_counter += 1

        if register_pwd.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1

        if pwd_again.get() == "":
            warn = "Re-enter password can't be empty"
        else:
            check_counter += 1

        if register_pwd.get() != pwd_again.get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1

        if check_counter == 8:
            try:
                con = sqlite3.connect('admindata.db')
                cur = con.cursor()
                cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()
                })
                con.commit()
                messagebox.showinfo('confirmation', 'Record Saved')
            except Exception as ep:
                messagebox.showerror('', ep)
        else:
            messagebox.showerror('Error', warn)


    def login_response():
        try:
            con = sqlite3.connect('admindata.db')
            c = con.cursor()
            for row in c.execute("Select * from record"):
                username = row[1]
                pwd = row[5]
        except Exception as ep:
            messagebox.showerror('', ep)

        uname = email_tf.get()
        upwd = pwd_tf.get()
        check_counter=0
        if uname == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if upwd == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1

        if check_counter == 2:
            if (uname == username and upwd == pwd):
                res=messagebox.askquestion('Login Status', 'Logged in Successfully!\n Do You want to continue?')
                if res=='yes':
                    ws.withdraw()
                    ws1=Toplevel()
                    ws1.geometry("1920x1080")
                    ws1.config(bg='#0B5A81')
                    def getFolderPath():
                        #filedialog.askdirectory()
                        os.startfile("C:\\Users\\sindhu\\Desktop\\MP")

                    
                        '''name = filedialog.askopenfilename(initialdir="C://Users//sindhu//Desktop//MP",
                            filetypes =(("Document","*.docx*"),("PDF","*.pdf*"),('PNG', '*.png')),
                           title = "Choose a file."
                           )'''
                    homeBtnFont = font.Font(size=12, weight='bold')
                    '''img =Image.open('C:\\Users\\sindhu\\Desktop\\m1.png')
                    bg = ImageTk.PhotoImage(img)
                    label1 = Label(ws1, image=bg)
                    label1.place(x = 0,y = 0)'''

                    img3 =Image.open("C:\\Users\\sindhu\\Desktop\\o1.png")
                    bg3 = ImageTk.PhotoImage(img3)
                    lab7=Label(ws1,image=bg3, pady=30).place(x=600,y=350)
                    img4 =Image.open("C:\\Users\\sindhu\\Desktop\\e3.png")
                    bg4 = ImageTk.PhotoImage(img4)
                    lab8=Label(ws1,image=bg4, pady=30).place(x=1100,y=350)

                    Btt1=Button(ws1, padx=2, pady=1, width=30, text="Open Folder", bg='white', foreground='black', bd=1, font=homeBtnFont,
                              command=getFolderPath).place(x=500,y=600)
                    Btt2=Button(ws1, padx=2, pady=2, width=30, text="Exit", bg='white', foreground='black', bd=1, font=homeBtnFont,
                              command=lambda:  ws1.destroy()).place(x=1000,y=600)

                    ws1.mainloop()


                  
                    #btnFind = ttk.Button(ws, text="Open Folder",command=getFolderPath).place(x=300,y=600)
                    #btnFind.grid(row=0,column=2)
                    #quitBtn = Button(ws, text="Exit",font=10, command =lambda:  ws.destroy()).place(x=600,y=600)


                    #lab1=Label(top, text="Login Page", bg='white', font=titleFont, pady=30).pack()
                    
                    #img3 =Image.open('C:\\Users\\sindhu\\Desktop\\a1.png')
                    #bg3 = ImageTk.PhotoImage(img3)
                    #lab7=Label(ws1,image=bg3, pady=30).place(x=600,y=350)
                    #img4 =Image.open('C:\\Users\\sindhu\\Desktop\\a2.png')
                    #bg4 = ImageTk.PhotoImage(img4)
                    #lab8=Label(ws1,image=bg4, pady=30).place(x=1100,y=350)

                                        #os.system('python p3.py')
                    #p3.main_result()
                    #User.method1()
                    #execfile('User.py')
                    
                    #newWindow=Toplevel(ws)
                    #newWindow.title("User Login")
                    #newWindow.geometry('1366x768')
                    #os.system("python User.py")
                else :
                    messagebox.showinfo('Warning', 'Are you sure,Do you want to quit?')
            else:
                messagebox.showerror('Login Status', 'invalid username or password')
        else:
            messagebox.showerror('', warn)
  

    def clear_text():
        register_name.delete(0, END)
        register_email.delete(0, END)
        register_mobile.delete(0, END)
        register_pwd.delete(0, END)
        pwd_again.delete(0, END)
        email_tf.delete(0, END)
        pwd_tf.delete(0, END)

    var = StringVar()
    var.set('male')

    countries = []
    variable = StringVar()
    world = open('countries.txt', 'r')
    for country in world:
        country = country.rstrip('\n')
        countries.append(country)
    variable.set(countries[5])

    # widgets
    Label(ws,text="*** Admin Login/Registration Form ***",bg='RED',font=F).pack()

    left_frame = Frame(ws,bd=2,bg='#CCCCCC',relief=SOLID,padx=10,pady=10)

    Label(left_frame,text="-->LOGIN HERE",bg='#CCCCCC',font=g).grid(row=0, column=0, sticky=W, pady=10)

    Label(left_frame,text="Enter Email",bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

    Label(left_frame,text="Enter Password",bg='#CCCCCC',font=f).grid(row=2, column=0,sticky=W, pady=10)

    email_tf = Entry(left_frame,font=f)

    pwd_tf = Entry(left_frame,font=f,show='*')

    login_btn = Button(left_frame,width=15,text='Login',font=f,relief=SOLID,cursor='hand2',command=login_response)
    

    right_frame = Frame(ws,bd=2,bg='#CCCCCC',relief=SOLID,padx=10,pady=10)
    
    Label(right_frame,text="-->REGISTER HERE",bg='#CCCCCC',font=g).grid(row=0, column=0, sticky=W, pady=10)

    Label(right_frame,text="Enter Name",bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

    Label(right_frame,text="Enter Email",bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)

    Label(right_frame,text="Contact Number",bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)

    Label(right_frame,text="Select Gender",bg='#CCCCCC',font=f).grid(row=4, column=0, sticky=W, pady=10)

    Label(right_frame,text="Select Country",bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)

    Label(right_frame,text="Enter Password",bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)

    Label(right_frame,text="Re-Enter Password",bg='#CCCCCC',font=f).grid(row=7, column=0, sticky=W, pady=10)

    gender_frame = LabelFrame(right_frame,bg='#CCCCCC',padx=10,pady=10,)


    register_name = Entry(right_frame,font=f)

    register_email = Entry(right_frame,font=f)

    register_mobile = Entry(right_frame,font=f)

    male_rb = Radiobutton(gender_frame,text='Male',bg='#CCCCCC',variable=var,value='male',font=('Times', 10),)

    female_rb = Radiobutton(gender_frame,text='Female',bg='#CCCCCC',variable=var,value='female',font=('Times', 10),)

    others_rb = Radiobutton(gender_frame,text='Others',bg='#CCCCCC',variable=var,value='others',font=('Times', 10))

    register_country = OptionMenu(right_frame,variable,*countries)

    register_country.config(width=15,font=('Times', 12))

    register_pwd = Entry(right_frame,font=f,show='*')

    pwd_again = Entry(right_frame,font=f,show='*')

    register_btn = Button(right_frame,width=15,text='Register',font=f,relief=SOLID,cursor='hand2',command=insert_record)

    clear_btn = Button(right_frame,width=15,text='Clear',font=f,relief=SOLID,cursor='hand2',command=clear_text)

    # widgets placement
    email_tf.grid(row=1, column=1, pady=10, padx=20)
    pwd_tf.grid(row=2, column=1, pady=10, padx=20)
    login_btn.grid(row=3, column=1, pady=10, padx=20)
    left_frame.place(x=300, y=300)

    register_name.grid(row=1, column=1, pady=15, padx=30)
    register_email.grid(row=2, column=1, pady=15, padx=30)
    register_mobile.grid(row=3, column=1, pady=15, padx=30)
    register_country.grid(row=5, column=1, pady=15, padx=30)
    register_pwd.grid(row=6, column=1, pady=15, padx=30)
    pwd_again.grid(row=7, column=1, pady=15, padx=30)
    register_btn.grid(row=8, column=0, pady=15, padx=30)
    clear_btn.grid(row=8, column=1, pady=15, padx=30)
    right_frame.place(x=1000, y=200)

    gender_frame.grid(row=4, column=1, pady=10, padx=30)
    male_rb.pack(expand=True, side=LEFT)
    female_rb.pack(expand=True, side=LEFT)
    others_rb.pack(expand=True, side=LEFT)

    ws.mainloop()
