"""Set up widgets, event handlers."""
import tkinter as tk
from tkinter import font
from tkinter.constants import GROOVE, LEFT, NSEW, RAISED
from math import sqrt, pi

EXPRESSION = ""


def on_click(lbl_screen, value):
    """DSTRING."""
    global EXPRESSION
    EXPRESSION += value

    lbl_screen["text"] = EXPRESSION

def on_key_press(lbl_screen, event):
    """DSTRING."""
    global EXPRESSION
    EXPRESSION += str(event.char)

    lbl_screen["text"] = EXPRESSION


def clear(lbl_screen):
    """DSTRING."""
    global EXPRESSION
    EXPRESSION = ""
    lbl_screen["text"] = EXPRESSION


def delete(lbl_screen):
    """DSTR."""
    global EXPRESSION
    EXPRESSION = EXPRESSION[:-1]
    lbl_screen["text"] = EXPRESSION


def enter(lbl_screen):
    """DSTR."""
    global EXPRESSION

    # Catch ZeroDivisionError:
    try:
        EXPRESSION = str(eval(EXPRESSION))
        if EXPRESSION[-1] == '0' and EXPRESSION[-2] == '.':
            EXPRESSION = EXPRESSION[:-2]
        lbl_screen["text"] = EXPRESSION
    except ZeroDivisionError:
        lbl_screen["text"] = "Zero Division Error"
    except SyntaxError:
        lbl_screen["text"] = "Syntax Error"


def set_up_all(root):
    """Set up all widgets."""
    lbl_screen = tk.Label(root, text="", relief=GROOVE, justify=LEFT,
                          wraplength=210, bg='#e7f5fe')
    lbl_screen["font"] = 'Courier 30'
    lbl_screen.grid(row=0, columnspan=4, sticky=NSEW)

    def btn_set_up(button, name, row, column, root, button_id="numerical"):
        """Set up buttons so I do not have to do them individually."""
        # Set Up:
        my_font = font.Font(family='Courier 20 bold')


        if button_id == 'zero':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: on_click(lbl_screen,
                                                        button["text"]),
                               height=2)
            button.grid(row=row, column=column, columnspan=2, sticky=NSEW)

        if button_id == 'numerical':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: on_click(lbl_screen,
                                                        button["text"]),
                               height=2)

        if button_id == 'clear':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: clear(lbl_screen),
                               height=2)

        if button_id == 'delete':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: delete(lbl_screen),
                               height=2)

        if button_id == 'enter':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: enter(lbl_screen),
                               height=2)

        if button_id == 'square':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: on_click(lbl_screen, '²'),
                               height=2)

        if button_id == 'sqrt':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: on_click(lbl_screen, 'sqrt('),
                               height=2)

        if button_id == 'pi':
            button = tk.Button(master=root, text=name, relief=RAISED,
                               command=lambda: on_click(
                                   lbl_screen, '3.141592'),
                               height=2)
        button.configure(highlightthickness=2)
        button.grid(row=row, column=column, sticky=NSEW)
        button['font'] = my_font

    # Button 0.
    btn_zero = tk.Button()
    btn_zero.grid(columnspan=2)
    btn_set_up(btn_zero, '0', 6, 0, root, 'zero')
    btn_zero.bind("0", lambda: on_key_press(lbl_screen))

    # Button 1.
    btn_one = tk.Button()
    btn_set_up(btn_one, '1', 5, 0, root)

    # Button 2.
    btn_two = tk.Button()
    btn_set_up(btn_two, '2', 5, 1, root)

    # Button 3.
    btn_three = tk.Button()
    btn_set_up(btn_three, '3', 5, 2, root)

    # Button 4.
    btn_four = tk.Button()
    btn_set_up(btn_four, '4', 4, 0, root)

    # Button 5.
    btn_five = tk.Button()
    btn_set_up(btn_five, '5', 4, 1, root)

    # Button 6.
    btn_six = tk.Button()
    btn_set_up(btn_six, '6', 4, 2, root)

    # Button 7.
    btn_seven = tk.Button()
    btn_set_up(btn_seven, '7', 3, 0, root)

    # Button 8.
    btn_eight = tk.Button()
    btn_set_up(btn_eight, '8', 3, 1, root)

    # Button 9.
    btn_nine = tk.Button()
    btn_set_up(btn_nine, '9', 3, 2, root)

    # Plus sign.
    btn_plus = tk.Button()
    btn_set_up(btn_plus, '+', 5, 3, root)

    # Minus sign.
    btn_minus = tk.Button()
    btn_set_up(btn_minus, '-', 4, 3, root)

    # Times sign.
    btn_times = tk.Button()
    btn_set_up(btn_times, '*', 3, 3, root)

    # Division sign.
    btn_divide = tk.Button()
    btn_set_up(btn_divide, '/', 2, 3, root)

    # Decimal point.
    btn_decimal = tk.Button()
    btn_set_up(btn_decimal, '.', 6, 2, root)

    # Square.
    btn_square = tk.Button()
    btn_set_up(btn_square, 'x²', 2, 0, root, button_id='square')

    # Square Root
    btn_sqrt = tk.Button()
    btn_set_up(btn_sqrt, '√', 2, 1, root, button_id='sqrt')

    # Pi.
    btn_pi = tk.Button()
    btn_set_up(btn_pi, '\N{GREEK SMALL LETTER PI}', 2, 2,
               root, button_id='pi')

    # Clear.
    btn_clear = tk.Button()
    btn_set_up(btn_clear, 'CLEAR', 1, 2, root, button_id='clear')

    # Enter.
    btn_enter = tk.Button()
    btn_set_up(btn_enter, '=', 6, 3, root, 'enter')

    # Opening parentheses.
    btn_open_paren = tk.Button()
    btn_set_up(btn_open_paren, '(', 1, 0, root)

    # Closing parentheses.
    btn_close_paren = tk.Button()
    btn_set_up(btn_close_paren, ')', 1, 1, root)

    # Delete.
    btn_delete = tk.Button()
    btn_set_up(btn_delete, 'DELETE', 1, 3, root, button_id='delete')
