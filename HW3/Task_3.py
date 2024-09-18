import datetime

year = int(input("Year: "))
month = int(input("Month (1-12): "))
day = int(input("Day: "))

birth_date = datetime.date(year, month, day)

# I'm just finding day of the week -> (0 = Monday, 6 = Sunday)
day_of_week = birth_date.strftime("%A")

print(f"It was {day_of_week}.")
