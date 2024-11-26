import sqlite3
import os

# Read the SQL script
with open('create_db.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")
