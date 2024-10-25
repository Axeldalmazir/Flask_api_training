import requests 
import json

response = requests.get('http://api.stackexchange.com/2.3/comments?order=desc&sort=creation&site=stackoverflow')

for data in response.json()['items']:
    print('---------------')
    print(data['owner'])