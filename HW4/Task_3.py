num = int(input("Please enter a whole positive integer: "))

# Here, in this program main breakthrough moment is in 'num % i == 0' and why? At first, we use loop to
# iterate over from 1 to num(included, that's why here written +1) and for each iteration we check if input
# num could divide whole on each iterated number and if it's possible let's print them.
if num <= 0:
    print("Please enter a whole positive number!")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end = ' ')