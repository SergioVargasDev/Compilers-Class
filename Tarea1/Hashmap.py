
hashMap = {}
print(f"The hashMap initialized is {hashMap}")
print("--------------------------------")

print("Inserting key-value pairs")
hashMap["name"] = "Sergio"
print(dict(hashMap))
hashMap["age"] = 21
print(dict(hashMap))
hashMap["city"] = "Monterrey"
print(dict(hashMap))
print("--------------------------------")

print("Accessing values")
print(f"Name: {hashMap['name']}")
print(f"Age: {hashMap['age']}")
print(f"City: {hashMap['city']}")
print("--------------------------------")

print("Updating values")
hashMap["age"] = 22
print(dict(hashMap))
print("--------------------------------")

print("Deleting a key")
del hashMap["city"]
print(dict(hashMap))
print("--------------------------------")

print("Checking keys")
print(f"Does 'name' exist? {'name' in hashMap}")
print(f"Does 'city' exist? {'city' in hashMap}")
print("--------------------------------")

print(f"The size of the hashMap is: {len(hashMap)}")
print("--------------------------------")