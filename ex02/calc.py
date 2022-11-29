import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    
    if txt == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else: 
        entry.insert(tk.END, txt)


root = tk.Tk()
root.title("calc.py")
root.geometry("400x500")


entry = tk.Entry(justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 6)


r, c = 1, 0
operators = ["+", "-", "*", "/", "=", "."]
for num in range(9, -3, -1):
    ope = operators[r-1]
    if num >= 0:
        button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
        button.grid(row=r, column=c)
    elif num == -2:
        button = tk.Button(root, text=f"{operators[num]}", width=4, height=2, font=("", 30))
        button.grid(row=r, column=c)
    elif num == -1:
        button = tk.Button(root, text=f"{operators[-1]}", width=4, height=2, font=("", 30))
        button.grid(row=r, column=c)
    else:
        button = tk.Button(root, text="", width=4, height=2, font=("", 30))
        button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
        button.grid(row=r, column=c)
        r += 1
        c = 0
        button.bind("<1>", button_click)


root.mainloop()
