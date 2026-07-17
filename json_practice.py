import json

data = {"name": "Soomin", "level": 2, "topics": ["math", "json"]}

# dict -> json string
text = json.dumps(data)
print(text) # {"name": "Soomin", "level": 2, "topics": ["math", "json"]}

# json string -> dict
back = json.loads(text)
print(back["name"]) # Soomin

#pretty-print
print(json.dumps(data, indent=2)) 


#writing/reading a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2) # dict -> json string and write to file

with open("data.json", "r") as f:
    loaded = json.load(f) # file -> dict

    