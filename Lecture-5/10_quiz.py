try:
    x = int(input("enter x: "))
    ans = 15/x

except ZeroDivisionError:
    print(f"divide by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:
    print(f"ans = {ans}")    

finally:
    print("end of program")            
