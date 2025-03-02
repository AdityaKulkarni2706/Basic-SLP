import sqlite3


def create_table():
    conn = sqlite3.connect('database.db')
    query = "CREATE TABLE Users(UID Integer Primary Key, Username text, Password text)"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def select_data(required_columns):
    conn = sqlite3.connect('database.db')
    query = "SELECT {} FROM Users".format(', '.join(required_columns))
    cursor = conn.cursor()
    cursor.execute(query)
    recieved_data = cursor.fetchall()
    return recieved_data

def insert_data(data):
    conn = sqlite3.connect("database.db")
    query = "INSERT INTO Users(Username, Password) VALUES(?,?)"
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()

def specific_user_credentials(username):
    conn = sqlite3.connect("database.db")
    query = "SELECT * FROM USERS WHERE Username == ?"
    cursor = conn.cursor()
    cursor.execute(query, (username,))
    credentials = cursor.fetchone()
    return credentials






