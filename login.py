import sqlite3
def login(username, password):
  conn = sqlite3.connect("milestone2.db")
  cur = conn.cursor()
  potential_password = cur.execute("SELECT password FROM user WHERE username = '{0}'".format(username)).fetchone()
  conn.close()
  if potential_password:
  potential_password = potential_password[0]
  return potential_password == password 