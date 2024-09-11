# What this program does:
# This program simply at first asks users temperature in Celsius and when they type the answer, after that with the help
# of formula it converts that temperature to Fahrenheit.


temperature_in_celsius = float(input('Please type the Celsius temperature: '))

# Convert Celsius to Fahrenheit
temperature_in_farenheit = (temperature_in_celsius * 9 / 5) + 32

print(f'temperature in Farenheit is: {temperature_in_farenheit}')