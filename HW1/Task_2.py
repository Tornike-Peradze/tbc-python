# What this program does:
# This program asks users for their name and birth year, then it calculates user's age and print Hello message,
# which includes their name and calculated age.

# How our program works:
# At first I create user_name variable with input to give users chance to type their name, after that I create second
# variable user_birth_year to ask users in what year they were born and after that I import from datetime module
# datetime class. Firstly, I create a new variable current_year and with the help of datetime class I use now() to
# get the current date period and finally after dot I mention year to be specific of my intentions and then in print
# statement I use that calculated variable.

from datetime import datetime

user_name = input('Please type your name here: ')
user_birth_year = int(input('Please type your born year here: '))
current_year = datetime.now().year
user_age = current_year - user_birth_year

print(f"Hello {user_name}, you are {user_age} old.")