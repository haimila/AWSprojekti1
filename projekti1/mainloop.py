# from projekti1.robot import dancenumberone
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
        # tähän kohtaan tulee funktiokutsu
        with open("my_party_log.txt", "a") as file_object:
            file_object.write(f"I partied hard on {datetime.now()}.\n")
            file_object.close()
        continue

    elif userchoice == "2":
        # tähän kohtaan tulee funktiokutsu
        with open("my_party_log.txt", "a") as file_object:
            file_object.write(f"I chilled out at {datetime.now()}.\n")
            file_object.close()
        continue

    elif userchoice == "3":
        # tähän kohtaan tulee funktiokutsu
        with open("my_party_log.txt", "a") as file_object:
            file_object.write(f"I went to the afterparty at {datetime.now()}.\n")
            file_object.close()
        continue

    elif userchoice == "4":
        with open("my_party_log.txt", "a") as file_object:
            file_object.write(f"I left the party on {datetime.now()}.\n")
            file_object.close()
 #          os.system("scp my_party_log.txt käyttäjä@koneennimi:/tiedostopolku
 #          os.system("rm my_party_log.txt -f")
        break

    else:
        print("Please choose a valid party mode (1, 2, or 3)!")
        continue
