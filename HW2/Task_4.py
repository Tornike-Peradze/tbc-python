# Very simply, categorizing speed according to the condition using if-else statements in speed_categories method.
# After that I'm just using try catch to handle errors if it occurs, if not returning appropriate speed category.

def speed_categories(speed):
    if speed > 120:
        return "VERY FAST"
    elif speed > 60:
        return "FAST"
    elif speed > 30:
        return "MODERATE"
    else:
        return "SLOW"


try:
    speed = float(input("Enter car's speed: "))
    category = speed_categories(speed)
    print(f"Speed category: {category}")
except ValueError:
    print("Error: Enter valid number for speed.")
