def fartocel(x):
    c = (x- 32) * 5/9
    return c
def celtofar(x):
    f = x * (9/5) + 32
    return f

test = input("Enter a number.\n1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit\n")

if int(test) == 1:
    temp1 = int(input("Enter the temperature in Fahrenheit: "))
    print(f'The temperature in Celsius is {fartocel(temp1)}')
elif int(test) == 2:
    temp2 = int(input("Enter the temperature in Celsius: "))
    print(f'The temperature in Fahrenheit is {celtofar(temp2)}')
else:
    print('Please enter a valid number.')