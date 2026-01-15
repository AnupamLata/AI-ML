username = input("enter username: ")
password = input("enter pass: ")

if(username == "admin" and password == "pass"):
    print("success")
else:
    if(username != "admin"):
        print("Wrong username")
    else:
        print("Wrong password")       
