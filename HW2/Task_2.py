# Just getting numbers from console, and checking whether remainder of the division of A by B is zero and returning
# the appropriate result

A = int(input("First number: "))
B = int(input("Second number: "))

if B != 0 and A % B == 0:
    print(f"{A} is a multiple of {B}.")
else:
    print(f"{A} is not a multiple of {B}.")