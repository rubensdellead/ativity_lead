import unittest
import os
import requests
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class financial(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_financial_id(self):
        auth = authentication_token()

        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/financial-strategy/{61}', headers=header)
        assert response.status_code == 200


        json_data = json.loads(response.text)
        self.assertIn('id', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['id']), int)

        self.assertIn('id', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['id']), int)

        self.assertIn('id', json_data['salePrice']['company'])
        self.assertEqual(type(json_data['salePrice']['company']['id']), int)

        #recomeço salePrice

        self.assertIn('price_1', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['price_1']), float)

        self.assertIn('price_2', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['price_2']), float)

        self.assertIn('price_3', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['price_3']), float)

        self.assertIn('price_me', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['price_me']), float)

        self.assertIn('rentability', json_data['salePrice'])
        self.assertEqual(type(json_data['salePrice']['rentability']), float)

        self.assertIn('office_supplies', json_data['fixedCost'])
        self.assertEqual(type(json_data['fixedCost']['office_supplies']), float)

        for item in json_data['directMaterials']:
            self.assertIn('description', item)
            self.assertEqual(type(item['description']), str)

            self.assertIn('value', item)
            self.assertEqual(type(item['value']), float)

            self.assertIn('quantity', item)
            self.assertEqual(type(item['quantity']), float)
        #formulas

        self.assertIn('sumOfRentFixedCosts', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumOfRentFixedCosts']), float)

        self.assertIn('sumSalaryFixedCosts', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumSalaryFixedCosts']), float)

        self.assertIn('sumOfSocialChargesFixedCosts', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumOfSocialChargesFixedCosts']), float)

        self.assertIn('otherFixedCosts', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['otherFixedCosts']), float)

        self.assertIn('sumCommission', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumCommission']), float)

        self.assertIn('sumCommissionCharges', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumCommissionCharges']), float)

        self.assertIn('sumTaxForSale', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['sumTaxForSale']), float)

        self.assertIn('otherVariableCosts', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['otherVariableCosts']), float)

        self.assertIn('contribution', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['contribution']), float)

        self.assertIn('balance', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['balance']), float)

        self.assertIn('balanceNetProfit', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['balanceNetProfit']), float)

        self.assertIn('profit', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['profit']), float)

        self.assertIn('unitsToProduce', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['unitsToProduce']), float)
        #
        self.assertIn('verifySalesGoalAndBreakevenPoint', json_data)
        self.assertEqual(type(json_data['verifySalesGoalAndBreakevenPoint']), bool)

        self.assertIn('hasActionsPermission', json_data)
        self.assertEqual(type(json_data['hasActionsPermission']), bool)

        print()
