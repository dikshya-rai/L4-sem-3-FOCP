print("Enter temperatures in Celsius (e.g., 36C/36c).\nPress Enter to finish:")

celsius = []
while True:
    temp = input('')
    if temp == '': 
        break
    elif ValueError:
        print("Please enter a value.")
    else:
        if temp.endswith('c') or temp.endswith("C"):
            celsius.append(int(temp[:-1]))
        else:
            print("Please enter in correct format.")

if celsius:  
    min1 = min(celsius)
    max1 = max(celsius)
    mean = sum(celsius) / len(celsius)
    print(f'The minimum is {min1}, the maximum is {max1}, and the mean is {mean:.2f}.')
else:
    print("No temperatures were entered.")