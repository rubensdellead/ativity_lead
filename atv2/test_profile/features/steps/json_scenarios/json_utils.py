import requests
import json
def get_url():
    return 'https://test.jasgme.com/sgme/api'


def get_valid_credentials():
    return {'login': 'rubens.moreira@dellead.com', 'password': 'mengao123'}


def get_token():
    url = get_url()
    log = get_valid_credentials()
    response = requests.post(f'{url}/authenticate/login', json=log)
    assert response.status_code == 200
    json_data = json.loads(response.text)
    token = json_data['token']
    alth = f'Bearer {token}'
    return alth


