from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from PIL import Image, ImageTk
import p2
import p2admin
#import os
#from tkinter.ttk import *


def perdict_person():
    """Predict Personality"""
    
    # Closing The Previous Window
    root.withdraw()
    
    # Creating new window
    top = Toplevel()
    #top.geometry('700x500')
    top.geometry('1920x1080')
    top.configure(background='#0B5A81')
    top.title("Admin,User Page")

    def admin_login():
        #ws=Toplevel()
        p2admin.adminloginpage()

    def user_login():
        p2.userloginpage()
        #os.system('python Mpdemo.py')
        
        
        
    lab1=Label(top, text="Login Page", bg='white', font=titleFont, pady=30).pack()
    '''b1=Button(top, padx=2, pady=1, width=30, text="Admin", bg='white', foreground='black', bd=1, font=homeBtnFont,
             command=admin_login).pack()
    b2=Button(top, padx=2, pady=2, width=30, text="User", bg='white', foreground='black', bd=1, font=homeBtnFont,
              command=user_login).pack()'''
    
    img =Image.open('C:\\Users\\sindhu\\Desktop\\a1.png')
    bg = ImageTk.PhotoImage(img)
    lab2=Label(top,image=bg, pady=30).place(x=600,y=350)
    #label = Label(root, image=bg)
    #label.place(x = 0,y = 0)

    img1 =Image.open('C:\\Users\\sindhu\\Desktop\\a2.png')
    bg1 = ImageTk.PhotoImage(img1)
    lab3=Label(top,image=bg1, pady=30).place(x=1100,y=350)


    
    b1=Button(top, padx=2, pady=1, width=30, text="Admin", bg='white', foreground='black', bd=1, font=homeBtnFont,
             command=admin_login).place(x=500,y=600)
    b2=Button(top, padx=2, pady=2, width=30, text="User", bg='white', foreground='black', bd=1, font=homeBtnFont,
              command=user_login).place(x=1000,y=600)
    

    top.mainloop()
  



if __name__ == "__main__":
    #model = train_model()
    #model.train()

    root = Tk()
    #root.geometry('700x500')
    root.geometry('1920x1080')
    #root.configure(background='white')
    root.title("Personality Prediction System")
    titleFont = font.Font(family='Helvetica', size=25, weight='bold')
    img =Image.open('C:\\Users\\sindhu\\Desktop\\s2.png')
    bg = ImageTk.PhotoImage(img)
    label = Label(root, image=bg)
    label.place(x = 0,y = 0)
    homeBtnFont = font.Font(size=12, weight='bold')
    lab=Label(root, text="Resume Parser With Personality Prediction", font=titleFont, pady=30).pack()
    b3=Button(root, padx=4, pady=4, width=30, text="Predict Personality", bg='black', foreground='white', bd=1, font=homeBtnFont, command=perdict_person).place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    root.mainloop()
