import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "w":
        cy -= 20
    if key == "s":
        cy += 20
    if key == "a":
        cx -= 20
    if key == "d":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = "" #現在押されているキーを表す変数

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    #練習9
    maze_list = mm.make_maze(15, 9)
    print(maze_list)

    root = tk.mainloop()