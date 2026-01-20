# Ask the user for : Principle (P) , Rate (R) , Time (T). convert all to float,  then calculate and print temperature in Fahrenheit.
# conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32

celsiusTemp = float(input("Enter temperature in celsius: "))

fahrenheitTemp = (celsiusTemp * (9/5)) + 32

print("temperature in fahrenheit is: " ,fahrenheitTemp)
