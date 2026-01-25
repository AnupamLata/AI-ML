# given a lsit of tuples with info(name, subject):
# -> list all unique course
# -> list students enrolled in english
# -> create dictionary  (student, set of courses)

info =[
    ("Alice" , "Math"),
    ("Bob" , "science"),
    ("Alice" , "science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math" ),
    ("Alice" , "English"),
    ("Charlie" , "English"),
]
# 1
unique_courses = set()

for tup in info:
    # print(tup)
    # print(tup[0])  # access the name
    # print(tup[1])  #access the course

    unique_courses.add(tup[1])

print(unique_courses)   


# 2
for name, course in info:
    if(course == "English"):
        print(name)


# 3
dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)

    else:
        dict[name].add(course)    
print(dict)
