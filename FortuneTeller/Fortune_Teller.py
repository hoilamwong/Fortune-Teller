"""Team 3: Fortune Teller Application
Created By: Constance Sturm, Michelle Cook, Chelsea Nieves,
Valerie Rudich, and Hoi Lam Wong
University of Maryland Global Campus
CMSC 495-7382: Capstone in Computer Science
Professor David Castillo
November 26, 2023"""

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

import DatabaseHelper as DBHelper
from FTHelper import *

# def guest_menu():
#     """
#     This function creates a new pop-up window for Guest Form
#
#     UPDATE ! 12/1 This method is not used anymore since I removed the window to ask whether the player want to play as guest or not
#     User can register directly from the main menu
#     """
#
#     # Create a guest menu window
#     guest_tk = Tk()
#     guest_tk.geometry('300x200')
#     guest_tk.title('Guest Form')
#     center_window(guest_tk)
#
#     # Guest Label
#     lbl_guest = Label(guest_tk, text='Would you like to play as a guest?')
#     lbl_guest.pack()
#
#     # add buttons for the user to select their answer
#     btn_fortune_menu = tk.Button(guest_tk, text='Yes', bd='5', command=lambda: fortune_menu())
#     btn_register = tk.Button(guest_tk, text='No', bd='5', command=lambda: registration_window())
#     btn_fortune_menu.pack()
#     btn_register.pack()
#
#     guest_tk.mainloop()

def display_rules():
    """ Create a window that displays the rules to the user"""

    # Initialize New Window
    rules_tk = Tk()
    rules_tk.geometry('300x200')
    rules_tk.title('Rules of the Fortune Teller')
    center_window(rules_tk)

    lbl = Label(rules_tk, text='How to Play the Fortune Teller Game', font='50')
    lbl.pack()
    msg = Message(rules_tk, text='> Please select a category from the following buttons. \n '
                                 '> The program will display the fortune to you automatically. \n'
                                 '> The program will save your fortune '
                                 '> if you are logged in as a returning user and select save from menu. \n'
                                 '> Use the menu selection Exit to exit the program.\n')
    msg.pack()
    btn_rule_close = tk.Button(rules_tk, text='Close', bd='5', command=rules_tk.destroy)
    btn_rule_close.pack()


def login_window():
    """This function is used for returning users"""

    # Initialize New Window
    login_tk = Tk()
    login_tk.geometry('300x200')
    login_tk.title('User Login')
    center_window(login_tk)

    # create new frame to contain the labels and entry boxes
    login_form = Frame(relief=SUNKEN, borderwidth=3)
    login_form.pack()

    username_login_label = Label(login_tk, text="Username:")
    username_login_label.grid(row=0, column=0)
    password_login_label = Label(login_tk, text="Password:")
    password_login_label.grid(row=1, column=0)

    username_login_entry = Entry(login_tk)
    username_login_entry.grid(row=0, column=1)

    password_login_entry = Entry(login_tk, show='*')
    # password_login_entry = Entry(login_tk)

    password_login_entry.grid(row=1, column=1)

    btn_login_submit = Button(master=login_tk, text="Login", command=lambda: user_login())
    btn_login_submit.grid(row=2, column=0)
    btn_login_close = Button(login_tk, text='Cancel', command=login_tk.destroy)
    btn_login_close.grid(row=2, column=1)

    def user_login():
        uname = username_login_entry.get().lower().strip()
        password = password_login_entry.get().strip()

        error_message, logged_in = DBHelper.auth_user(uname, password)
        if logged_in == "True":
            # destroy login form if successfully logged in
            login_tk.destroy()

        login_message_window(error_message)

    login_tk.mainloop()


def login_message_window(error_message):
    """ New window that show whether sign up is successful or not"""

    login_result_tk = Tk()
    login_result_tk.geometry('400x150')
    login_result_tk.title('User Register')
    center_window(login_result_tk)

    # Dynamically set message to show sign up confirmation
    message = ""
    if error_message == "":
        # There is no error if error message is empty
        message = "Log In Successful!"
    else:
        # Else message to be displayed is the error message
        message = error_message

    # Create label for message
    login_result_label = Label(login_result_tk, text=message)
    login_result_label.pack()

    # Create button for closing window
    btn_close = Button(login_result_tk, text='Close', command=login_result_tk.destroy)
    btn_close.pack()

    login_result_tk.mainloop()


