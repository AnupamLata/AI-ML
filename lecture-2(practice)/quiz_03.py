# Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]


def print_digits(n):
    if n == 0:
        print(0)
        return

    digits = []

    # Extract digits
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10

    # Reverse to print in correct order
    digits.reverse()

    # Print digits
    for d in digits:
        print(d)


# Example
n = int(input("Enter a number: "))
print_digits(n)



def print_digits(n):
    while n > 0:
        print(n % 10)
        n = n // 10 


n = int(input("Enter a number: "))
print_digits(n)
