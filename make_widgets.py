"""Set up widgets, event handlers."""
import tkinter as tk
from tkinter import font
from tkinter.constants import CENTER, LEFT, NSEW, RAISED
from math import sqrt, pi

EXPRESSION = ""


def on_click(lbl_screen, value):
    """Append string on button click.

    For any numerical, operational, or functional button, appends the value of
    the button to the string. This is for clicking buttons.
    """
    global EXPRESSION
    EXPRESSION += value  # <- append user_input to global value EXPRESSION.
    lbl_screen["text"] = EXPRESSION  # <- display EXPRESSION.


def on_key_press(lbl_screen, event):
    """Append string.

    For any numerical, operational, or functional button, appends the value of
    the button to the string. This is for keyboard keys. Work In Progress.
    """
    global EXPRESSION
    EXPRESSION += str(event.char)

    lbl_screen["text"] = EXPRESSION


def clear(lbl_screen):
    """When the 'clear' button is clicked.

    Clears the screen, and string.
    """
    global EXPRESSION
    EXPRESSION = ""  # <- essentially clears EXPRESSION.
    lbl_screen["text"] = EXPRESSION  # <- display EXPRESSION.


def delete(lbl_screen):
    """When the 'delete' button is clicked.

    Deletes the last added character from the string.
    """
    global EXPRESSION
    EXPRESSION = EXPRESSION[
        :-1
    ]  # <- this deletes the last added character from EXPRESSION.
    lbl_screen["text"] = EXPRESSION  # <- display EXPRESSION.


def enter(lbl_screen):
    """When the '=' button is clicked.

    Evaluates the expression and displays result.
    """
    global EXPRESSION
    # replace instances of '²' with **2 -->
    EXPRESSION = EXPRESSION.replace("²", "**2")
    # replace pi symbol with 'pi' -->
    EXPRESSION = EXPRESSION.replace("\N{GREEK SMALL LETTER PI}", "pi")
    EXPRESSION = EXPRESSION.replace("√", "sqrt")  # <- replace '√' with 'sqrt'.

    # Catch ZeroDivisionError, SyntaxError ==>
    try:
        EXPRESSION = str(eval(EXPRESSION))  # evaluate
        if EXPRESSION != "0":
            if EXPRESSION[-1] == "0" and EXPRESSION[-2] == ".":
                # check if last characters in EXPRESSION is '.0' =>
                EXPRESSION = EXPRESSION[
                    :-2
                ]  # <- remove last two characters from EXPRESSION.
        lbl_screen["text"] = EXPRESSION

    except ZeroDivisionError:
        lbl_screen["text"] = "Zero Division Error"

    except SyntaxError:
        lbl_screen["text"] = "Syntax Error"
    lbl_screen["justify"] = CENTER

    # replace '²' with **2 ->
    EXPRESSION = EXPRESSION.replace("²", "**2")
    # replace pi symbol with 'pi' ->
    EXPRESSION = EXPRESSION.replace(
        "\N{GREEK SMALL LETTER PI}", "pi"
    )
    EXPRESSION = EXPRESSION.replace("√", "sqrt")  # <- replace '√' with 'sqrt'.


