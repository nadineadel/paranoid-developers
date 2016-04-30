import sqlite3
def deactivate(username):
  with sqlite3.connect("milestone2.db") as conn:
    cur = conn.cursor()
    user = cur.execute("DELETE FROM user WHERE username = '{0}'".format(username)).fetchone()
    conn.commit()
    conn.close()
  print "deactivated"
  return  "deactivated"

if __name__ == "__main__":
  deactivate()