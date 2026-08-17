#database
import sqlite3

conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()
#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
#add in the data (so far all plack holders)
subjects = ["subject-A", "subject-B", "subject-C", "subject-D"]

cursor.execute("DELETE FROM subjects")

for sub in subjects:
    cursor.execute("INSERT INTO subjects (name) VALUES (?)", (sub,))

conn.commit()
conn.close()