def set_up_all(root):
    """Set up all widgets."""
    # Set up the display ==>
    lbl_screen = tk.Label(  # basic configuration -->
        master=root,  # add widget to window.
        text="",  # set widget text.
        justify=LEFT,  # justify widget on left side.
        wraplength=250,  # set widget wraplength.
        bg='#ECEFF4',  # set widget background.
    )
    label_font = font.Font(family="JetBrains Mono", size=25)
    # assign widget spot on grid -->
    lbl_screen.grid(row=0, columnspan=4, sticky=NSEW)
    lbl_screen.configure(font=label_font)

    def btn_set_up(button, name, row, column, root, button_id="num"):
        """Set up buttons so I do not have to do them individually."""
        my_font = font.Font(family="JetBrains Mono", size=14)  # assign font.

        if button_id == "zero":  # if the button is the 0 button ==>
            button = tk.Button(
                master=root,  # <- add button to the window.
                text=name,  # <- set text to button's name.
                relief=RAISED,  # <- special relief (RAISED).
                # on click command =>
                command=lambda: on_click(lbl_screen, button["text"]),
                height=2,  # <- set button height.
            )
            # assign button spot on grid ->
            button.grid(row=row, column=column, columnspan=2, sticky=NSEW)

        if button_id == "num":  # if the button is any number that != 0 ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, name),
                height=2,  # set button height.
                highlightbackground="#D8DEE9",  # <- set color.
            )

        if button_id == "minus":  # if the button is the minus (-) button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text="−",  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, "-"),
                height=2,  # set button height.
            )

        if button_id == "multiply":  # if button is the times (*) button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text="×",  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, "*"),
                height=2,  # set button height.
            )

        if button_id == "divide":  # if the button is the divide (/) button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, "/"),
                height=2,  # set button height.
            )

        if button_id == "clear":  # if the button is the clear button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: clear(lbl_screen),
                height=2,  # set button height.
                fg="#BF616A",  # set text color.
            )

        if button_id == "delete":  # if button is the delete button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: delete(lbl_screen),
                height=2,  # set button height.
            )

        if button_id == "enter":  # if button is the enter button ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: enter(lbl_screen),
                height=2,  # set button height.
            )

        if button_id == "square":  # if button is the ² button (^2) ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, "²"),
                height=2,  # set button height.
            )

        if button_id == "sqrt":  # if button is the √ button (sqrt) ==>
            button = tk.Button(
                master=root,  # add button to window.
                text=name,  # set button text as name.
                relief=RAISED,  # set button relief.
                # on click command =>
                command=lambda: on_click(lbl_screen, "√("),
                height=2,  # set button height.
            )

        # for all buttons => set font, highlightthickness, and grid location.
        button.configure(
            highlightthickness=3, font=my_font, highlightbackground="#D8DEE9"
        )
        button.grid(row=row, column=column, sticky=NSEW)

        if button_id != "clear":
            button["fg"] = "#2E3440"

    # Initializing Buttons ==>
    # this part is mostly repetitive, therefore I will only comment
    # for Button 0.

    # Button 0 ==>
    btn_zero = tk.Button()  # initialize button.
    btn_zero.grid(columnspan=2)  # have button take up 2 columns.
    # info sent is widget_name, button_name, grid_placement, master, id -->
    btn_set_up(btn_zero, "0", 6, 0, root, "zero")  # send info to btn_set_up.

    # Button 1.
    btn_one = tk.Button()
    btn_set_up(btn_one, "1", 5, 0, root)

    # Button 2.
    btn_two = tk.Button()
    btn_set_up(btn_two, "2", 5, 1, root)

    # Button 3.
    btn_three = tk.Button()
    btn_set_up(btn_three, "3", 5, 2, root)

    # Button 4.
    btn_four = tk.Button()
    btn_set_up(btn_four, "4", 4, 0, root)

    # Button 5.
    btn_five = tk.Button()
    btn_set_up(btn_five, "5", 4, 1, root)

    # Button 6.
    btn_six = tk.Button()
    btn_set_up(btn_six, "6", 4, 2, root)

    # Button 7.
    btn_seven = tk.Button()
    btn_set_up(btn_seven, "7", 3, 0, root)

    # Button 8.
    btn_eight = tk.Button()
    btn_set_up(btn_eight, "8", 3, 1, root)

    # Button 9.
    btn_nine = tk.Button()
    btn_set_up(btn_nine, "9", 3, 2, root)

    # Plus sign.
    btn_plus = tk.Button()
    btn_set_up(btn_plus, "+", 5, 3, root)

    # Minus sign.
    btn_minus = tk.Button()
    btn_set_up(btn_minus, "-", 4, 3, root, "minus")
    btn_minus["text"] = "－"

    # Times sign.
    btn_times = tk.Button()
    btn_set_up(btn_times, "x", 3, 3, root, "multiply")

    # Division sign.
    btn_divide = tk.Button()
    btn_set_up(btn_divide, "÷", 2, 3, root, "divide")

    # Decimal point.
    btn_decimal = tk.Button()
    btn_set_up(btn_decimal, ".", 6, 2, root)

    # Square.
    btn_square = tk.Button()
    btn_set_up(btn_square, "x²", 2, 0, root, "square")

    # Square Root
    btn_sqrt = tk.Button()
    btn_set_up(btn_sqrt, "√", 2, 1, root, "sqrt")

    # Pi.
    btn_pi = tk.Button()
    btn_set_up(btn_pi, "\N{GREEK SMALL LETTER PI}", 2, 2, root)

    # Clear.
    btn_clear = tk.Button()
    btn_set_up(btn_clear, "Clear", 1, 2, root, button_id="clear")

    # Enter.
    btn_enter = tk.Button()
    btn_set_up(btn_enter, "=", 6, 3, root, "enter")

    # Opening parentheses.
    btn_open_paren = tk.Button()
    btn_set_up(btn_open_paren, "(", 1, 0, root)

    # Closing parentheses.
    btn_close_paren = tk.Button()
    btn_set_up(btn_close_paren, ")", 1, 1, root)

    # Delete.
    btn_delete = tk.Button()
    btn_set_up(btn_delete, " Del ", 1, 3, root, button_id="delete")
