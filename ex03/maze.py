import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    if key == "w":
        my -= 1
    if key == "s":
        my += 1
    if key == "a":
        mx -= 1
    if key == "d":
        mx += 1
    cx, cy = mx*100+50, my*100+50
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    #練習9,10
    maze_list = mm.make_maze(15, 9)
    # print(maze_list)
    mm.show_maze(canv, maze_list)

    tori = tk.PhotoImage(file="fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = "" #現在押されているキーを表す変数

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    


    root = tk.mainloop()