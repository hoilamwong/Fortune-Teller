from tkinter import *
import random
from LogHandler import db_logger

LOVE_FORTUNE_PATH = "texts/love_fortune.txt"
CAREER_FORTUNE_PATH = "texts/career_fortune.txt"
GENERAL_FORTUNE_PATH = "texts/general_fortune.txt"
HEALTH_FORTUNE_PATH = "texts/health_fortune.txt"


def center_window(win):
    """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def crystal_ball_ascii_art(win):
    """ Function to add a label with crystal ball ascii art to window win"""

    def pad_to_center(l: list, w: int) -> str:
        """Helper Method for Manual centering ascii art"""
        padding = ' ' * (w // 2)  # a 1 char line would need at most w/2 spaces in front
        parts = [padding[0: (w - len(p)) // 2 + 1] + p for p in l]
        return '\n'.join(parts)

    crystal_ball_raw = r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠾⠛⠋⠉⠉⠉⠉⢙⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⣷⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣾⢇⣤⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⢹⣇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣤⡙⠻⢿⣿⣿⣿⣿⣿⣋⣠⣤⡶⠟⢁⣤⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⣤⣈⣉⠉⠛⠛⠉⣉⣠⣤⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣦⣀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢋⣠⣴⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⢿⣿⣿⣿⣷⣶⣤⣬⣭⣉⣉⣉⣩⣭⣥⣤⣶⣾⣿⣿⣿⡿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """

    crystal_ball_text = pad_to_center(crystal_ball_raw.split('\n'), 60)
    Label(win, justify=LEFT, text=crystal_ball_text).pack()


def get_love_fortune():
    try:
        fortune = []
        file1 = open(LOVE_FORTUNE_PATH, 'r')
        lines = file1.read().splitlines()

        for line in lines:
            fortune.append(line)
        return random.choice(fortune)
    except IOError as err:
        print('Unable to find file love_fortune.txt')
        db_logger.error(err)


def get_career_fortune():
    try:
        fortune = []
        file1 = open(CAREER_FORTUNE_PATH, 'r')
        lines = file1.read().splitlines()

        for line in lines:
            fortune.append(line)
        return random.choice(fortune)
    except IOError as err:
        print('Unable to find file career_fortune.txt')
        db_logger.error(err)


def get_health_fortune():
    try:
        fortune = []
        file1 = open(HEALTH_FORTUNE_PATH, 'r')
        lines = file1.read().splitlines()

        for line in lines:
            fortune.append(line)
        return random.choice(fortune)
    except IOError as err:
        print('Unable to find file health_fortune.txt')
        db_logger.error(err)


def get_general_fortune():
    try:
        fortune = []
        file1 = open(GENERAL_FORTUNE_PATH, 'r')
        lines = file1.read().splitlines()

        for line in lines:
            fortune.append(line)
        return random.choice(fortune)
    except IOError as err:
        print('Unable to find file general_fortune.txt')
        db_logger.error(err)


def get_random_fortune():
    fortune = []
    try:
        # Open multiple text files
        with open(LOVE_FORTUNE_PATH, 'r') as file_love, open(GENERAL_FORTUNE_PATH, 'r') as file_general, open(
                HEALTH_FORTUNE_PATH, 'r') as file_health, open(CAREER_FORTUNE_PATH, 'r') as file_career:
            # Read text files and split by line
            lines_love = file_love.read().splitlines()
            lines_general = file_general.read().splitlines()
            lines_health = file_health.read().splitlines()
            lines_career = file_career.read().splitlines()

            # Append lines to fortune
            for line in lines_love:
                fortune.append(line)
            for line in lines_general:
                fortune.append(line)
            for line in lines_health:
                fortune.append(line)
            for line in lines_career:
                fortune.append(line)
            return random.choice(fortune)
    except IOError as err:
        db_logger.error(err)
