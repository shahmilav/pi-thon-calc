"""module docstring."""
import tkinter as tk
import make_widgets


class Calculator:
    """Calc."""

    root = tk.Tk()
    root.configure(bg = "red")

    # Configuring window
    root.title("\N{GREEK SMALL LETTER PI}-thon Calculator")
    root.resizable(False, False)
    root.minsize(260, 350)
    root.maxsize(260, 350)
    root.rowconfigure(0, minsize=50, weight=1)
    root.columnconfigure([0, 1, 2], minsize=50, weight=1)
    make_widgets.set_up_all(root)
    root.mainloop()


    # TODO:
    # Make square (x^2) work. (x**2)
    # Change colors of the calculator.
    # Change font sizes and families.
    # Make keyboard input work
