# database
import sqlite3


# Data stored in the code

subjects = {

    "Mathematics-college": [

        {
            "name": "Mathematics",
            "description": "Mathematics helps develop problem-solving and logical thinking skills."
        },

        {
            "name": "Physics",
            "description": "Physics studies matter, energy and how they interact with each other."
        },

        {
            "name": "Engineering",
            "description": "Engineering uses mathematics and science to solve real-world problems."
        },

        {
            "name": "Computer Science",
            "description": "Computer Science focuses on programming, software and computer systems."
        },

        {
            "name": "Statistics",
            "description": "Statistics involves collecting, analysing and interpreting data."
        },

        {
            "name": "Calculus",
            "description": "Calculus studies change and is commonly used in mathematics, physics and engineering."
        }
    ],


    "subject-B": [

        {
            "name": "Recommendation B1",
            "description": "Description for recommendation B1."
        },

        {
            "name": "Recommendation B2",
            "description": "Description for recommendation B2."
        },

        {
            "name": "Recommendation B3",
            "description": "Description for recommendation B3."
        },

        {
            "name": "Recommendation B4",
            "description": "Description for recommendation B4."
        },

        {
            "name": "Recommendation B5",
            "description": "Description for recommendation B5."
        },

        {
            "name": "Recommendation B6",
            "description": "Description for recommendation B6."
        }
    ],


    "subject-C": [

        {
            "name": "Recommendation C1",
            "description": "Description for recommendation C1."
        },

        {
            "name": "Recommendation C2",
            "description": "Description for recommendation C2."
        },

        {
            "name": "Recommendation C3",
            "description": "Description for recommendation C3."
        },

        {
            "name": "Recommendation C4",
            "description": "Description for recommendation C4."
        },

        {
            "name": "Recommendation C5",
            "description": "Description for recommendation C5."
        },

        {
            "name": "Recommendation C6",
            "description": "Description for recommendation C6."
        }
    ],


    "subject-D": [

        {
            "name": "Recommendation D1",
            "description": "Description for recommendation D1."
        },

        {
            "name": "Recommendation D2",
            "description": "Description for recommendation D2."
        },

        {
            "name": "Recommendation D3",
            "description": "Description for recommendation D3."
        },

        {
            "name": "Recommendation D4",
            "description": "Description for recommendation D4."
        },

        {
            "name": "Recommendation D5",
            "description": "Description for recommendation D5."
        },

        {
            "name": "Recommendation D6",
            "description": "Description for recommendation D6."
        }
    ],


    "subject-E": [

        {
            "name": "Recommendation E1",
            "description": "Description for recommendation E1."
        },

        {
            "name": "Recommendation E2",
            "description": "Description for recommendation E2."
        },

        {
            "name": "Recommendation E3",
            "description": "Description for recommendation E3."
        },

        {
            "name": "Recommendation E4",
            "description": "Description for recommendation E4."
        },

        {
            "name": "Recommendation E5",
            "description": "Description for recommendation E5."
        },

        {
            "name": "Recommendation E6",
            "description": "Description for recommendation E6."
        }
    ],


    "subject-F": [

        {
            "name": "Recommendation F1",
            "description": "Description for recommendation F1."
        },

        {
            "name": "Recommendation F2",
            "description": "Description for recommendation F2."
        },

        {
            "name": "Recommendation F3",
            "description": "Description for recommendation F3."
        },

        {
            "name": "Recommendation F4",
            "description": "Description for recommendation F4."
        },

        {
            "name": "Recommendation F5",
            "description": "Description for recommendation F5."
        },

        {
            "name": "Recommendation F6",
            "description": "Description for recommendation F6."
        }
    ]
}


# Initialize Database
def init_database():

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()


    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)



    # Subjects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)


    # Recommendations table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER,
        button_number INTEGER,
        recommendation TEXT,
        description TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """)


    # Check if description column exists

    cursor.execute("""
    PRAGMA table_info(recommendations)
    """)

    columns = cursor.fetchall()

    column_names = []

    for column in columns:
        column_names.append(column[1])


    if "description" not in column_names:

        cursor.execute("""
        ALTER TABLE recommendations
        ADD COLUMN description TEXT
        """)



    # Admin user account
    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    """)

    user_count = cursor.fetchone()[0]


    if user_count == 0:

        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """, ("admin", "1234"))


    # Check database data
    database_matches = True


    # Get subjects from database
    cursor.execute("""
    SELECT name
    FROM subjects
    ORDER BY id
    """)

    database_subjects = cursor.fetchall()


    database_subject_names = []

    for row in database_subjects:
        database_subject_names.append(row[0])


    # Subjects in code
    code_subject_names = list(subjects.keys())


    # Check subjects
    if database_subject_names != code_subject_names:

        database_matches = False

    # Check recommendations

    if database_matches:

        for subject_name, recommendations in subjects.items():

            cursor.execute("""
            SELECT recommendations.recommendation,
                   recommendations.description

            FROM recommendations

            JOIN subjects
            ON recommendations.subject_id = subjects.id

            WHERE subjects.name = ?

            ORDER BY recommendations.button_number
            """, (subject_name,))

            database_recommendations = cursor.fetchall()


            code_recommendations = []

            for recommendation in recommendations:

                code_recommendations.append(
                    (
                        recommendation["name"],
                        recommendation["description"]
                    )
                )


            if database_recommendations != code_recommendations:

                database_matches = False

                break
    # Refresh database if data does not match

    if not database_matches:

        print("Database does not match the code.")
        print("Refreshing subjects and recommendations...")


        # Delete old recommendations
        cursor.execute("""
        DELETE FROM recommendations
        """)


        # Delete old subjects
        cursor.execute("""
        DELETE FROM subjects
        """)


        # Add subjects and recommendations

        for subject_name, recommendations in subjects.items():

            cursor.execute("""
            INSERT INTO subjects (name)
            VALUES (?)
            """, (subject_name,))
            subject_id = cursor.lastrowid
            for number, recommendation in enumerate(
                recommendations,
                start=1
            ):

                cursor.execute("""
                INSERT INTO recommendations
                (
                    subject_id,
                    button_number,
                    recommendation,
                    description
                )
                VALUES (?, ?, ?, ?)
                """, (
                    subject_id,
                    number,
                    recommendation["name"],
                    recommendation["description"]
                ))


        print("Database refreshed.")


    else:

        print("Database is already up to date.")


    # Save everything
    conn.commit()
    conn.close()


# Get Subjects
def get_subjects():

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM subjects
    ORDER BY id
    """)

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


# Get Recommendations
def get_recommendations(subject_name):

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT recommendations.recommendation

    FROM recommendations

    JOIN subjects
    ON recommendations.subject_id = subjects.id

    WHERE subjects.name = ?

    ORDER BY recommendations.button_number
    """, (subject_name,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]

# Get Recommendation Description

def get_description(recommendation):

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT description
    FROM recommendations
    WHERE recommendation = ?
    """, (recommendation,))

    result = cursor.fetchone()

    conn.close()

    if result and result[0]:

        return result[0]

    return "No description available."

# Check Login accounts
def check_login(username, password):

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM users
    WHERE username = ?
    AND password = ?
    """, (username, password))

    result = cursor.fetchone()

    conn.close()

    if result:

        return True

    return False


# Register new user account

def register_user(username, password):

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """, (username, password))

        conn.commit()

        conn.close()

        return True

    except sqlite3.IntegrityError:

        conn.close()

        return False