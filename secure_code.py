from cryptography.fernet import Fernet
from simplecrypt import encrypt, decrypt

ciphertext = encrypt('password', 'nadine.txt')
#plaintext = decrypt('password', ciphertext)
# def encrypt_code(key, code):
#   key = Fernet.generate_key()
#   cipher_suite = Fernet(key)
#   cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
#   return key
#   #plain_text = cipher_suite.decrypt(cipher_text)

# def decrypt_code(key, code):
#   # decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV)
#   # plain_text = decryption_suite.decrypt(code)
if __name__ == '__main__':
  encrypt_file("nadine","nadine.txt")