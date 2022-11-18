import requests, json

data = {
    'id': 1,
    'name': 'lily',
    'age': 11,
    'birthplace': 'san',
    'grade': 123
}
url = 'http://10.10.30.46:5000/url='

r = requests.post(url, data=json.dumps(data))
print(r.json())


