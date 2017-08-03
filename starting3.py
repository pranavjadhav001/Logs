from tkinter import *
import os
import random
from PIL import Image,ImageTk
import datetime
import prac



def new():

    root = Tk()
    root.title("HYHY")

    one = Label(root, text="Welcome to hyhy Logs",font=('helvetica',26),relief = 'sunken')
    one.pack(side=TOP)
    path = "media.jpg"

    pic = ImageTk.PhotoImage(Image.open(path))
    label = Label(root, image=pic)
    label.pack(side=TOP)
    button1 = Button(root,text="Open a new account",font=('italiac',20,'bold'),fg="black",bg="grey",bd=8,command =signup)
    button2 = Button(root,text="Already have an account",font=('italiac',20,'bold'),fg="black",bg="grey",bd=8,command= login)
    button1.pack()

    button2.pack()
    root.mainloop()
def signup():  # This is the signup definiti
    global pwordE  # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots

    roots = Tk()  # This creates the window, just a blank one.
    roots.title('Signup')  # This renames the title of said window to 'signup'
    intruction = Label(roots,
                           text='Please Enter new Credidentials\n')  # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0,
                        sticky=E)  # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    nameL = Label(roots,
                      text='New Username: ')  # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ')  # ^^
    nameL.grid(row=1, column=0,
                   sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W)  # ^^

    nameE = Entry(roots)  # This now puts a text box waiting for input.
    pwordE = Entry(roots,
                       show='*')  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1)  # You know what this does now :D
    pwordE.grid(row=2, column=1)  # ^^

    signupButton = Button(roots, text='Signup',
                              command=FSSignup)  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()  # This just makes the window keep open, we will destroy it soon

def FSSignup():
    benzu = "C:\\files"
    benz = os.path.join(benzu,nameE.get())
    os.mkdir(benz)

    os.chdir(benz)
    with open(str(nameE.get()+".txt"),'w') as nhi:

        nhi.write(nameE.get())
        nhi.write("\n")
        nhi.write(pwordE.get())

    roots.destroy()
    login()

def login():
    global nameEL
    global pwordEL  # More globals :D
    global rootA

    rootA = Tk()  # This now makes a new window.
    rootA.title('Login')  # This makes the window title 'login'

    intruction = Label(rootA, text='Please Login\n')  # More labels to tell us what they do
    intruction.grid(sticky=E)  # Blahdy Blah

    nameL = Label(rootA, text='Username: ')  # More labels
    pwordL = Label(rootA, text='Password: ')  # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA)  # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='Login',
                    command=CheckLogin)  # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Delete User', fg='red',
                    command=DelUser)  # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()

def CheckLogin():
    geg = "C:\\files"
    kappa = os.path.join(geg,nameEL.get())
    if os.path.exists(kappa):
        os.chdir(kappa)


        with open(str(nameEL.get())+".txt",'r') as f:
            data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
            uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it


        if nameEL.get() == uname and pwordEL.get() == pword:  # Checks to see if you entered the correct data.
            r = Tk()  # Opens new window
            r.title(':D')
            r.geometry('150x50')  # Makes the window a certain size
            rlbl = Button(r,text='\n[+] Logged In',command=r.quit)  # "logged in" label


            rlbl.pack()  # Pack is like .grid(), just different
            r.mainloop()
            prac.baap()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

def DelUser():

    hi = nameEL.get()+".txt"

    if os.path.isfile(hi):
        os.remove(hi)
    rootA.destroy()  # Destroys the login window


new()