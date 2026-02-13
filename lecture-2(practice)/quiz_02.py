# Write a function that takes two integers and and prints all even
#  numbers between them (inclusive).

def even_numbers(a, b):
    
    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

# Example call
even_numbers(4, 15)
