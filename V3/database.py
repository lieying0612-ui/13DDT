#database
import sqlite3


conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()

def init_database():
    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER,
        button_number INTEGER,
        recommendation TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """)
cursor.execute("SELECT COUNT(*) FROM subjects")
    
if cursor.fetchone()[0] == 0:

        subjects = {
            "subject-A": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ],

            "subject-B": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ],

            "subject-C": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ],

            "subject-D": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ],
             "subject-E": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ],
             "subject-F": [
                "place_holder1",
                "place_holder2",
                "place_holder3",
                "place_holder4",
                "place_holder5",
                "place_holder6"
            ]
        }
        for subject_name, recommendations in subjects.items():

            cursor.execute(
                "INSERT INTO subjects (name) VALUES (?)",
                (subject_name,)
            )

            subject_id = cursor.lastrowid

            for number, recommendation in enumerate(recommendations, start=1):

                cursor.execute("""
                INSERT INTO recommendations
                (subject_id, button_number, recommendation)
                VALUES (?, ?, ?)
                """, (
                    subject_id,
                    number,
                    recommendation
                ))

        conn.commit()
        conn.close()

def get_subjects():

    conn = sqlite3.connect("subjects.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM subjects
    """)

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


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
#login page database
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

