import json

x = '{"firstName":"John","lastName":"Doe" }'
obj = json.loads(x)
print(obj["firstName"])
print("Last name= ", obj["lastName"])


print(json.dumps({"firstName":"Akash"}))
print(json.dumps({"lastName":"Doe"}))
