import requests

url = 'https://dummyjson.com/todos'

params = {
    'limit' : 150
}

response = requests.get(url=url, params=params)

result = response.json()
todos = result['todos']

not_completed_list = []

for todo in todos:
    if not todo['completed']:
        not_completed_list.append(todo['todo'])

print(', '.join(not_completed_list))
