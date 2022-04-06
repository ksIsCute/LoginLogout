import json

choice = input("""
______________
|            |
| 1. Sign Up |
|            |
| 2. Log In  |
|____________|\n\n""")


if str(choice) == "1":
  # defining our basic ass motherfucking variables please understand this
  username = input("Choose a username:\n\n")
  
  # open the json file to read your hell
  with open("file.json", "r") as f:
    uname = json.load(f)
  if username in uname:
    print("The username entered is taken! Please choose an available username!")
  else:
    password = input("Choose a password for your account:\n\n")
    # open it in write mode because r+ exists but fuck you im doing it this way
    with open("file.json", "w") as f:
      uname[str(username)] = password
      json.dump(uname, f, indent=2)
else:
  with open("file.json", "r") as f:
    uname = json.load(f)
  username = input("\nWhats your username?\n\n")
  if uname.get(username) is None:
    print("That username is invalid! Check capitalisation! Or that username might not be taken!")
  else:
    password = input(f"\nWhat is the password for {username}?\n\n")
    if password != uname.get(username):
      print("\nYour password is WRONG, try again and check for typos!")
    else:
      print(f"\nNow logged in as {username}!")  