# Take a Decimal number as input (like 45.78) and output its: 
#  . integer part - 45
#  . fractional part - .78     

num = float(input("enter decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part: ", int(num))
print("Fractional part: ", round(fractional_part , 2))
