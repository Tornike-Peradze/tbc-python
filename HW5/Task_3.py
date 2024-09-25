# Program 3:

# This is kind of Fibonacci sequence one more time. Here we ask user to type the number they want in the range of 0 to
# 20. We check if they obey that rule and proceed with the main part of the program. As we know, first two number of the
# sequence is known. 0 and 1, so we create that for sure in variables, we also check if user type 0, because if the user
# inputs 0, they should see 0 or sth else, in this case we print that please enter valid number. Also, we need sth to
# check which sequence are we now, for example 0 - 0, 1 - 1, so next is 2 yes? So, we create that variable that's checks
# sequence/index of the number, if current index is less or equal user input number we should generate sequence's next
# number, but also important moment is that our first number should become second and second generated and why, for
# example let's say user typed 4. So, we have 0 1 already, current sequence 2 is < 4, so we are generating next number
# 0 + 1 = 1. So, we have 0 1 1. Ok, now before go to the next sequence we should change sth I mean 0 should become 1, 1
# should become 1 and we should generate new number, so now 0 -> 1, 1 -> 1, so next number will be 2, now 1 -> 1, 1 -> 2
# and like that until urrent_sequence <= user_input_number becomes false.
user_input_number = int(input('Please enter a number: '))

if user_input_number < 0 or user_input_number >= 20:
    print('You entered invalid number, please reenter number and make sure it is in range of 0-20.')
else:
    first_number = 0
    second_number = 1
    if user_input_number == 0:
        print("This is invalid number too, you can't get any sequence if you enter that number!")
    else:
        print(first_number, second_number, end=' ')
        current_sequence = 2
        while current_sequence <= user_input_number:
            next_sequence_number = first_number + second_number
            print(next_sequence_number, end=' ')
            first_number = second_number
            second_number = next_sequence_number
            current_sequence += 1
        print()

