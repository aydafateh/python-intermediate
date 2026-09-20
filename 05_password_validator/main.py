password = input("password Example: ")

has_digit = False
has_lower = False
has_upper = False

if len(password) >= 8:
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
    if has_lower and has_upper and has_digit :
        print("password: strong")
    else:
        print("password : not strong")
else:
    print("password : not strong")