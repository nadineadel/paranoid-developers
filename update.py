import argparse
import sqlite3
ﶄ=sqlite3.connect
def 㸛(username,change,password_email):
 if change=="password":
  with ﶄ("milestone2.db")as conn:
   闑=conn.cursor()
   ﲷ=闑.execute("UPDATE user SET password = '{password}' WHERE username = '{username}';".format(username=username,password=password_email))
   conn.commit()
   return "password updated"
 elif change=="email":
  with ﶄ("milestone2.db")as conn:
   闑=conn.cursor()
   ﲷ=闑.execute("UPDATE user SET email = '{email}' WHERE username = '{username}';".format(username=username,email=password_email))
   conn.commit()
   return "email updated"
 else:
  return "you can only update password and email"
if __name__=="__main__":
 㸛()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
