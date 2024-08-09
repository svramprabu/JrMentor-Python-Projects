def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    # If no factors are found, the number is prime
    return True

# Example usage:
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
