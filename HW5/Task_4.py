# Program 4:

# In this program, we ask users a integer number and we use that number to generate a tree. Yeah, a tree :D. We have 4
# symbols that we use in that creation process. What we know exactly is that at the top we should have * and at the
# bottom we should have |. But, interesting part of that symbols creation are their alignment. We want to align them
# with the help of ' ' spaces and use amount of space the user typed in their input_number.Ok, but we have two other
# symbols, in this chapter we are doing all the work on While, so we need some True statement, that's why in all tasks
# create outer variable with some value, then we add or subtract that value to finally become false in while, here we do
# the same, we create i and use user_input_number too and say, please print as many space as user_input - current i and
# please change the default value of end and after that print, please also print / | and \\(we write two backlash
# because for python backlash has a specific meaning in that way we say please use it as I said). We write on each line
# current amount of i, i increases by 1 and until it > input number we'll have our tree growing from top to bottom.

user_input_number = int(input("Please enter a number(don't forget we are creating a tree, so it's like you"
                              "tell us height of a tree: "))

if user_input_number > 0 and user_input_number < 50:
    print(' ' * (user_input_number) + '*')
    i = 1
    while i < user_input_number:
        print(' ' * (user_input_number - i), end='')
        print('/' * i + '|' + '\\' * i)
        i += 1

    print(' ' * (user_input_number - 1) + ' |')
else:
    print("You entered invalid number, please take into consideration it should be in 1-49 range!")
