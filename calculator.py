<<<<<<< Updated upstream
"""This module has the Calculator class."""
=======
"""The main module for the pi-thon-calc.

This module sets up the root, and runs the set_up_all function.
"""
>>>>>>> Stashed changes
import tkinter as tk
from make_widgets import set_up_all


class Calculator:
    """Sets up the calculator.

<<<<<<< Updated upstream
    Run this file to run the calculator.
    """

    # TODO =>>
    # Make keyboard input work

    root = tk.Tk()  # <- initialize window.

    # Configuring window ==>
    root.title("\N{GREEK SMALL LETTER PI}-thon Calculator")  # <- set title.
    root.resizable(False, False)  # <- set window to non-resizable.
    root.geometry("275x375")  # <- set window size.
    root.rowconfigure(0, minsize=50, weight=1)  # <- set rows for buttons.
    root.columnconfigure([0, 1, 2], minsize=50, weight=1)  # <- set columns.
    root.configure(background="red")  # <- set window background.
    set_up_all(root)  # <- sets up all widgets, buttons, etc.
    root.mainloop()  # <- it's showtime!
=======
    root = tk.Tk()
    root.configure()

    # Configuring window
    root.title("\N{GREEK SMALL LETTER PI}-thon Calculator")
    root.resizable(False, False)
    root.minsize(260, 350)
    root.maxsize(260, 350)
    root.rowconfigure(0, minsize=50, weight=1)
    root.columnconfigure([0, 1, 2], minsize=50, weight=1)
    set_up_all(root)
    root.mainloop()
>>>>>>> Stashed changes
