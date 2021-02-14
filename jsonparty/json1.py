import json
data = '''[ "Glenn", "Sally", "Jen" ]'''

info = json.loads(data)
print(info[0])
