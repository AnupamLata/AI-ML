# Write a function to return the sum of digits of a number, n .

def sum_of_digits(n):
    n = str(abs(n))   # Convert number to string & handle negative
    total = 0

    for digit in n:
        total += int(digit)

    return total


num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))



