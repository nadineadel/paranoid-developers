import sqlite3
곐=sqlite3.connect
def 懮(username,password,email):
 ﴮ=곐("milestone2.db")
 ﮢ=ﴮ.cursor()
 蘷=c.execute("INSERT INTO user (username, password, email) VALUES ('{username}','{password}','{email}')".format(username=username,password=password,email=email))
 ﴮ.commit()
 ﴮ.close()
 return "user added"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
