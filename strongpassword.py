password=input("Enter the password")
if len(password)>=1:
    if "$"in password or "@" in password or "#" in password:
        if "0"or"9" in password:
            if "A"or "Z"in password:
                print("Strong password")
            else:
                print("weak password")
        else:
            ("Wrong password")
    else:
        print("wrong")
else:
        print("Nothing")
        