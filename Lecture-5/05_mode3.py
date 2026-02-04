# for r+

f = open("05_mode3.txt" , "r+")

# f.write("12345")
f.write("123")

print(f.read())

f.close()


# for  a+
f = open("05_mode3.txt" , "a+")

f.write("1234")
print(f.read())

f.close()

# for w+
f = open("05_mode3.txt" , "w+")

f.write("125")
print(f.read())

f.close()
