from validator import is_number , is_operator

def get_number(prompt="enter a number:"):
    while True:
        number = input(prompt)
        if number and is_number(number):
            number = float(number)
            return number


def get_operator(prompt="operator: "):
    while True:
        operator = input(prompt)
        if operator and is_operator(operator):
            return operator
        else:
            print("invalid operator")

def add(first, second):
    return first + second

def mul(first, second):
    return first * second

def division(first, second):
    if not second:
        raise ZeroDivisionError("cannot divide by zero")
    return first / second

def minus(first, second):
    return first - second

def calculator(value, first, second):
    if value == "+":
        return add(first , second)
    elif value == "-":
        return minus(first , second)
    elif value == "*":
        return mul(first , second)
    elif value == "/":
        return division(first , second)
    
def main():
    while True:
        first_number = get_number("first number: ")
        operator = get_operator()
        second_number = get_number("second number: ")
        result = calculator(operator , first_number, second_number)
        print(f"result: {result}")
        
        again = input("again?(y/n) :")
        if again.lower() == "n":
            exit()
            
if __name__ == "__main__":
    main()