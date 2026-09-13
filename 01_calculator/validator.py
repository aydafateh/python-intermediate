def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print("invalid number")
        return False

def is_operator(operator):
    if operator in ("+", "-", "*", "/"):
        return True
    else:
        return False
    