import tkinter as tk
from tkinter import Toplevel


#login page 
def open_login_window(root):
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
