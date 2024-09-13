def categorize_speed(speed):
    if speed > 120:
        return "VERY FAST"
    elif speed > 60:
        return "FAST"
    elif speed > 30:
        return "MODERATE"
    else:
        return "SLOW"


try:
    speed = float(input("Enter the car's speed (in km/h): "))
    category = categorize_speed(speed)
    print(f"Speed category: {category}")
except ValueError:
    print("Error: Please enter a valid number for the speed.")
