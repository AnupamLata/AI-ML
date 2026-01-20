# Ask the user for:Principal(P), Rate(R), Time(T), . Convert all to Float and compute simple interest :
# SI = (P * R * T)/ 100

P = float(input("enter principal amount: "))
R = float(input("enter rate of interest: "))
T = float(input("enter time(in year): "))

SI = (P * R * T)/ 100

print("Simple interest is: ",SI)
