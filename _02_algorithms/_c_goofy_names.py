"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    name = simpledialog.askstring(title=None, prompt="whats ur name?")
    goofy = ' '
    for i in range(len(name)):
        if name % 2 == 0:
            goofy + name[0].upper()
        else:
            goofy + name[0].lower()
    messagebox.showinfo(title='ur goofy name!', message=goofy)

    pass
