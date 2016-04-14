import sqlite3
def login(username, password):
	with sqlite3.connect("security.db") as conn:
		c = conn.cursor()
		potential_password = c.execute("SELECT password FROM user WHERE username = '{0}'".format(username)).fetchone()
		if potential_password:
			potential_password = potential_password[0]
		return potential_password == password
	return "Error happened at login"