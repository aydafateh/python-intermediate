email = input("enter email: ").strip()

if email.count("@") == 1 and email.count(".") == 1:

    parts = email.split("@")
    username = parts[0]
    domain_extension = parts[1]

    if username:
        valid_username = True
        for char in username:
            if not (char.isalnum() or char in "._-"):
                valid_username = False
                break

        if valid_username:
            parts = domain_extension.split(".")
            domain = parts[0]
            extension = parts[1]
            if domain.isalpha() and extension.isalpha():
                print(
                    f"username : {username}\n"
                    f"domain : {domain}\n"
                    f"extension : {extension}"
                )
            else:
                print("invalid domain or extension")
        else:
            print("invalid username")
    else:
        print("invalid username")
else:
    print("invalid email")