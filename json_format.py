import sys
import json

file_name = sys.argv[1]

try:
	with open(file_name) as file:
		contents = json.load(file)
except ValueError as e:
	print("Invalid JSON file. Reason:")
	sys.exit(e)

formatted_contents = json.dumps(contents, sort_keys=True, indent=4)

with open(file_name, "w") as file:
	file.write(formatted_contents)