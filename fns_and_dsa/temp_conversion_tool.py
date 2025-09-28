
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Example usage
temperature = int(input("Enter the temperature to convert: "))
measure = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

if measure == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
elif measure == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
else:
    print("Invalid input. Please enter C or F.")
