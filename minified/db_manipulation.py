import subprocess
import pysqlcipher
from pysqlcipher import dbapi2 as sqlite
def 俅():
 뿟=sqlite.connect("milestone2.db")
 c=뿟.cursor()
 뿟.commit()
 c.close()
def 컳():
 print("encryptt")
 뿟=sqlite.connect("milestone2.db")
 c=뿟.cursor()
 c.executescript("ATTACH DATABASE 'milestone2.db' AS encrypted KEY 'my password'")
 c.executescript("SELECT sqlcipher_export('encrypted')")
 c.executescript("DETACH DATABASE encrypted")
 뿟.commit()
 뿟.close()
def 橎():
 print("decrypt")
 冽="encrypted.db"
 ڷ="PRAGMA key = 'my password';"
 ﭧ="ATTACH DATABASE 'plaintext.db' as plaintext KEY '';"
 ޏ="SELECT sqlcipher_export('decrypted');"
 ﱙ="DETACH DATABASE plaintext;"
 뿟=sqlite.connect(冽)
 c=뿟.cursor()
 c.executescript(ڷ)
 c.executescript(ﭧ)
 c.executescript(ޏ)
 c.executescript(ﱙ)
 뿟.commit()
 뿟.close()
if __name__=="__main__":
 橎()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
