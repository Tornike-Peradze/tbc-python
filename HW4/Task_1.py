import random

# Here we ask user to enter the number of players:
players_number = int(input("Enter players number: "))

# Here, at first we check for ensurance purposes that by mistake user doesn't input invalid number, after
# that we write program with the help of for loop. Range, at this time iteration amount that we need depends
# on the number of players input, that's why I use players_number variable in this case. Also, we create 2
# variables for each dice random number and finally, we have 2 random dice for each player.
if players_number <= 0:
    print("Please enter positive player number")
else:
    for i in range(1, players_number+1):
        dice_a = random.randint(1,6)
        dice_b = random.randint(1,6)
        print(f"{dice_a}, {dice_b}")