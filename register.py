import sqlite3
ਅ=sqlite3.connect
ﮟ=ਅ
def 뙈(username,password,email):
 ﰄ=ﮟ("milestone2.db")
 ذ=ﰄ.cursor()
 穕=c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username=username,password=password,email=email))
 ﰄ.commit()
 ﰄ.close()
 return "user added"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
