# input two lists of integers from the user. merge them into one list and sort the result.
# Eg - list1 = [1,2,7] , list2 = [2,4,5]
# result = [1,2,2,4,5,7]


list2 = list(map(int,input("enter second list element: ").split()))
list1 = list(map(int,input("enter first list elements: ").split()))

merged = list1 + list2

merged.sort()

print("result: " , merged)
