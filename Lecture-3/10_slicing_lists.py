# slicing lists

marks = [99, 89, 100, 65 ,92, "abc", 100.98]

print(marks[0:5])
# Or     (same)
print(marks[:5])

print(marks[5:len(marks)])
#  or   (same)
print(marks[5:])


# negative indexing
print(marks[-4: -2])
