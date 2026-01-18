# print vowel count of a given string
#  word = "artificial"

word = "artificial"

count = 0

for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1

print(" no. of vowel " , count)        
