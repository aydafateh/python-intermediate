def is_name(name:str):
    if name and name.replace(" ", "").isalpha():
        return True
    else:
        return False
        
def get_name(prompt="Name: "):
    while True:
        name = input(prompt).strip()
        
        if name.lower() in ("q", "quit", "exit"):
            return None
        
        if is_name(name):
            return name
        else:
            print("invalid name")

def is_age(age):
    try:
        int(age)
        return True
    except ValueError:
        return False
    
def get_age(prompt="Age: "):
    while True:
        age = input(prompt).strip()
        if age and is_age(age):
            age = int(age)
            return age
        else :
            print("invalid age")

def is_status(status:str):
    if status.upper() in ("STUDENT" , "YES" , "Y"):
        return True
    else:
        return False
    
def get_status(prompt="student status: ") :
    while True:
        status = input(prompt).strip()
        if is_status(status):
            return "YES"
        else:
            return "NO"

def main():
    while True:
        name = get_name()
        
        if name is None:
            break
        
        age = get_age()
        city = get_name("City: ")
        language = get_name("Programming Language: ")
        status = get_status()
        
        profile = {
            "Name" : name ,
            "Age" : age ,
            "City" : city ,
            "favorite language" : language ,
            "student" : status
        }
        
        print(f"\n\n====USER PROFILE==== \nName: {profile['Name']} \nAge: {profile['Age']} \nCity: {profile['City']} \nfavorite language: {profile['favorite language']} \nstudent: {profile['student']}")

if __name__ == "__main__":
    main()