# Create a dictionary where:
# •Keys = student names
# •Values = marks(integer) 
# Write a menu-based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)depending on the operation they want to perform on the dictionary: 
# 1. A-Add a student  
# 2. B-Update marks 
# 3. C-Search for a student 
# 4. D-Display all students and marks

students = {}

while True:
    print("\nA-Add  B-Update  C-Search  D-Display  E-Exit")
    ch = input("Enter choice: ").upper()

    if ch == 'A':
        name = input("Name: ")
        students[name] = int(input("Marks: "))

    elif ch == 'B':
        name = input("Name: ")
        if name in students:
            students[name] = int(input("New Marks: "))
        else:
            print("Student not found")

    elif ch == 'C':
        name = input("Name: ")
        print(students[name] if name in students else "Student not found")

    elif ch == 'D':
        for s, m in students.items():
            print(s, ":", m)

    elif ch == 'E':
        break
