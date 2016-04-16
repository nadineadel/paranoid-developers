import sqlite3
ਅ=sqlite3.connect
ﮟ=ਅ
def 뙈(a0,a1,a2):
 ﰄ=ﮟ("milestone2.db")
 ذ=ﰄ.cursor()
 穕=c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username=a0,password=a1,email=a2))
 ﰄ.commit()
 ﰄ.close()
 return "user added"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
