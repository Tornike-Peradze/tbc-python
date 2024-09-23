import random

n = int(input("Please enter the whole positive number: "))

# Here, at first we check the n number correctness. After we assure, everything is correct, then at first we
# create a list empty variable and then start for loop. In for we loop n-th time in range, to make that number
# of variable finally. We assign number variable a random integer up to 1000 and for each iteration it generates
# new random number and we also use lists append method to add empty created list variable each random number and
# don't lose them. Finally, we tryna find the max number from the list.
if n <= 0 or n >= 30:
    print("Please enter positive whole number, as said in input script")
else:
    random_selected_numbers_list = []
    for i in range(n):
        number = random.randint(0, 1000)
        random_selected_numbers_list.append(number)
        print(f"Randomly generated numbers are: {random_selected_numbers_list}")
        max_number = max(random_selected_numbers_list)
        print(f"Max number is: {max_number}")