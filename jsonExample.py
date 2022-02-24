import json

x = '{"firstName":"John","lastName":"Doe" }'
obj = json.loads(x)
print(obj["firstName"])
print("Last name= ", obj["lastName"])


print(json.dumps({"firstName":"Akash", "lastName":"Doe"}))
print(json.dumps({"lastName":"Doe"}))


#a = '{"employees":[{"firstName":"John","lastName":"Doe" }, {"firstName":"Anna","lastName":"Smith" },{"firstName":"Peter","lastName":"Jones" }]}'



