import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_user(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user

    return ''
