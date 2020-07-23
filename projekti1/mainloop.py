#!/usr/bin/env python3
from robot import dance1
from robo2 import dancenumbertwo
from robo3 import dancenumberthree

from datetime import datetime
# import os

while True:

    print("Welcome to the Party Bot!")
    print("What is your current party mood?\n")
    print("1. I want to party hard!")
    print("2. I want to chill out!")
    print("3. Give me the afterparty!")
    print("4. Quit program, party's over")

    userchoice = input("Make your selection: ")

    if userchoice == "1":
        dance1()
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I chilled out at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "2":
        dancenumbertwo()
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I chilled out at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "3":
        dancenumberthree()
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I went to the afterparty at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "4":
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I left the party on {time}.\n".format(time=datetime.now()))
            file_object.close()
 #          os.system("scp my_party_log.txt käyttäjä@koneennimi:/tiedostopolku
 #          os.system("rm my_party_log.txt -f")
        break

    else:
        print("Please choose a valid party mode (1, 2, or 3)!")
        continue
