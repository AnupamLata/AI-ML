import json

# json_str = '{"name" : "Anupam", "isTeacher" : true}'
json_str = '{"name" : "Anupam", "isTeacher" : null}'

print(type(json_str))


# convert to python object

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)


