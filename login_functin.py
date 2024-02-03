# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:37:05 2022

@author: twitc
"""

import datetime
from tkinter import *
from tkinter import ttk
import user

def loginCheck():
    UserList = []
    with open('test_profiles.txt') as f:
        for line in f:
            temp = user.User()
            line = line.strip().replace(" ", "").split(",")
            temp.setUser(line[0])
            temp.setPass(line[1])
            temp.setHint(line[2])
            UserList.append(temp)
    for i in UserList:
        if i.getUser() == usr_e.get() and i.getPass() == pass_e.get():
            window.destroy()
            # import ms_player
    return


def createAccount():
    frame1.pack_forget()
    frame2.pack()
    return


def back():
    frame2.pack_forget()
    frame1.pack()
    return


def confirmCreate():
    f = open('test_profiles.txt', 'a')
    createdUser = user.User()
    if (c_pass_e.get() == c_pass_e2.get()):
        createdUser.setUser(usr_e.get())
        createdUser.setPass(c_pass_e.get())
        createdUser.setHint(hint_e.get())
        f.write(createdUser.getUser() + ", " +
                createdUser.getPass() + ", " + createdUser.getHint() + "\n")
        f.close()
        frame2.pack_forget()
        frame1.pack()
    else:
        errorMessage = Label(frame2, text="Re-enter Password",
                             bg='#00008B', fg='white', font=('Helvetica', 16, 'bold'))
        errorMessage.grid(row=7, columnspan=4)
    return


window = Tk()
window.geometry("380x200")
window['bg'] = '#00008B'
window.title('Mage Speller Log-in System')

# frame 1
frame1 = Frame(window)
frame1['bg'] = "#00008B"

dt = Label(frame1, text=datetime.date.today(), bg='#00008B',
           fg='white', font=('Helvetica', 10, 'bold'))
lbl = Label(frame1, text='Welcome to Mage Speller',
            bg='#00008B', fg='white', font=('Helvetica', 16))
usr_l = Label(frame1, text='User Name: ', fg='black',
              font=('Helvetica', 10, 'bold'))
usr_e = Entry(frame1, text='Enter User Name', bg='white', fg='black', bd=5)
pass_l = Label(frame1, text='Password:   ', fg='black',
               font=('Helvetica', 10, 'bold'))
pass_e = Entry(frame1, bg='white', fg='black', bd=5)
login = Button(frame1, text="Log In", fg='blue', command=loginCheck)
create_account = Button(frame1, text="Create Account",
                        fg='blue', command=createAccount)

dt.grid(row=0, column=4)
lbl.grid(row=1, columnspan=4)
usr_l.grid(row=2, column=1)
usr_e.grid(row=2, column=2)
pass_l.grid(row=3, column=1)
pass_e.grid(row=3, column=2)
login.grid(row=4, columnspan=2)
create_account.grid(row=4, columnspan=4)


# frame 2
frame2 = Frame(window)
frame2['bg'] = "#00008B"


dt = Label(frame2, text=datetime.date.today(), bg='#00008B',
           fg='white', font=('Helvetica', 10, 'bold'))
lbl = Label(frame2, text='Create Account',
            bg='#00008B', fg='white', font=('Helvetica', 16))
usr_l = Label(frame2, text='User Name: ', fg='black',
              font=('Helvetica', 10, 'bold'))
usr_e = Entry(frame2, text='Enter User Name', bg='white', fg='black', bd=5)
c_pass_l = Label(frame2, text='Password:   ', fg='black',
                 font=('Helvetica', 10, 'bold'))
c_pass_e = Entry(frame2, show="*", bg='white', fg='black', bd=5)
c_pass_l2 = Label(frame2, text='Confirm Pass:   ', fg='black',
                  font=('Helvetica', 10, 'bold'))
c_pass_e2 = Entry(frame2, show="*", bg='white', fg='black', bd=5)
hint_l = Label(frame2, text='Hint:   ', fg='black',
               font=('Helvetica', 10, 'bold'))
hint_e = Entry(frame2, bg='white', fg='black', bd=5)
confirm = Button(frame2, text="Confrim", fg='blue', command=confirmCreate)
backB = Button(frame2, text="Back", fg='Blue', command=back)

dt.grid(row=0, column=4)
lbl.grid(row=1, columnspan=4)
usr_l.grid(row=2, column=1)
usr_e.grid(row=2, column=2)
c_pass_l.grid(row=3, column=1)
c_pass_e.grid(row=3, column=2)
c_pass_l2.grid(row=4, column=1)
c_pass_e2.grid(row=4, column=2)
hint_l.grid(row=5, column=1)
hint_e.grid(row=5, column=2)
confirm.grid(row=6, columnspan=2)
backB.grid(row=6, columnspan=4)
# start that shit baby
frame1.pack()
window.mainloop()
