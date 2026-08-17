import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
root = tk.Tk()

root.title("V1 of the app")
root.geometry('800x400')
#登入栏
def open_login_window():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("sign in")
    new_window.geometry("300x175")  

    tk.Label(new_window, text="username").grid(row=0, column=0)
    tk.Label(new_window, text="password").grid(row=1, column=0) 
    entry1 = tk.Entry(new_window)
    entry2 = tk.Entry(new_window)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    button = tk.Button(new_window, text="conform", width=5, command=new_window.destroy)
    button.grid(row=2, column=1)


button = tk.Button(root, text="sign in", width=5, command=open_login_window)
button.place(relx=1.0, x=-20, y=0, anchor="ne") 
#搜索栏
search_frame = tk.Frame(root)
search_frame.grid(row=0, column=0, columnspan=5)

root.columnconfigure(0, weight=1)
tk.Label(search_frame, text="search bar").pack(side="left", padx=5)
entry1 = tk.Entry(search_frame)
entry1.pack(side="left", padx=5)
#分割栏
divider = tk.Frame(root, height=50, bg="grey")
divider.grid(row=2, column=0, columnspan=5, sticky="ew", pady=10)
#分割栏中的文字
label = tk.Label(
    divider, text="Welcome to the Subject Advice App", bg="grey", font=("Arial", 14, "bold"))
label.place(relx=0.5, rely=0.5, anchor="center")

#左侧输入
left_frame = tk.Frame(root)
left_frame.grid(row=3, column=0, sticky="nw", padx=10, pady=10)

tk.Label(left_frame, text="Select subject:").pack(anchor="w")
subject = ttk.Combobox(
    left_frame,
    values=["subject-A", "subject-B", "subject-C", "subject-D"],
    state="readonly",
    width=12)
subject.pack(anchor="w", pady=5)

#六个小窗
#1
frame_1 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_1.grid(row=3, column=1, padx=(0, 40) )
frame_1.grid_propagate(False)
label_1 = tk.Label(frame_1, text="Frame 1", bg="grey")
label_1.grid(row=0,column=0, padx=(0, 40))
#2
frame_2 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_2.grid(row=3, column=2, padx=(0, 40))
frame_2.grid_propagate(False)
label_2 = tk.Label(frame_2, text="Frame 2", bg="grey")
label_2.grid(row=0,column=0, padx=(0, 40))
#4
frame_3 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_3.grid(row=3, column=3, padx=(0, 40))
frame_3.grid_propagate(False)
label_3 = tk.Label(frame_3, text="Frame 3", bg="grey")
label_3.grid(row=0,column=0, padx=(0, 40))
#4
frame_4 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_4.grid(row=4, column=1, padx=(0, 40) )
frame_4.grid_propagate(False)
label_4 = tk.Label(frame_4, text="Frame 4", bg="grey")
label_4.grid(row=0,column=0, padx=(0, 40))
#5
frame_5 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_5.grid(row=4, column=2, padx=(0, 40))
frame_5.grid_propagate(False)
label_5 = tk.Label(frame_5, text="Frame 5", bg="grey")
label_5.grid(row=0,column=0, padx=(0, 40))
#6
frame_6 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_6.grid(row=4, column=3, padx=(0, 40))
frame_6.grid_propagate(False)
label_6 = tk.Label(frame_6, text="Frame 6", bg="grey")
label_6.grid(row=0,column=0, padx=(0, 40))
root.mainloop()