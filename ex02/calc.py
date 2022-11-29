import tkinter as tk
import tkinter.messagebox as tkm

next = True
r, c = 1, 0
result = []
res = 0


root = tk.Tk()
root.title("calc.py")
root.geometry("374x700")


entry = tk.Entry(justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 6)


def history():
    rh = r
    for res in result:
        label = tk.Label(root, text=f"%d回目:{res}"%(rh-r+1), font=("", 15))
        label.grid(row=rh)
        rh += 1


def button_click(event):
    global next, res

    btn = event.widget
    txt = btn["text"]
    
    if txt == "=":
        siki = entry.get()
        try:
            res = eval(siki)
        except:
            tkm.showwarning("警告", "計算できません\n式を入れなおしてください")
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
        result.append(res)
        history()
    else: 
        entry.insert(tk.END, txt)


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
        button = tk.Button(root, text=f"{operators[num]}", width=4, height=2, font=("", 30))
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
