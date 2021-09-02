"""ModuleDocString."""
# import tkinter as tk
# from tkinter.constants import GROOVE, NSEW


# def init_all():
#     """Init all widgets."""
#     def on_click(value):
#         lbl_screen["text"] = value

#     # image = tk.PhotoImage(width=30, height=40)

#     # Button 0.
#     btn_zero = tk.Button(text="0", command=lambda: on_click("0"),
#                          compound="c")
#     btn_zero.grid(row=6, column=0, sticky=NSEW)

#     # Button 1.
#     btn_one = tk.Button(text="1", command=lambda: on_click("1"),
#                         compound="c")
#     btn_one.grid(row=5, column=0, sticky=NSEW)

#     # Button 2.
#     btn_two = tk.Button(text="2", command=lambda: on_click("2"),
#                         compound="c")
#     btn_two.grid(row=5, column=1, sticky=NSEW)

#     # Button 3.
#     btn_three = tk.Button(text="3", command=lambda: on_click("3"),
#                           compound="c")
#     btn_three.grid(row=5, column=2, sticky=NSEW)


# #     # Button 4.
# #     btn_four = tk.Button()

# #     # Button 5.
# #     btn_five = tk.Button()

# #     # Button 6.
# #     btn_six = tk.Button()

# #     # Button 7.
# #     btn_seven = tk.Button()

# #     # Button 8.
# #     btn_eight = tk.Button()

# #     # Button 9.
# #     btn_nine = tk.Button()

# #     # Plus sign.
# #     btn_plus = tk.Button()

# #     # Minus sign.
# #     btn_minus = tk.Button()

# #     # Times sign.
# #     btn_times = tk.Button()

# #     # Division sign.
# #     btn_divide = tk.Button()

# #     # Decimal point.
# #     btn_decimal = tk.Button()

# #     # Positive/Negative button.
# #     btn_posneg = tk.Button()

# #     # Square.
# #     btn_square = tk.Button()

# #     # Square Root
# #     btn_sqrt = tk.Button()

# #     # Pi.
# #     btn_pi = tk.Button()


# #     # Clear.
# #     btn_clear = tk.Button()

# #     # Enter.
# #     btn_enter = tk.Button()

# #     # Opening parentheses.
# #     btn_open_paren = tk.Button()

# #     # Closing parentheses.
# #     btn_close_paren = tk.Button()

# #     # Delete.
# #     btn_delete = tk.Button()

#     lbl_screen = tk.Label(root, text="", relief=GROOVE)
#     lbl_screen.grid(row=0, columnspan=4)


# root = tk.Tk()
# # Configuring window
# root.title("\N{GREEK SMALL LETTER PI}-thon Calculator")
# root.resizable(False, False)
# root.minsize(260, 350)
# root.maxsize(260, 350)
# root.rowconfigure(0, minsize=50, weight=1)
# root.columnconfigure([0, 1, 2], minsize=50, weight=1)
# init_all()

milav = "5+5+2*3.0"
if milav[-1] == '0' and milav[-2] == '.':
    print(milav[:-2])
else:
    print(milav)