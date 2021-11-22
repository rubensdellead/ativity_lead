import requests
import json

def get_url():
    return 'https://test.jasgme.com/sgme/api/health'

def get_valid_credentials():
    return {'login': 'rubens.moreira@dellead.com', 'password': 'mengao123'}

def get_token():
    url = get_url()
    credentials_body = get_valid_credentials()

    assert response.status_code == 200

    json_data = json.loads(response.text)

    token = json_data['token']

    auth = f'Bearer {token}

    return auth