import subprocess
import pysqlcipher
from pysqlcipher import dbapi2 as sqlite
def Ｔ():
 ڔ=sqlite.connect("milestone2.db")
 c=ڔ.cursor()
 ڔ.commit()
 c.close()
def ډ():
 print("encryptt")
 ڔ=sqlite.connect("milestone2.db")
 c=ڔ.cursor()
 c.executescript("ATTACH DATABASE 'milestone2.db' AS encrypted KEY 'my password'")
 c.executescript("SELECT sqlcipher_export('encrypted')")
 c.executescript("DETACH DATABASE encrypted")
 ڔ.commit()
 ڔ.close()
def 㥒():
 print("decrypt")
 ﻦ="encrypted.db"
 ݥ="PRAGMA key = 'my password';"
 ﲀ="ATTACH DATABASE 'plaintext.db' as plaintext KEY '';"
 ﱄ="SELECT sqlcipher_export('decrypted');"
 ܥ="DETACH DATABASE plaintext;"
 ڔ=sqlite.connect(ﻦ)
 c=ڔ.cursor()
 c.executescript(ݥ)
 c.executescript(ﲀ)
 c.executescript(ﱄ)
 c.executescript(ܥ)
 ڔ.commit()
 ڔ.close()
if __name__=="__main__":
 㥒()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
