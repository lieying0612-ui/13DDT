import tkinter as tk


def open_login_window(root):

    login_window = tk.Toplevel(root)

    login_window.title("Sign in")
    login_window.geometry("300x175")

    # Username
    tk.Label(
        login_window,
        text="Username:"
    ).grid(row=0, column=0, padx=10, pady=10)

    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password
    tk.Label(
        login_window,
        text="Password:"
    ).grid(row=1, column=0, padx=10, pady=10)

    password_entry = tk.Entry(
        login_window,
        show="*"
    )
    password_entry.grid(row=1, column=1, padx=10, pady=10)


    # -------------------------
    # Login result window
    # -------------------------

    def show_result(message):

        result_window = tk.Toplevel(login_window)

        result_window.title("Login")
        result_window.geometry("250x120")

        # Message
        tk.Label(
            result_window,
            text=message,
            font=("Arial", 12)
        ).pack(pady=20)

        # Confirm button
        confirm_button = tk.Button(
            result_window,
            text="Confirm",
            width=8,
            command=result_window.destroy
        )

        confirm_button.pack()


    # -------------------------
    # Login
    # -------------------------

    def login():

        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "1234":

            show_result("Login successful!")

        else:

            show_result("Incorrect username or password.")


    # Login button
    login_button = tk.Button(
        login_window,
        text="Login",
        width=8,
        command=login
    )

    login_button.grid(
        row=2,
        column=1,
        pady=10
    )