import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
root = tk.Tk()

from database import init_database, get_subjects, get_recommendations
from login import open_login_window, open_signup_window
init_database()

root.title("app")
root.geometry('800x400')
#login
signin_button = tk.Button(root,text="sign in", width=6, command=lambda: open_login_window(root))
signin_button.place(relx=1.0, x=-110, y=0, anchor="ne")
#sign up
signup_button = tk.Button(root,text="sign up",width=6,command=lambda: open_signup_window(root))
signup_button.place(relx=1.0,x=-20,y=0,anchor="ne")

#search bar & search entery
search_frame = tk.Frame(root)
search_frame.grid(row=0, column=0, columnspan=5)

root.columnconfigure(0, weight=1)
tk.Label(search_frame, text="search bar").pack(side="left", padx=5)
entry1 = tk.Entry(search_frame)
entry1.pack(side="left", padx=5)
#divider
divider = tk.Frame(root, height=50, bg="grey")
divider.grid(row=2, column=0, columnspan=5, sticky="ew", pady=10)
#texts in divider
label = tk.Label(
    divider, text="Welcome to the Subject Advice App", bg="grey", font=("Arial", 14, "bold"))
label.place(relx=0.5, rely=0.5, anchor="center")

#left enter
left_frame = tk.Frame(root)
left_frame.grid(row=3, column=0, sticky="nw", padx=10, pady=10)

tk.Label(left_frame, text="Select subject:").pack(anchor="w")
subject = ttk.Combobox(
    left_frame,
    values=get_subjects(),
    state="readonly",
    width=12)
subject.pack(anchor="w", pady=5)


#six frames/buttons
#frame 1
frame_1 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_1.grid(row=3, column=1, padx=(0, 40) )
frame_1.grid_propagate(False)
button_1 = tk.Button(frame_1, text="subject", bg="grey", relief=tk.FLAT)
button_1.place(relx=0, rely=0, relwidth=1, relheight=1)
#frame2
frame_2 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_2.grid(row=3, column=2, padx=(0, 40) )
frame_2.grid_propagate(False)
button_2 = tk.Button(frame_2, text="subject", bg="grey", relief=tk.FLAT)
button_2.place(relx=0, rely=0, relwidth=1, relheight=1)
#frame 3
frame_3 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_3.grid(row=3, column=3, padx=(0, 40) )
frame_3.grid_propagate(False)
button_3 = tk.Button(frame_3, text="subject", bg="grey", relief=tk.FLAT)
button_3.place(relx=0, rely=0, relwidth=1, relheight=1)
#frame 4
frame_4 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_4.grid(row=4, column=1, padx=(0, 40) )
frame_4.grid_propagate(False)
button_4 = tk.Button(frame_4, text="subject", bg="grey", relief=tk.FLAT)
button_4.place(relx=0, rely=0, relwidth=1, relheight=1)
#frame 5
frame_5 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_5.grid(row=4, column=2, padx=(0, 40) )
frame_5.grid_propagate(False)
button_5 = tk.Button(frame_5, text="subject", bg="grey", relief=tk.FLAT)
button_5.place(relx=0, rely=0, relwidth=1, relheight=1)
#frame 6
frame_6 = tk.Frame(root, bg="grey", width=100, height=50, bd=3, relief=tk.RIDGE)
frame_6.grid(row=4, column=3, padx=(0, 40) )
frame_6.grid_propagate(False)
button_6 = tk.Button(frame_6, text="subject", bg="grey", relief=tk.FLAT)
button_6.place(relx=0, rely=0, relwidth=1, relheight=1)

def add_hover(btn):
    btn.bind("<Enter>", lambda e: btn.config(bg="#d9d9d9"))
    btn.bind("<Leave>", lambda e: btn.config(bg="grey"))
for b in [button_1, button_2, button_3, button_4, button_5, button_6]:
    add_hover(b)

buttons = [ button_1, button_2, button_3, button_4, button_5, button_6]
def update_buttons(event=None):
    selected_subject = subject.get()
    recommendations = get_recommendations(selected_subject)
    for i in range(6):
        if i < len(recommendations):
            buttons[i].config(text=recommendations[i])
        else:
            buttons[i].config(text="")

subject.bind("<<ComboboxSelected>>", update_buttons)

def open_button_window():
    button_window = Toplevel(root)  # Create a new window
    button_window.title("")
    button_window.geometry("300x210")  

    exit_button = tk.Button(button_window, text="conform", width=5, command=button_window.destroy)
    exit_button.grid(row=2, column=1)

root.mainloop()