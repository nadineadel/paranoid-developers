import sqlite3
def register(username, password, email):
    conn = sqlite3.connect("milestone2.db")
    cur = conn.cursor()
    new_user = c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username = username, password = password, email = email))
    conn.commit()
    conn.close()
    return "user added"