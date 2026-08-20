import tkinter as tk
from database import check_login, register_user

def show_result(parent, title, message):

    result_window = tk.Toplevel(parent)

    result_window.title(title)
    result_window.geometry("250x120")

    tk.Label(
        result_window,
        text=message,
        font=("Arial", 12)
    ).pack(pady=20)

    confirm_button = tk.Button(
        result_window,
        text="Confirm",
        width=8,
        command=result_window.destroy
    )

    confirm_button.pack()

def open_login_window(root):

    login_window = tk.Toplevel(root)

    login_window.title("Sign in")
    login_window.geometry("300x175")

    # Username
    tk.Label(login_window,text="Username:").grid(row=0, column=0, padx=10, pady=10)

    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password
    tk.Label(login_window,text="Password:").grid(row=1, column=0, padx=10, pady=10)

    password_entry = tk.Entry(login_window,show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Login
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "1234":show_result("Login successful!")
        else:show_result("Incorrect username or password.")


    #Login button
    login_button = tk.Button(login_window,text="Login",width=8,command=login)
    login_button.grid(row=2,column=1,pady=10)

#sign up
def open_signup_window(root):

    signup_window = tk.Toplevel(root)

    signup_window.title("Sign up")

    signup_window.geometry("300x230")


    # Username

    tk.Label(
        signup_window,
        text="Username:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    username_entry = tk.Entry(
        signup_window
    )

    username_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )


    # Password

    tk.Label(
        signup_window,
        text="Password:"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    password_entry = tk.Entry(
        signup_window,
        show="*"
    )

    password_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )


    # Confirm password

    tk.Label(
        signup_window,
        text="Confirm:"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10
    )

    confirm_entry = tk.Entry(
        signup_window,
        show="*"
    )

    confirm_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )


    # ======================================
    # Sign Up
    # ======================================

    def signup():

        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_entry.get()


        # Empty fields

        if username == "" or password == "":

            show_result(
                signup_window,
                "Sign up",
                "Please fill in all fields."
            )

            return


        # Check passwords

        if password != confirm_password:

            show_result(
                signup_window,
                "Sign up",
                "Passwords do not match."
            )

            return


        # Add user to database

        if register_user(username, password):

            show_result(
                signup_window,
                "Sign up",
                "Sign up successful!"
            )

            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            confirm_entry.delete(0, tk.END)

        else:

            show_result(
                signup_window,
                "Sign up",
                "Username already exists."
            )


    # Sign Up button

    signup_button = tk.Button(
        signup_window,
        text="Sign Up",
        width=8,
        command=signup
    )

    signup_button.grid(
        row=3,
        column=1,
        pady=10
    )