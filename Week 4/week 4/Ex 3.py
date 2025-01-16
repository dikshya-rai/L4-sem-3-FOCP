name = input("Enter your name: ")

def capitalize(text):
    if text:
        result = text[0].upper() + text[1:].lower()
        print(f'{result}')
    else:
        print("No name entered.")

capitalize(name)