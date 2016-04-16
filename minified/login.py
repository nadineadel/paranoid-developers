import sqlite3
붘=sqlite3.connect
def ᣑ(username,password):
 ޡ=붘("milestone2.db")
 ㄪ=ޡ.cursor()
 ﲁ=ㄪ.execute("SELECT password FROM user WHERE username = '{0}'".format(username)).fetchone()
 ޡ.close()
 if ﲁ:
  ﲁ=ﲁ[0]
 return ﲁ==password
# Created by pyminifier (https://github.com/liftoff/pyminifier)
