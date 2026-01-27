# Ask the user for a string and print :
# •All unique characters 
#  •The count of unique characters

s = input("enter a string: ")

unique_chars = set(s) 

print("unique characters: " , unique_chars)
print("count of unique characters:" ,len(unique_chars))