def registration_window():
    """ This function is used to create new window that holds registration from """

    # Initialize New Window
    registration_tk = Tk()
    registration_tk.geometry('350x350')
    registration_tk.title('Registration Form')
    center_window(registration_tk)

    # create new frame to contain the labels and entry boxes
    frm_form = Frame(relief=SUNKEN, borderwidth=3)
    frm_form.pack()

    first_name_label = Label(registration_tk, text="First Name:")
    first_name_label.grid(row=0, column=0)
    last_name_label = Label(registration_tk, text="Last Name:")
    last_name_label.grid(row=1, column=0)
    username_label = Label(registration_tk, text="Username:")
    username_label.grid(row=2, column=0)
    email_label = Label(registration_tk, text="Email:")
    email_label.grid(row=3, column=0)
    password_label = Label(registration_tk, text="Password:")
    password_label.grid(row=4, column=0)
    password_confirm_label = Label(registration_tk, text="Confirm Password:")
    password_confirm_label.grid(row=5, column=0)

    first_name_entry = Entry(registration_tk)
    first_name_entry.grid(row=0, column=1)
    last_name_entry = Entry(registration_tk)
    last_name_entry.grid(row=1, column=1)
    username_entry = Entry(registration_tk)
    username_entry.grid(row=2, column=1)
    email_entry = Entry(registration_tk)
    email_entry.grid(row=3, column=1)
    password_entry = Entry(registration_tk, show='*')
    # password_entry = Entry(registration_tk)
    password_entry.grid(row=4, column=1)
    password_confirm_entry = Entry(registration_tk, show='*')
    password_confirm_entry.grid(row=5, column=1)

    btn_submit = Button(master=registration_tk, text="Submit",
                        command=lambda: user_register())
    btn_submit.grid(row=6, column=0)
    btn_close = Button(registration_tk, text='Close', command=registration_tk.destroy)
    btn_close.grid(row=6, column=1)

    def user_register():
        """
            Method for registration() for backend
            Note: This method is part of/inside of method registration()
        """
        # Get value from text boxes
        uname = username_entry.get()
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        pass1 = password_entry.get()
        pass2 = password_confirm_entry.get()
        email = email_entry.get()

        ### NEW NEW NEW ###
        # 2Dec Nieves, Chelsea
        # Modified flow so logic is in DBHelper rather than GUI (Fortune_Teller.py)
        error_message, registered = DBHelper.sign_up(uname, fname, lname, email, pass1, pass2) # Assign returned tuple 
        if registered == "True":
            # destroy registration form if successfully signed up
            registration_tk.destroy()

        # Call method to create new window that contains the confirmation/ error message
        registration_message_window(error_message)

    # Call to create registration_tk... END of registration TK
    registration_tk.mainloop()


def registration_message_window(error_message):
    """ New window that show whether sign up is successful or not"""

    submission_result_tk = Tk()
    submission_result_tk.geometry('400x150')
    submission_result_tk.title('User Register')
    center_window(submission_result_tk)

    # Dynamically set message to show sign up confirmation
    message = ""
    if error_message == "":
        # There is no error if error message is empty
        message = "Registration Successful! Please Log In"
    else:
        # Else message to be displayed is the error message
        message = error_message

    # Create label for message
    submission_result_label = Label(submission_result_tk, text=message)
    submission_result_label.pack()

    # Create button for closing window
    btn_close = Button(submission_result_tk, text='Close', command=submission_result_tk.destroy)
    btn_close.pack()

    submission_result_tk.mainloop()


def fortune_menu():
    """This menu will give the user the option to choose a category"""

    # Initialize New Window
    fortune_menu_tk = Tk()
    fortune_menu_tk.geometry('300x200')
    fortune_menu_tk.title('Fortune Menu')
    center_window(fortune_menu_tk)

    lbl = Label(fortune_menu_tk, text='Please select a category!')
    btn_love = Button(fortune_menu_tk, text='Love', command=lambda: display_fortune('Love'))
    btn_career = Button(fortune_menu_tk, text='Career', command=lambda: display_fortune('Career'))
    btn_health = Button(fortune_menu_tk, text='Health', command=lambda: display_fortune('Health'))
    btn_general = Button(fortune_menu_tk, text='General', command=lambda: display_fortune('General'))
    btn_random = Button(fortune_menu_tk, text='Random', command=lambda: display_fortune('Random'))

    lbl.pack()
    btn_love.pack()
    btn_career.pack()
    btn_health.pack()
    btn_general.pack()
    btn_random.pack()

    btn_previous_fortunes = Button(fortune_menu_tk, text='View Past Fortunes',
                                   command=lambda: past_fortunes_window())
    btn_previous_fortunes.pack()

    fortune_menu_tk.mainloop()


