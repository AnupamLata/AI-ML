# Write a program that takes as input. Using conditional statements,
# calculate the based on these rules:
# Q1 salary
# final tax rate
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

# Take salary input
salary = int(input("Enter your salary: "))

# Apply conditions to calculate tax
if salary < 30000:
    tax_rate = 0.05
elif salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

# Calculate tax amount
tax = salary * tax_rate

# Print result
print("Salary:", salary)
print("Tax Rate:", tax_rate * 100, "%")
print("Tax Amount:", tax)
