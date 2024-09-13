A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))

if B != 0 and A % B == 0:
    print(f"{A} is a multiple of {B}.")
else:
    print(f"{A} is not a multiple of {B}.")
