#  lets l = [1,2,3,10,4]
# search x value  ; x=10(index of this value)


l = [1,2,3,10,4]

x = 10
idx = 0

for val in l:
    if(val == x):
        print(f"x found at idx = {idx}")
        print(f"{x} found at idx = {idx}")
        break
    idx += 1


    # all above code is linear search
