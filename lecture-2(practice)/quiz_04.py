# Write a function to return the count the number of digits in a number, n .

def count_digits(n):
    if n == 0:
        return 1
    
    n = abs(n)   # for negative counting the digits when there is a negative sign before any number
    count = 0

    while n > 0:
        n = n //10
        count += 1

    return count 


num = int(input("Enter the number: "))
print(f"count_digit = {count_digits(num)}")

