# Program 1:

# This program starts by creation of variable - user_input_number, which asks the users to type their desired number.
# Before we create main logic of the program, at first we check if the user's entered number is valid(is in range).
# After that check, we actually start the program's main part. At first, we create some variable in this case - i.
# We use that variable then as a current input number, I mean we start from 1 and gradually add 1 to it and in that
# process checking if each number up until it reaches user_input_number can be divided. Ok, after that variable creation
# we create first while statement, where check if the i is equal or less user_input_number, if it's true then we proceed
# Next print statement is interesting, because finally we want to have each number from 1 up to user_input_number and
# parallely divisors of it, so here we write i, current number and as we know in print statement end has default value of
# \n we change it to '' to have concrete numbers output in a row. Next, we need another variable and why? Because we
# already created a 'current' number, but also we need another variable to divide that current number. After that, final
# logic comes, we say while j <= i is true, please check if the i for example 1 % 1 == 0, if it's correct then add
# another print statement, at this time each j value and please change the end here too, now as - end ' '. So,
# on the example of 1, we have 1 - 1. Then, we add j + 1 and my while statement becomes false for 1. Then, we have empty
# print(), that gives us next line for the next current number and finally we add 1 to i aka current number.


user_input_number = int(input('Please enter a number: '))

if user_input_number < 0 or user_input_number > 50:
    print('Your input number is invalid, please reenter and make sure it is in range of 0-50')
else:
    i = 1
    while i <= user_input_number:
        print(f'{i} - ', end='')
        j = 1
        while j <= i:
            if i % j == 0:
                print(j, end=' ')
            j += 1
        print()
        i += 1
