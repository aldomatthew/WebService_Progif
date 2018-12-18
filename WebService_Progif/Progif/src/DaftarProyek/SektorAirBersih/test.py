import json

source_file = open("SektorAirdanSanitas.json")

json_data = json.load(source_file)

print (json_data)
