import sqlite3
붘=sqlite3.connect
def 姲(username,password,email):
 挚=붘("milestone2.db")
 鱠=挚.cursor()
 ﴸ=c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username=username,password=password,email=email))
 挚.commit()
 挚.close()
 return "user added"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
