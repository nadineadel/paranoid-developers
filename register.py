import sqlite3
def register(username, password, email):
	with sqlite3.connect("security.db") as conn:
		c = conn.cursor()
		new_user = c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username = username, password = password, email = email))
		conn.commit()
		return "user added"
	return "Error Happpened at register"