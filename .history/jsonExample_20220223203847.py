import json

x = '{"firstName":"John","lastName":"Doe" }'
obj = json.loads(x)
print(obj["firstName"])
print("Last name= ", obj["lastName"])


json.dumps({"firstName":"Akash"})
json.dumps({"lastName":"Doe"})