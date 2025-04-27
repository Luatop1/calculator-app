import tkinter as tk
import math

def solve():
    try:
        res = eval(calc.get())
        calc.delete(0, "end")
        calc.insert(0, res)
    except:
        calc.delete(0, "end")
        calc.insert(0, "Ошибка")

def add_num(btn):
    if btn["text"] != "√" and btn["text"] != "π" and btn["text"] != "e":
        try:
            if calc.get()[len(calc.get()) - 1] == "(":
                calc.insert(len(calc.get()), f"{btn["text"]})")
            else:
                calc.insert(len(calc.get()), btn["text"])
        except IndexError:
            calc.insert(len(calc.get()), btn["text"])
    else:
        if btn["text"] == "√":
            calc.insert(len(calc.get()), "math.sqrt(")
        elif btn["text"] == "π":
            calc.insert(len(calc.get()), "3.14159265359")
        elif btn["text"] == "e":
            calc.insert(len(calc.get()), "2.71828182846")

root = tk.Tk()

root["bg"] = "#DADADA"
root.geometry("190x212")
root.resizable(False, False)

calc = tk.Entry(root, borderwidth=4, width=29)
calc.place(x=3, y=5)

btn_1 = tk.Button(root, text="1", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_1))
btn_1.place(x=5, y=35)

btn_2 = tk.Button(root, text="2", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_2))
btn_2.place(x=5, y=80)

btn_3 = tk.Button(root, text="3", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_3))
btn_3.place(x=5, y=125)

btn_4 = tk.Button(root, text="4", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_4))
btn_4.place(x=43, y=35)

btn_5 = tk.Button(root, text="5", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_5))
btn_5.place(x=43, y=80)

btn_6 = tk.Button(root, text="6", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_6))
btn_6.place(x=43, y=125)

btn_7 = tk.Button(root, text="7", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_7))
btn_7.place(x=80, y=35)

btn_8 = tk.Button(root, text="8", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_8))
btn_8.place(x=80, y=80)

btn_9 = tk.Button(root, text="9", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_9))
btn_9.place(x=80, y=125)

btn_0 = tk.Button(root, text="0", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_0))
btn_0.place(x=117, y=35)

btn_clear = tk.Button(root, text="☓", height=1, width=2, font=("Arial", 14, "bold"), bg="#FF4444", command=lambda: calc.delete(0, "end"))
btn_clear.place(x=155, y=36)

btn_calc = tk.Button(root, text="=", height=1, width=2, font=("Arial", 15), padx=1.5, command=lambda: solve())
btn_calc.place(x=155, y=80)

btn_plus = tk.Button(root, text="+", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_plus))
btn_plus.place(x=156, y=125)

btn_minus = tk.Button(root, text="-", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_minus))
btn_minus.place(x=117, y=80)

btn_sqrt = tk.Button(root, text="√", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_sqrt))
btn_sqrt.place(x=117, y=125)

btn_multipy = tk.Button(root, text="*", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_multipy))
btn_multipy.place(x=117, y=170)

btn_divide = tk.Button(root, text="/", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_divide))
btn_divide.place(x=156, y=170)

btn_pi = tk.Button(root, bg="#E5E5E5", text="π", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_pi))
btn_pi.place(x=80, y=170)

btn_eller = tk.Button(root, bg="#E5E5E5", text="e", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_eller))
btn_eller.place(x=43, y=170)

btn_dot = tk.Button(root, bg="#E5E5E5", text=".", height=1, width=2, font=("Arial", 15), command=lambda: add_num(btn_dot))
btn_dot.place(x=5, y=170)

root.mainloop()