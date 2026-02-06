# create a square of list of numbers

squares = []

for i in range(6):
    squares.append(i*i)

print(squares)    

# this same question solve by list comprehensions 

sq = [i*i for i in range(6)]
print(sq)
