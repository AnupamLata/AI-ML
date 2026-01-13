# the user enters a string containing a number (e.g.. "45"). convert it to:
#  an integer
#  a float
#  a string again
    #  print all three values with their types.


num_str = input("enter a number as a string: ")

num_int = int(num_str)
num_float = float(num_str)
num_string_again = str(num_str)

print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_string_again, type(num_string_again))
