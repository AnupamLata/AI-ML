nums = [-2, -3, 3, 4, -1, 7]

# want -> [0, 0, 3, 4, 0, 7]

nums = [0 if val < 0 else val for val in nums]
print(nums)
