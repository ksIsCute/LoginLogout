import json, random

choice = input("""
                  ______________
                  |            |
                  | 1. Sign Up |
                  |            |
                  | 2. Log In  |
                  |____________|
\n\n""")


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
    if len(password) < 8:
      print("Your password is too small! Make sure your password is 8 characters or under!")
      
    elif len(password) > 71:
      print("Your password must be under 72 characters!")
    # open it in write mode because r+ exists but fuck you im doing it this way
    with open("file.json", "w") as f:
      userbio = "This user has no bio!"
      email = "totallyrealemail69420@gmail.com"
      id = random.randint(1000000, 9999999)
      if id in uname:
        id = random.randint(1000000, 9999999)
        if id in uname:
          id = random.randint(1000000, 9999999)
          if id in uname:
            id = random.randint(1000000, 9999999)
            if id in uname:
                id = random.randint(1000000, 9999999)
                if id in uname:
                    id = random.randint(1000000, 9999999)
      uname[str(username)] = {"username": username, "password": password, "email": email, "bio": userbio, "id": id}
      json.dump(uname, f, indent=2)
      print(f"Created {uname[str(username)]['username']}")
      print(f"Your id is {uname[username]['id']}")
    print("\nDone!\nSign in by selecting 2 at this selection screen!\nAccount created!")
else:
  with open("file.json", "r") as f:
    uname = json.load(f)
  username = input("\nWhats your username?\n\n")
  if username not in uname:
    print("That username is invalid! Check capitalisation! Or that username might not be taken!")
  else:
    password = input(f"\nWhat is the password for {username}?\n\n")
    if password != uname[username]['password']:
      print("\nYour password is WRONG, try again and check for typos!")
    else:
      print(f"\nNow logged in as {username}!")
      selection = input("""
                  _________________________
                  |                       |
                  |  1. Delete Account    |
                  |  2. Change password   |
                  |  3. Change username   |
                  |  4. Profile Settings  |
                  |  5. Your Profile      |
                  |  6. Sign Out          |
                  |_______________________|
\n\n""")
      if str(selection) == "1":
        d = input(f"Are you sure you want to delete your account {username}?\n")
        if d.lower() in ["n", "no", "cancel", "nope", "nah", "nuh"]:
          print("\nAccount not deleted. You may exit safely now.")
        elif d.lower() in ["y", "yes", "sure", "ok", "yuh", "yessir", "okay", "confirm", "continue", "yea"]:
          with open("file.json", "r") as f:
            data = json.load(f)
          with open("file.json", "w") as f:
            data.pop(username)
            json.dump(data, f, indent=2)
          print("\nAccount deleted, you cannot go back now.")