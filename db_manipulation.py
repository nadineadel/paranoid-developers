# import subprocess
# import pysqlcipher
from pysqlcipher import dbapi2 as sqlite


def create_database():
  conn = sqlite.connect("milestone2.db")
  c = conn.cursor()
  # c.executescript('pragma key="testing"; pragma kdf_iter=64000;')
  # c.execute('create table users (username, password, email)')
  # c.execute('insert into stocks values ("2006-01-05","BUY","RHAT",100,35.14)')
  conn.commit()
  c.close()


def encrypt():
  print ("encryptt")
  conn = sqlite.connect("milestone2.db")
  c = conn.cursor()
  c.executescript("ATTACH DATABASE 'milestone2.db' AS encrypted KEY 'my password'")
  c.executescript("SELECT sqlcipher_export('encrypted')")
  c.executescript("DETACH DATABASE encrypted")
  conn.commit()
  conn.close()


def decrypt():
  print("decrypt")
  command = "encrypted.db"
  pragma = "PRAGMA key = 'my password';"
  attach = "ATTACH DATABASE 'plaintext.db' as plaintext KEY '';"
  select = "SELECT sqlcipher_export('decrypted');"
  detach = "DETACH DATABASE plaintext;"
  conn = sqlite.connect(command)
  c = conn.cursor()
  c.executescript(pragma)
  c.executescript(attach)
  c.executescript(select)
  c.executescript(detach)
  conn.commit()
  conn.close()


if __name__ == "__main__":
  decrypt()
