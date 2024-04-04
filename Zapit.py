import requests

def get_nationality_probability(name):
    url = f"https://api.nationalize.io?name={name}"
    response = requests.get(url)
    data = response.json()
    return data

name = "John"
result = get_nationality_probability(name)
print(f"Для імені '{name}':")
print("Ймовірність національностей:")
for item in result['country']:
    print(f"{item['country_id']}: {item['probability']}")
