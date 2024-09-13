# Instead of calculating whether each number is prime, I just use a predefined list of prime numbers less than or
# equal to 10
def prime_divisors(num):
    prime_numbers = [2, 3, 5, 7]  # <= 10
    divisors = [p for p in prime_numbers if num % p == 0]
    return divisors


# Simply, list comprehension to find prime divisors by checking if the input number is divisible by any of the primes
# in the list.
number = input("Enter an integer: ")

if number.isdigit():
    number = int(number)

    if 1 <= number <= 10:
        prime_divisors = prime_divisors(number)

        if prime_divisors:
            print("Prime divisors:", ", ".join(map(str, prime_divisors)))
        else:
            print(f"{number} does not have prime divisors.")
    else:
        print("Error: Enter number between 1 and 10.")
else:
    print("Error: Enter valid integer.")