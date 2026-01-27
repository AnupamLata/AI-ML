# given a list of words:
# words = ["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length.Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}
for w in words:
    result[w] = len(w)

print(result)    


# method 2
words = ["apple", "banana", "kiwi", "cherry", "mango"]
print({w : len(w) for w in words})
