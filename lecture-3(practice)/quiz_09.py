# Given a list , print all elements that appear more than once in the list.
# [HINT - use sets]

lst = [ 1,2,1,4,5,2,3,6]

result = set()

for i in lst:
    if lst.count(i) > 1:
        result.add(i)

print("elements appearing more than once :", result)     
