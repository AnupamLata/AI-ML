# write a program to check whether two lists share no common elements.
# share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]
# [HINT - use sets]

list1 = [1,2,3,4]
list2 = [5,6,7,8]

# set1 = set(list1)
# set2 = set(list2)

common = set(list1).intersection(set(list2))

if common:
    print("common element found:", common)

else:
    print("no common element") 

#  share common elements list3 =[1,2,3] list4 =[3,4]

list3 = [1,2,3]
list4 = [3,4]

common  = set(list3) & set(list4)

if common:
    print("common element: ", common)

else:
    print("no common element")    

