# json.dumps()
import json

py_obj = {
    "name" : "anupam",
    "isTeacher" : True
}

json_str = json.dumps(py_obj)

print(type(json_str), json_str)
