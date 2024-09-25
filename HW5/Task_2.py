# Program 2:

# In this program we wanted to have a product of numbers from 1 to 9, but there is more than just that, on each row
# we want to have only unique products and on each new row one new column should add. So, one of the solution for this
# task is to create a variables for the rows and columns. The basic logic is that, you should start multiply two var
# and those variables should increment by 1 on each new line. Ok, at first we create column variable with the value of 1
# This variable should be meaning of each new column. Next, We create outer while statement, where saying I am interested
# in only from 1 to 9. Next new essential variable row is being created. So, how it's possible to create kind of
# products of numbers, we create one more while inside statement and say while row <= column please multiply them,
# so let's say I have 1 for column, 1 for row, while row <= column is true we have 1 * 1 = 1. We need print statement
# to show the result, one catching moment here is that we change the default value of end='  ', to make vivid appearence.
# And extremely interesting moment is when we add 1 to row, so now row becomes 2 and inside while statement is not True
# anymore. So then we have print() empty for purposes to print next products on a new line and also finally we add
# column 1 too, because to jump to next product arrays. So, next I have column 2. Row one more time become 1 and we
# go inside while, yes, it's true row = 1 < column = 2, so we have 1 * 2 = 2, next row +1, one more True condition
# so, we have 2 * 2 = 4 and like that.

column = 1
while column <= 9:
    row = 1
    while row <= column:
        multiplied = row * column
        print(f'{row} * {column} = {multiplied}', end='  ')
        row += 1
    print()
    column += 1
