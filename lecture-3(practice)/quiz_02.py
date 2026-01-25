# given a list of integers compute the average of all numbers in the list.

l = [10, 20, 30, 40, 50]
total =0

for i in l:
    total = total + i

average = total / len(l)
print("average =", average)

# or

l2 = [ 10, 30, 20, 60 ]

average = sum(l2) / len(l)

print("average : " , average)
