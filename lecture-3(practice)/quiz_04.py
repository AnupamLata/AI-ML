# given a tuple of integers, create:
# -> A tuple of all even numbers
# -> A tuple of all odd numbers

t = (1,2,3,4,5,6,7,8,9)

even = []
odd = []

for i in t:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i) 


# convert lists to tuples

odd_tuple = tuple(odd)
even_tuple = tuple(even)

print("even numbers tuple: " , even_tuple)
print("odd numbers tuple: ", odd)



# another method
t1 = (4,5,6,7,8,9,10,11,12)

even_tup = tuple(i for i in t1 if i % 2 == 0)
odd_tup = tuple(i for i in t1 if i %2 != 0)

print("even :" , even_tup)
print("odd : " , odd_tup)
