import sqlite3
ر=sqlite3.connect
def ॺ(username,password,email):
 with ر("milestone2.db")as conn:
  ڤ=conn.cursor()
  蝆=ڤ.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username=username,password=password,email=email))
  conn.commit()
  conn.close()
 return "user added"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
