"""This module has the Calculator class."""
import tkinter as tk
from make_widgets import set_up_all


class Calculator:
    """Sets up the calculator.

    Run this file to run the calculator.
    """

    # TODO:
    # Make square (x²) work. (x**2)
    # Change font sizes and families.
    # Make keyboard input work

    root = tk.Tk()
    root.configure(background="red")

    # Configuring window
    root.title("\N{GREEK SMALL LETTER PI}-thon Calculator")
    root.resizable(False, False)
    root.minsize(260, 350)
    root.maxsize(260, 350)
    root.rowconfigure(0, minsize=50, weight=1)
    root.columnconfigure([0, 1, 2], minsize=50, weight=1)
    set_up_all(root)
    root.mainloop()
