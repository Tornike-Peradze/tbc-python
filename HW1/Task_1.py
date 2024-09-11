# What this program does:
# In this program allow users to input their first name, last name and age. After we collect those info, we greet them
# and name their age too.

# How our program works:
# At first we create 3 variables and to store users credentials. # The input prompts are provided with text to make it
# easier for users to understand. One interesting moment is that user_age's input is in int() brackets, because here
# logical output of variable is whole number and each and every output of input is string, so it would be better to
# write like that. Finally, the program ends with print statement, where I use f'' technique to easily embody the
# variables and text.

user_name = input('Please type your name: ')
user_last_name = input('Please type your last name: ')
user_age = int(input('Please type your age: '))

print(f"Hello {user_name}, {user_last_name}, you are {user_age} years old.")