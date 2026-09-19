def is_sentence(sentence:str):
    if " " in sentence:
        return True
    else:
        return False
    
def get_sentence(prompt="text: "):
    while True:
        sentence = input(prompt).strip()
        if is_sentence(sentence):
            return sentence
        else: 
            print("invalid text")
        
def charector(value:str):
    value = value.replace(" " , "")
    return len(value)

def count_word(value:str):
    words = value.split()
    return len(words)
    
def uppercase(value:str):
    value = value.replace(" ", "")
    upper = 0
    for char in value:
        if char.isupper():
            upper += 1
    return upper
    
def lowercase(value:str):
    value = value.replace(" ", "")
    lower = 0
    for char in value:
        if char.islower():
            lower += 1
    return lower

def digit(value:str):
    value = value.replace(" ", "")
    number = 0
    for char in value:
        if char.isdigit():
            number += 1
    return number

def space(value:str):
    return value.count(" ")

def main():
    sentence = get_sentence()
    characters = charector(sentence)
    words = count_word(sentence)
    uppercase_characters = uppercase(sentence)
    lowercase_characters = lowercase(sentence)
    digits = digit(sentence)
    spaces = space(sentence)
    
    analyzer = {
        "characters" : characters,
        "words" : words,
        "uppercase_charcters" : uppercase_characters,
        "lowercase_charcters" : lowercase_characters,
        "digits" : digits,
        "spaces" : spaces
    }
    print(f"characters: {analyzer['characters']} \nwords: {analyzer['words']} \nuppercase: {analyzer['uppercase_characters']} \nlowercase: {analyzer['lowercase_characters']} \ndigits: {analyzer['digits']} \nspaces: {analyzer['spaces']}")
    
if __name__ == "__main__" :
    main()
    