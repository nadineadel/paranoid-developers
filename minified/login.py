import sqlite3
ܤ=sqlite3.connect
def ܓ(username,password):
 괙=ܤ("milestone2.db")
 ﱏ=괙.cursor()
 峟=ﱏ.execute("SELECT password FROM user WHERE username = '{0}'".format(username)).fetchone()
 괙.close()
 if 峟:
  峟=峟[0]
 return 峟==password
# Created by pyminifier (https://github.com/liftoff/pyminifier)
