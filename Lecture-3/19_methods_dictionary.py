# methods of dictionary

info = {
    "name" : "Anupam",
    "cgpa" : 9.5,
    " subjects" : ["math" , "science"],
    3.14 : "PI"
}

# d.keys()  -> returns all keys
dict_keys = info.keys()
print(dict_keys)
   # or
print(info.keys())

   # typecasting
dict_keys = list(info.keys())
print(dict_keys)
print(type(dict_keys))



# d.values()  -> returns all values
dict_vals = info.values()
print(dict_vals)
print(list(dict_vals))



# d.items()  -> returns (key, val) pairs
print(info.items())



# d.get(val) -> returns val acc. to key
print(info.get("cgpa"))
print(info.get("cgpa23"))
print("end of code")



# d.update(new_item)  -> adds new item to dict
info.update({
    "city" : "Delhi"
})

print(info)
