FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if temp_unit == 'f':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif temp_unit == 'c':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
