import argparse
import sqlite3
def update(username, change, password_email):
  if change == "password":
    with sqlite3.connect("milestone2.db") as conn:
      c = conn.cursor()
      update_user = c.execute("UPDATE user SET password = '{password}' WHERE username = '{username}';".format(username = username, password = password_email))
      conn.commit()
      return "password updated"
  elif change == "email":
    with sqlite3.connect("milestone2.db") as conn:
      c = conn.cursor()
      update_user = c.execute("UPDATE user SET email = '{email}' WHERE username = '{username}';".format(username = username, email = password_email))
      conn.commit()
      return "email updated"
  else:
    return "you can only update password and email"

if __name__ == "__main__":
  update()