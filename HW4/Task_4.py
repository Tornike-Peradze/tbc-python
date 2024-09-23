n = int(input("Please enter positive whole number: "))

# Here we have kind of Fibonacci sequence, where next member of the sequence is the sum of before two. Also,
# first two numbers are known, there are - 0, 1. So, our main task is to find what is the n-th number value.
# For example, if the input of n is 4. In Fibonacci sequence 4th number is - 0, 1, 2, 3. So the answer is 3.
# How we do that, at first we create known variables - 0, 1. Then, we check for not correct input number - 0.
# But the most interesting part is in else part, for the range we use n + 1, because to go as far as the input is
# and after that for the every next iteration for every next member, we say at first a = b and b = sum of
# before two numbers
if n < 0 or n > 20:
    print("Please enter positive number from 0 to 20!")
else:
    a = 0
    b = 1
    if n == 0:
        print("The number is 0.")
    else:
        for i in range(2, n + 1):
            a, b = b, a + b
        print(b)