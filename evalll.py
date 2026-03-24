import json

filename="eval2.json"

with open(filename,"r") as f:
    data=json.load(f)

data.reverse()

new_data=[]

for entry in data:
    entry=dict(reversed(list(entry.items())))

for item in data:
    item={v:k for k,v in item.items()}
    new_data.append(item)

with open(filename,"w") as f:
    json.dump(new_data,f,indent=4)
print(new_data)
