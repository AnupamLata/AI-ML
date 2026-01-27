# write a program that takes a string from the user and prints the number of spaces in the string.

string = input("Enter a string: ")

count = 0
for ch in string:
    if ch == ' ':
        count += 1

print("number of space :", count)        
