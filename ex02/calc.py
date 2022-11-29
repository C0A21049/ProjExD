import tkinter as tk
import tkinter.messagebox as tkm
#3
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt, f"[{txt}のボタンがクリックされました]")
    #6
    entry.insert(tk.END, num)

#1
root = tk.Tk()
root.title("calc.py")
root.geometry("300x500")

#4
entry = tk.Entry(justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

#2
r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
    
    #3
    button.bind("<1>", button_click)

#5
operators = ["+", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
    #6
    button.bind("<1>", button_click)

root.mainloop()
