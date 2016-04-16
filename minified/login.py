import sqlite3
遑=sqlite3.connect
ﷶ=遑
def ܤ(a0,a1):
 縍=ﷶ("milestone2.db")
 ﱾ=縍.cursor()
 溠=ﱾ.execute("SELECT password FROM user WHERE username = '{0}'".format(username)).fetchone()
 縍.close()
 if 溠:
  溠=溠[0]
 return 溠==a1
# Created by pyminifier (https://github.com/liftoff/pyminifier)
