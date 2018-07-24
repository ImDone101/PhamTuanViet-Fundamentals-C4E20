userName = input("Username: ")

if userName == "Viet":
    print("Correct")
    p = input("Password: ")
    if p != "456":
        print("Incorrect password")
    else:
        print("Welcome Viet")
else:
    print("Incorrect username")