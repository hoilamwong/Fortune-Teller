"""Team 3: Fortune Teller Application
Created By: Constance Sturm, Michelle Cook, Chelsea Nieves,
Valerie Rudich, and Hoi Lam Wong
University of Maryland Global Campus
CMSC 495-7382: Capstone in Computer Science
Professor David Castillo
November 26, 2023"""

import random
import fileinput
from tkinter import *
from tkinter.ttk import *
import tkinter as tk


def main():
    """Display Main Menu and Welcome Message"""
    # create root window
    root = Tk()
    # root window and title dimensions
    root.title('Fortune Teller')
    # geometry of the box (width x height)
    root.geometry('350x200')

    # add menu bar to allow user to view rules or exit
    menubar = Menu(root)
    # add Rules menu and commands
    rules = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Rules', menu=rules)
    rules.add_command(label='View Rules', command=lambda: display_rules())
    # add Exit menu and commands
    # updated variable name for menu exit
    program_exit = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Exit', menu=program_exit)
    program_exit.add_command(label='Exit Program', command=root.destroy)

    # add label to the root window
    lbl1 = Label(root, text='Welcome to the Fortune Teller Game!')
    lbl2 = Label(root, text='Reveal what your future holds!')
    # ask user if they want to play as a guest
    lbl3 = Label(root, text='Would you like to login?')
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()

    # add buttons for user to select yes or no
    btn_login_yes = tk.Button(root, text='Yes', bd='5', command=lambda: login())
    btn_login_no = tk.Button(root, text='No', bd='5', command=lambda: guest_menu())

    btn_login_yes.pack()
    btn_login_no.pack()
    # display menu
    root.config(menu=menubar)
    root.mainloop()


def login():
    """This function is used for returning users"""


# Added new registration form
def guest_menu():
    # Create a guest menu window
    guest = Tk()
    guest.geometry('300x200')
    guest.title('Guest Form')
    lbl_guest = Label(guest, text='Would you like to play as a guest?')
    lbl_guest.pack()
    # add buttons for the user to select their answer
    btn_fortune_menu = tk.Button(guest, text='Yes', bd='5', command=lambda: fortune_menu())
    btn_register = tk.Button(guest, text='No', bd='5', command=lambda: registration())
    btn_fortune_menu.pack()
    btn_register.pack()


def registration():
    # have the user register as a login user
    reg = Tk()
    reg.geometry('300x200')
    reg.title('Registration Form')
    # create new frame to contain the labels and entry boxes
    frm_form = Frame(relief=SUNKEN, borderwidth=3)
    frm_form.pack()

    a = Label(reg, text="First Name:")
    a.grid(row=0, column=0)
    b = Label(reg, text="Last Name:")
    b.grid(row=1, column=0)
    c = Label(reg, text="Username:")
    c.grid(row=2, column=0)
    d = Label(reg, text="Password:")
    d.grid(row=3, column=0)
    a1 = Entry(reg)
    a1.grid(row=0, column=1)
    b1 = Entry(reg)
    b1.grid(row=1, column=1)
    c1 = Entry(reg)
    c1.grid(row=2, column=1)
    d1 = Entry(reg)
    d1.grid(row=3, column=1)

    btn_submit = Button(master=reg, text="Submit", command=lambda: database())
    btn_submit.grid(row=4, column=0)
    btn_close = Button(reg, text='Close', command=reg.destroy)
    btn_close.grid(row=4, column=1)
    
def database():
    """Will be used to save registration/fortunes to database"""


def display_rules():
    """ Create a window that displays the rules to the user"""
    rules = Tk()
    rules.geometry('300x200')
    rules.title('Rules of the Fortune Teller')
    lbl = Label(rules, text='How to Play the Fortune Teller Game', font='50')
    lbl.pack()
    msg = Message(rules, text='> Please select a category from the following buttons. \n '
                              '> The program will display the fortune to you automatically. \n'
                              '> The program will save your fortune '
                              '> if you are logged in as a returning user and select save from menu. \n'
                              '> Use the menu selection Exit to exit the program.\n')
    msg.pack()
    btn_rule_close = tk.Button(rules, text='Close', bd='5', command=rules.destroy)
    btn_rule_close.pack()


def fortune_menu():
    """This menu will give the user the option to choose a category"""
    fortune = Tk()
    fortune.title('Fortune Menu')

    # Create menu bar
    menubar = Menu(fortune)

    # Add file menu for save and exit options
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='New Fortune', command=lambda: fortune_menu())
    file.add_command(label='Save', command=lambda: database())
    file.add_separator()
    file.add_command(label='Exit', command=fortune.destroy)

    lbl = Label(fortune, text='Please select a category!')
    btn_love = Button(fortune, text='Love', command=lambda: love_fortune())
    btn_career = Button(fortune, text='Career', command=lambda: career_fortune())
    btn_health = Button(fortune, text='Health', command=lambda: health_fortune())
    btn_general = Button(fortune, text='General', command=lambda: general_fortune())
    btn_random = Button(fortune, text='Random', command=lambda: random_fortune())

    lbl.pack()
    btn_love.pack()
    btn_career.pack()
    btn_health.pack()
    btn_general.pack()
    btn_random.pack()


def love_fortune():
    with open("love_fortune.txt", "r") as file:
        all_text: str = file.read()
        fortune = list(map(str, all_text.split(":")))
        # Print random fortune from love_fortune.txt
        print(random.choice(fortune))


def career_fortune():
    with open("career_fortune.txt", "r") as file:
        all_text: str = file.read()
        fortune = list(map(str, all_text.split(":")))
        # Print random fortune from career_fortune.txt
        print(random.choice(fortune))


def health_fortune():
    with open("health_fortune.txt", "r") as file:
        all_text: str = file.read()
        fortune = list(map(str, all_text.split(":")))
        # Print random fortune from health_fortune.txt
        print(random.choice(fortune))


def general_fortune():
    with open("general_fortune.txt", "r") as file:
        all_text: str = file.read()
        fortune = list(map(str, all_text.split(":")))
        # Print random fortune from general_fortune.txt
        print(random.choice(fortune))


def random_fortune():
    with fileinput.input(
            files=("love_fortune.txt", "career_fortune.txt", "health_fortune.txt", "general_fortune.txt")) as file:
        all_text: str = file.read()
        fortune = list(map(str, all_text.split(":")))
        # Print random fortune from any of the .txt files
        print(random.choice(fortune))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
