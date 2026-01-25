# Ask the user for a string and check whether it is a palindrome or not. A palindrome is a string which is same when we read it forward & backward . Eg - "madam", "racecar" etc.

s = input("enter a string: ")

rev = ""  #zero character

for ch in s:
    rev = ch + rev

if s == rev:
    print("palindrome")

else:
    print("Not Palindrome")        
