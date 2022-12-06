import tkinter as tk

#8
import random
import maze_maker as mm

def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = [[1 for i in range(tate)] for j in range(yoko)]  #大きさがtate*yokoの「1」の2次元リスト
    for maze_yoko in range(1, len(maze_lst)-1): #壁ではない部分を0にする
        for cell in range(1, len(maze_lst[0])-1):
            maze_lst[maze_yoko][cell] = 0
    for y in range(2, tate-2, 2): #迷路を作る
        for x in range(2, yoko-2, 2):
            maze_lst[x][y] = 1
            if x > 2:
                rnd = random.randint(0, 2)
            else:
                rnd = random.randint(0, 3)
            maze_lst[x+YP[rnd]][y+XP[rnd]] = 1
    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for x in range(len(maze_lst)):
        for y in range(len(maze_lst[x])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill=color[maze_lst[x][y]])
    #ゴール位置の設定
    x = 13
    y = 7
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="red")
    #スタート位置の設定
    x = 1
    y = 1
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="blue")
#迷路を描写する関数
def re_make_maze():
    global maze
    #9
    maze = mm.make_maze(15,9)
    #10
    show_maze(canvas, maze)
#7#11
def main_proc():
    global mx, my, cx, cy, tmr, job, tmp, key, kokaton
    #開始時にタイマー起動
    if job == True:
        label["text"] = "今回の記録:"+str(round(tmr,1))+"前回の記録:"+str(round(tmp,1))
        tmr = tmr + 0.1
    #キーによる移動
    if key == "Up" and maze[mx][my-1] == 0:
        my -= 1
    if key == "Down" and maze[mx][my+1] == 0:
        my += 1
    if key == "Left" and maze[mx-1][my] == 0:
        mx -= 1
    if key == "Right" and maze[mx+1][my] == 0:
        mx += 1
    #ゴールの判定
    if mx == 13 and my == 7:
        key = "r"
        #ゴールした後次のステージに行く
        re_make_maze()
        cx = mx*100 + 50
        cy = my*100 + 50
        canvas.coords(
            "kokaton",
            cx,
            cy,
        )
    #rキーを押すことでリセットを行う
    if key == "r":
        mx = 1
        my = 1
        tmp = tmr
        tmr = 0.0
        label["text"] = "今回の記録:"+str(round(tmr,1))+"前回の記録:"+str(round(tmp,1))
    #tキーを押すことでタイマー機能を稼働させる。
    if key == "t" and job == None:
        label["text"] = "今回の記録:"+str(round(tmr,1))+"前回の記録:"+str(round(tmp,1))
        tmr = tmr + 0.1
        job = True
    #タイマー機能の一時停止
    elif key == "t" and job == True:
        job = None
    cx = mx*100 + 50
    cy = my*100 + 50
    kokaton = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(cx,cy,image=kokaton, tag="kokaton")
    root.after(100,main_proc)
#5
def key_down(event):
    global key
    key = event.keysym
#6
def key_up(event):
    global key
    key = ""

#1
if __name__ == "__main__":
    root = tk.Tk()
    #時間経過を表示するラベル
    tmr = 0.0
    tmp = 0.0
    job = True
    label = tk.Label(root, font=("",50))
    label["text"] = "今回の記録:"+str(round(tmr,1))+"前回の記録:"+str(round(tmr,1))
    label.pack()
    #1
    root.title("迷えるこうかとん")
    root.geometry("1500x1000")
    #3#11
    mx = 1
    my = 1
    cx = mx*100 + 50
    cy = my*100 + 50
    #2
    canvas = tk.Canvas(
        root,
        width=1500,
        height=900,
        bg="black")
    #4
    key = ""
    #5
    root.bind("<KeyPress>", key_down)
    #6
    root.bind("<KeyRelease>", key_up)
    #7
    main_proc()
    re_make_maze()
    #3
    kokaton = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(cx,cy,image=kokaton, tag="kokaton")
    #2
    canvas.pack()

    root.mainloop()
