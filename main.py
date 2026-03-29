# Unifying two different data models

data1 = {"name": "Abi", "age": 21}
data2 = {"full_name": "Abi", "years": 21}

def unify(data):
    return {
        "full_name": data.get("name") or data.get("full_name"),
        "age": data.get("age") or data.get("years")
    }

print(unify(data1))
print(unify(data2))