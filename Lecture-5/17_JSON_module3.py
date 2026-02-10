# JSON.laod()
import json

with open("15_data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)
    print(type(py_obj))
