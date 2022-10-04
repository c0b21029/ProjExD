import tkinter as tk
import tkinter.messagebox as tkm



def click_number(event): 
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num) 


def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)


root = tk.Tk()
root.geometry("400x700")

entry = tk.Entry(root, width=14, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=4)

r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
numbers = list(range(9, -1, -1)) # 数字だけのリスト
operators = ["+", "-", "/", "*", "**", "%"] # 演算子だけのリスト
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r+1, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0


# button1 = tk.Button(root, text="AC",font= ("", 30), width=4, height=2)
# button2 = tk.Button(root, text="%", font= ("", 30), width=4, height=2)
# button3 = tk.Button(root, text="√",font= ("", 30), width=4, height=2)
# button4 = tk.Button(root, text="/", font=("", 30), width=4, height=2)
# button5 = tk.Button(root, text="*", font=("", 30), width=4, height=2)
# button6 = tk.Button(root, text="-", font=("", 30), width=4, height=2)

# button2.bind("<1>", click_number)
# # button3.bind("<1>", click_number)
# button4.bind("<1>", click_number)
# button5.bind("<1>", click_number)
# button6.bind("<1>", click_number)

# button1.grid(row=1, column=0)
# button2.grid(row=1, column=1)
# button3.grid(row=1, column=2)
# button4.grid(row=1, column=3)
# button5.grid(row=2, column=3)
# button6.grid(row=3, column=3)

btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r+1, column=c)

root.mainloop()