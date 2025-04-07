import json
input_file = open('student.json', 'r')
data = json.load(input_file)
print(data)
print()

input_file.close()

output_file = open('butterfiles.json', 'w')
d = {'painted lady': 1, 'bronze copper': 2, 'monarch': 5}
json.dump(d, output_file)