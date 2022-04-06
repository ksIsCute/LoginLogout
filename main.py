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
      email = input("What is your email?")
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
                  |  4. Settings          |
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
          print("\nAccount deleted, you cannot go back now. But you can create another. We're sorry to see you go!")
      elif str(selection) == "2":
        opw = input("Enter old password:\n")
        if opw != uname[username]['password']:
          print("\nWrong password!")
        elif opw == uname[username]['password']:
          npw = input("\nCorrect password! Please enter your new password:\n")
          with open("file.json", "w") as f:
            uname[username]["password"] = npw
            json.dump(uname, f, indent=2)
          print("Password changed")
      elif str(selection) == "3":
        nun = input("\nChoose a new username:\n")
        with open("file.json", "r") as f:
          uname = json.load(f)
        with open("file.json", "w") as f:
          if nun in uname:
            print("Username taken! Sorry!")
          else:
            uname[nun] = {"username": nun, "password": uname[username]['password'], "email": uname[username]['email'], "bio": uname[username]['bio'], "id": uname[username]['id']}
            uname.pop(username)
            json.dump(uname, f, indent=2)
      elif str(selection) == "4":
        with open("file.json", "r") as f:
          uname = json.load(f)
        print("""
                  _________________________
                  |                       |
                  |  1. Set Bio           |
                  |  2. Change Email      |
                  |  3. Add friend        |
                  |  4. Settings          |
                  |  5. Set your status   |
                  |  6. Sign Out          |
                  |_______________________|
              """)
        print("a")