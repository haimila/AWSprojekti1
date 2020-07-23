#!/usr/bin/env python3
from robot import dance1
from robo2 import dance2
from robo3 import dance3

from datetime import datetime
import os

os.system("rm my_party_log.txt -f")

while True:
    print("Welcome to the Party Bot!")
    print("What is your current party mood?\n")
    print("1. I want to party hard!")
    print("2. I want to chill out!")
    print("3. Give me the afterparty!")
    print("4. Quit program, party's over")

    userchoice = input("Make your selection: ")

    if userchoice == "1":
        while True:
            dance1()
            break
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I partied hard at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "2":
        dance2()
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I chilled out at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "3":
        dance3()
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I went to the afterparty at {time}.\n".format(time=datetime.now()))
            file_object.close()
        continue

    elif userchoice == "4":
        print("Thank you for partying!")
        with open("my_party_log.txt", "a") as file_object:
            file_object.write("I left the party on {time}.\n".format(time=datetime.now()))
            file_object.close()

        break

    else:
        print("Please choose a valid party mode (1, 2, or 3)!")
        continue
