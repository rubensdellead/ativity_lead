import unittest
import os
import requests
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class users(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_post_users_id(self):
        auth = authentication_token()

        header = {'Authorization': auth}
        params = {"start": 0, 'max': 10}
        body = {"name": "Rubens",
                "email": "rubens.moreira@dellead.com",
                "lastAccess": "",
                "profile": "",
                "country": "",
                "state": "",
                "institution": "",
                "responsible": "",
                "active": "true"}

        response = requests.post(f'{self.url}/users-list', headers=header, json=body, params=params)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for item in json_data['list']:
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)

            self.assertIn('name', item)
            self.assertEqual(type(item['name']), str)

            self.assertIn('email', item)
            self.assertEqual(type(item['email']), str)

            self.assertIn('lastAccess', item)
            self.assertEqual(type(item['lastAccess']),  str)

            self.assertIn('id', item['profile'])
            self.assertEqual(type(item['profile']['id']), int)

            self.assertIn('name', item['profile'])
            self.assertEqual(type(item['profile']['name']), str)

            self.assertIn('id', item['country'])
            self.assertEqual(type(item['country']['id']), int)

            self.assertIn('name', item['country'])
            self.assertEqual(type(item['country']['name']), str)

            self.assertIn('id', item['state'])
            self.assertEqual(type(item['state']['id']), int)

            self.assertIn('id', item['state'])
            self.assertEqual(type(item['state']['id']), int)

            self.assertIn('institution', item)
            self.assertEqual(type(item['institution']), str)

            self.assertIn('active', item)
            self.assertEqual(type(item['active']), bool)

        self.assertIn('total', json_data)
        self.assertEqual(type(json_data['total']), int)




