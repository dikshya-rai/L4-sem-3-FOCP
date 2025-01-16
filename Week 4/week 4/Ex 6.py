def celtofar(celsius):
    return celsius * (9/5) + 32

cent = input("Enter temperature in Celsius (e.g., 25C): ")
if cent.endswith("C") or cent.endswith("c"):
    cel = float(cent[:-1])
    fahrenheit = celtofar(cel)
    print(f"{fahrenheit:.2f}F")
else:
    print("Please enter in correct format.")