# 11/28/23 Hoi
# Needs work (Connect to Database to save fortune if user is logged in)
def display_fortune(category):
    """ Method to create a new window to display user's fortune based on the category they choose in fortune menu"""

    user_fortune = ""
    if category == 'Love':
        user_fortune = get_love_fortune()
    elif category == 'Career':
        user_fortune = get_career_fortune()
    elif category == 'General':
        user_fortune = get_general_fortune()
    elif category == 'Health':
        user_fortune = get_health_fortune()
    elif category == 'Random':
        user_fortune = get_random_fortune()

    # Initialize New Window
    fortune_tk = Tk()
    fortune_tk.title('Fortune Menu')
    fortune_tk.geometry('300x200')
    center_window(fortune_tk)

    lbl = Label(fortune_tk, text='Your Fortune', font='50')
    lbl.pack()
    lbl_category = Label(fortune_tk, text=category, font='40')
    lbl_category.pack()

    fortune_message = Message(fortune_tk, text=user_fortune)
    fortune_message.pack()

    btn_fortune_new = tk.Button(fortune_tk, text='New Fortune', bd='2', command=fortune_tk.destroy)
    btn_fortune_new.pack()
    btn_fortune_save = tk.Button(fortune_tk, text='Save', bd='2', command=lambda: save_fortune())
    btn_fortune_save.pack()

    def save_fortune():
        """ Method to save user's fortune """
        print("Need work! Saving user's fortune")

    fortune_tk.mainloop()


def past_fortunes_window():
    """ Method to create new window for displaying user's past fortunes """

    # Check if user is logged in
    username = "placeholder_username"

    def create_past_fortunes_table(data, win):
        """ method to create table in win with dynamic height (rows) from data """
        # Create table frame widget
        past_fortunes_table_frame = tk.Frame(win)
        past_fortunes_table_frame.grid(row=1, column=0, padx=10, pady=10)

        # past_fortunes_canvas = tk.Canvas(previous_fortunes_tk, borderwidth=0)
        scrollbar = Scrollbar(past_fortunes_table_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(past_fortunes_table_frame, yscrollcommand=scrollbar.set, width=75)
        for line in range(100):
            mylist.insert(END, "This is line number --------------------------------------" + str(line))
        mylist.pack(side=LEFT, fill=BOTH)
        #
        # total_rows = len(data)
        # total_columns = len(data[0])
        #
        # # code for creating table
        # for i in range(total_rows):
        #     for j in range(total_columns):
        #         e = tk.Entry(past_fortunes_table_frame, width=20, font=('Arial', 16, 'bold'))
        #         e.grid(row=i, column=j, sticky=W)
        #         e.insert(END, data[i][j])
        #         e.config(state=DISABLED)
        scrollbar.config(command=mylist.yview)

    # WIP Retrieve dataset from backend
    def get_past_fortunes_list(username):
        """ Method to get past fortunes from specific user"""
        # Placeholder list
        past_fortunes_list = [('11/28/2023', 'Good'),
                              ('11/28/2023', 'Bad'),
                              ('11/29/2023', '1'),
                              ('11/29/2023', '2'),
                              ('11/30/2023', '3'),
                              ('11/28/2023', 'Good'),
                              ('11/28/2023', 'Bad'),
                              ('11/29/2023', '1'),
                              ('11/29/2023', '2'),
                              ('11/30/2023', '3')]
        return past_fortunes_list

    # Initialize New Window
    previous_fortunes_tk = Tk()
    previous_fortunes_tk.title('Past Fortunes')
    previous_fortunes_tk.geometry('510x300')
    center_window(previous_fortunes_tk)

    # Username label
    username_label = Label(previous_fortunes_tk, text=username)
    username_label.grid(row=0, column=0)

    # Create table
    create_past_fortunes_table(get_past_fortunes_list(username), previous_fortunes_tk)

    # Button for Action
    btn_close = tk.Button(previous_fortunes_tk, text='Close', bd='5', command=previous_fortunes_tk.destroy)
    btn_close.grid(row=2, column=0)

    previous_fortunes_tk.mainloop()


def main_window():
    """Display Main Menu and Welcome Message"""

    DBHelper.create_table()
    print("Table created")
    # test_create_table()

    # create root window
    root = Tk()
    # root window and title dimensions
    root.title('Fortune Teller')
    # geometry of the box (width x height)
    root.geometry('650x400')
    # center window
    center_window(root)

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
    lbl1.pack()
    lbl2.pack()

    # add crystal ball ascii art
    crystal_ball_ascii_art(root)

    # # ask user if they want to play as a guest
    # lbl3 = Label(root, text='Would you like to login?')
    # lbl3.pack()
    #
    # # add buttons for user to select yes or no
    # btn_login_yes = tk.Button(root, text='Yes', bd='5', command=lambda: login_window())
    # btn_login_no = tk.Button(root, text='No', bd='5', command=lambda: guest_menu())
    # btn_login_yes.pack()
    # btn_login_no.pack()

    # Changed Buttons to include more options
    btn_play = tk.Button(root, text='Play as Guest', bd='1', command=lambda: fortune_menu())
    btn_login = tk.Button(root, text='Login', bd='1', command=lambda: login_window())
    btn_register = tk.Button(root, text='Register', bd='1', command=lambda: registration_window())

    btn_play.pack()
    btn_login.pack()
    btn_register.pack()

    # display menu
    root.config(menu=menubar)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_window()
