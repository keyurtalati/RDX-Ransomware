from cryptography.fernet import Fernet
import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
key = (input("Enter the key"))# Use one of the methods to get a key (it must be the same as used in encrypting))
files=[]
for input_file in os.listdir(os.getcwd()):
    files.append(input_file)
files.remove("rdx-crypter.py")
files.remove("key.key")
files.remove("NOTE.txt")
for input_file in files:
    if input_file.split('.')[1]:
            new_filename = input_file.split('.')[0] +'.'+ input_file.split('.')[1]
            os.rename(input_file,  new_filename)
    output_file=input_file
files2=[]
for x in os.listdir(os.getcwd()):
    files2.append(x)
files2.remove("rdx-crypter.py")
files2.remove("key.key")
files2.remove("NOTE.txt")
for input_file in files2:
    output_file=input_file
    with open(input_file, 'rb') as f:
         data = f.read()
         f.close()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
        f.close()
print("Decryption Completed...")
os.remove("rdx-crypter.py")
os.remove("key,key")
os.remove("NOTE.txt")
