import random

# Generate non-integer number
random_number = random.uniform(0, 100)

# Round to nearest decimal
rounded_number = round(random_number, 1)

print(f"Random number: {random_number}")
print(f"Rounded number: {rounded_number}")
