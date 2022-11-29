import tkinter as tk
import tkinter.messagebox as tkm
#3
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}のボタンがクリックされました]")

#1
root = tk.Tk()
root.title("calc.py")
root.geometry("300x500")

#4
entry = tk.Entry(justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

#2
button = [10]
for i in range(10):
    button = tk.Button(root,
                          font = ("", 30),
                          text = i)
    if i%3 == 0:
        button.grid(row = 13-(i+(i//3)), column = 0)
    elif i%3 == 2:
        button.grid(row = 9-(4*(i//3)), column = 1)
    elif i%3 == 1:
        button.grid(row = 9-(4*(i//3)), column = 2)
    
    #3
    button.bind("<1>", button_click)

root.mainloop()
