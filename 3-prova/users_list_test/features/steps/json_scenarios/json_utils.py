import requests
import json


def get_url():
    return 'https://test.jasgme.com/sgme/api'


def get_valid_credentials():
    return {'login': 'rubens.moreira@dellead.com', 'password': 'mengao123'}


def authentication_token():
    url = get_url()
    data = get_valid_credentials()

    response = requests.post(f'{url}/authenticate/login', json=data)
    assert response.status_code == 200
    json_data = json.loads(response.text)

    token = json_data['token']
    authorization = f'Bearer {token}'
    return authorization