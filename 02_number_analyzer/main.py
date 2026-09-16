def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def get_number(prompt="number: "):
    while True:
        number = input(prompt)
        
        if number.lower() in ("q", "exit", "quit"):
            return None
        
        if number and is_number(number):
            number = int(number)
            return number
        
def is_even(value):
    return "No" if value%2 else "Yes"

def is_positive(value):
    if value > 0 :
        return "Yes"
    elif value < 0:
        return "No"
    else:
        return "Zero"

def main():
    numbers = []
    while True:
        number = get_number()
        
        if number is None:
            break
        
        even = is_even(number)
        positive = is_positive(number)
        numbers.append(number)
        print(f"even : {even} \npositive : {positive}")
        
    if numbers:
        upper = numbers[0]
        for i in numbers :
            if i >= upper:
                upper = i

        print(f"max : {upper}")
                
if __name__ == "__main__" :
    main()