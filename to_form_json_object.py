import json
# convert from JSON to Python
student_record = '{"first_name": "Lucy", "year": 1, "College": "Dawson"}'
parsed_record = json.loads(student_record)

print(parsed_record)
print(type(parsed_record))

# convert from Python to JSON
student_dict = {'name': 'Lucy', 'year': 1, 'College': 'Dawson'}
student_record_json = json.dumps(student_dict)
print(student_record_json)

print('\n\n')

print(json.dumps({'name': 'Lucy', 'year': 1}))
print(json.dumps(['red', 'blue', 'green']))