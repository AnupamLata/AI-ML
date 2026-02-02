f = open("01_fileSample.txt" , "r") #file object

# data = f.read()
# print(type(data))


# or line by line read
data = f.readline()
print(data)
data = f.readline()
print(data)


f.close()

