import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url=url)

result = response.json()
people = result['people']

people_list = []

for person in people:
    people_list.append(person['name'])

print(', '.join(people_list))
