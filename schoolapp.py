import requests
import json

url = ''

data = {
    'name' : 'Dushyant',
'eid' : 88167,
'city':'Delhi',
'dept':'IT'
}

json_data = json.dumps(data)

r = requests.post(url=url,data=json_data)
d = r.json()
print(d)