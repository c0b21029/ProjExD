import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

def click_number(event):
    btn = event.widget
    num = int(btn["text"])
    tkm.showinfo(f"{num}", f"[{num}]ボタンが押されました")

r, c = 0, 0
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

root.mainloop()