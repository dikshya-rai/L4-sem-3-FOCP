def teststring(name):
    upper = 0
    lower = 0
    for x in name:
        if ord(x) >= 65 and ord(x)<= 90:
            upper = upper + 1
        elif ord(x) >= 97 and ord(x) <= 122:
            lower = lower + 1
        else:
            continue
        print (f'There are {upper} uppercase letters and {lower} lowercase letters. ')
        
        message = input("Enter a string: ")
        teststring(message)