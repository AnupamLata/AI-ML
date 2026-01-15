age =int(input("enter age: "))
# age =float(input("enter age: "))

if (age < 13):
    print("child")
elif (age >= 13 and age < 18): # 13-18
    print("teenager")   
elif (age > 18):
    print("adult")         
