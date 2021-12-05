"""This module has the Calculator class."""
import tkinter as tk
from make_widgets import set_up_all


class Calculator:
    """Sets up the calculator.

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
