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

#2
button = [10]
for i in range(10):
    button = tk.Button(root,
                          font = ("", 30),
                          text = i)
    if i%3 == 0:
        button.grid(row = 12-(i+(i//3)), column = 0)
    elif i%3 == 2:
        button.grid(row = 8-(4*(i//3)), column = 2)
    elif i%3 == 1:
        button.grid(row = 8-(4*(i//3)), column = 4)
    
    #3
    button.bind("<1>", button_click)

root.mainloop()
