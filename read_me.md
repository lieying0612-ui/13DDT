# Subject Advice App

## Require Version

- Python 3.12 or above
- Tkinter
- SQLite3

## Project Structure

```text
13DDT/
│
└── V4/
    │
    ├── main.py
    ├── database.py
    ├── login.py
    ├── subjects.db
    └── README.md

## File Description
File	Description
main.py	Main program. Creates the GUI, subject dropdown, six recommendation buttons, search bar, Sign In and Sign Up buttons.
database.py	Handles the SQLite database. Stores subjects, recommendations and user login information.
login.py	Contains the Sign In and Sign Up windows and handles user login and registration.
subjects.db	SQLite database containing subjects, recommendations and user information.
README.md	Project documentation and instructions for running the application.
Features

The Subject Advice App provides students with information and recommendations about different school subjects.

Main Features
Subject selection using a dropdown menu
Six dynamic recommendation buttons
Recommendations are loaded from the SQLite database
Sign In system
Sign Up system
Username and password stored in the database
Login success and failure messages
Hover effects for recommendation buttons
Separate windows for Sign In and Sign Up
How It Works

The application uses Python Tkinter for the graphical user interface and SQLite3 for storing data.

The basic process is:

User selects a subject
        ↓
Tkinter Combobox
        ↓
get_recommendations()
        ↓
SQLite Database
        ↓
Return recommendations
        ↓
Update six buttons

For example, when the user selects subject-A, the application searches the database for the recommendations associated with subject-A.

The six buttons are then automatically updated with the results from the database.

Database

The application uses SQLite3.

The database contains the following main tables:

Subjects

Stores the available subjects.

Column	Description
id	Unique ID for each subject
name	Name of the subject
Recommendations

Stores recommendations for each subject.

Column	Description
id	Unique ID
subject_id	ID of the related subject
button_number	Button number from 1 to 6
recommendation	Recommendation displayed on the button
Users

Stores registered user information.

Column	Description
id	Unique user ID
username	User's username
password	User's password
Installation

Make sure Python is installed on the computer.

Check the Python version using:

python3 --version

The project requires Python 3.12 or above.

Tkinter and SQLite3 are normally included with Python.

Running the Application

Open Terminal and navigate to the project folder:

cd /Users/aobintang/Documents/GitHub/13DDT/V4

Then run:

python3 main.py

The main application window should open.

Using the Application
1. Select a Subject

Use the Select subject dropdown on the left side of the application.

Example:

Select subject:
[ subject-A ▼ ]

After selecting a subject, the six recommendation buttons will automatically update.

2. Sign In

Click the Sign In button in the top-right corner.

Enter:

Username
Password

Then click Login.

The application will display a separate result window showing whether the login was successful or unsuccessful.

3. Sign Up

Click the Sign Up button in the top-right corner.

Enter:

Username
Password
Confirm Password

The application checks that:

All required fields are filled in
The password and confirmation password match
The username does not already exist

If the registration is successful, the new account is stored in the SQLite database.

Project Dependencies

The project uses the following Python modules:

tkinter
sqlite3

tkinter is used to create the graphical user interface.

sqlite3 is used to create and manage the local database.

Important Functions
init_database()

Creates the required database tables and initial subject data.

init_database()
get_subjects()

Gets all subjects from the database.

subjects = get_subjects()

The returned subjects are used as the values of the Combobox.

get_recommendations(subject_name)

Gets the six recommendations associated with a selected subject.

recommendations = get_recommendations(selected_subject)
check_login(username, password)

Checks whether the username and password exist in the database.

check_login(username, password)
register_user(username, password)

Adds a new user to the database during Sign Up.

register_user(username, password)
Dynamic Buttons

The six recommendation buttons are connected to the subject dropdown.

The following event is used:

subject.bind("<<ComboboxSelected>>", update_buttons)

When the user selects a subject, update_buttons() is called.

def update_buttons(event=None):

    selected_subject = subject.get()

    recommendations = get_recommendations(selected_subject)

    for i in range(6):

        if i < len(recommendations):
            buttons[i].config(text=recommendations[i])
        else:
            buttons[i].config(text="")

This allows the content of the six buttons to change without manually changing the GUI code.

Future Improvements

Possible future improvements include:

Adding more subjects
Adding more detailed career information
Adding subject requirements
Adding university and course information
Improving the search function
Adding user profiles
Adding password security
Improving the GUI design
Adding images and icons
Adding personalised career recommendations
Connecting the application to a larger database
Author