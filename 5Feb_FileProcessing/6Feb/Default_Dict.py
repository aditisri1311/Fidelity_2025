from collections import defaultdict
def dc():
    return "Key not found"
d1= defaultdict(dc)
d1["name"] = "Aditi"
d1["age"] = 22

# Accessing existing keys
print(d1["name"])  # Output: Aditi
print(d1["age"])   # Output: 22

# Accessing a missing key
print(d1["city"])  # Output: Key not found
