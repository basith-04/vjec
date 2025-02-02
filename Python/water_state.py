temp = float(input("Enter the value of the temperature: "))
unit = input("Enter the unit (F/C): ").upper().strip()

if unit == 'F':
    temp = (temp - 32) * (5 / 9)
elif unit != 'C':
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    exit()

if temp > 100:
    print("Gaseous")
elif temp < 0:
    print("Solid")
else:
    print("Liquid")
