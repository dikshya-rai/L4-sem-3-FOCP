print("Enter temperatures in Celsius (e.g., 36C/36c):")

celsius = []
for x in range(6):
    temp = input('')
    if temp.endswith("c") or temp.endswith("C"):
        if ValueError:
            print("Invalid input. Please enter a number.")
        else:
            celsius.append(float(temp[:-1]))
    else:
        print("Please enter the temperature in the correct format. ")
        

if celsius: 
    min1 = min(celsius)
    max1 = max(celsius)
    mean = sum(celsius) / len(celsius)
    print(f'The minimum is {min1}, the maximum is {max1}, and the mean is {mean:.2f}.')
else:
    print("No temperatures were entered.")