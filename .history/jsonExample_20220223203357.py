import json

x = '{"firstName":"John","lastName":"Doe" }'

obj = json.loads(x)

print(obj["firstName"])
