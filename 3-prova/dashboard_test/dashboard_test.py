import unittest
import os
import requests
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class dashboard(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_dashboard_id(self):
        auth = authentication_token()

        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/dashboard/{61}', headers=header)
        assert response.status_code == 200


        json_data = json.loads(response.text)

        for item in json_data['journeys']:
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)

            self.assertIn('sort_order', item)
            self.assertEqual(type(item['sort_order']), int)

            self.assertIn('current', item)
            self.assertEqual(type(item['current']), bool)

            self.assertIn('open', item)
            self.assertEqual(type(item['open']), bool)

        self.assertIn('breakevenPoint', json_data['goals'])
        self.assertEqual(type(json_data['goals']['breakevenPoint']), float)

        self.assertIn('salesGoal', json_data['goals'])
        self.assertEqual(type(json_data['goals']['salesGoal']), float)

        self.assertIn('totalTaxForSale', json_data['goals'])
        self.assertEqual(type(json_data['goals']['totalTaxForSale']), float)

        self.assertIn('unitBP', json_data['goals'])
        self.assertEqual(type(json_data['goals']['unitBP']), float)

        self.assertIn('unitSG', json_data['goals'])
        self.assertEqual(type(json_data['goals']['unitSG']), float)

        self.assertIn('progressPlaning', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressPlaning']), float)

        self.assertIn('progressRH', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressRH']), float)

        self.assertIn('progressProduction', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressProduction']), int)

        self.assertIn('progressMarketing', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressMarketing']), int)

        self.assertIn('progressFinancial', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressFinancial']), float)

        self.assertIn('retired', json_data['saleDevolutionInfo'])
        self.assertEqual(type(json_data['saleDevolutionInfo']['retired']), int)

        self.assertIn('stock', json_data['saleDevolutionInfo'])
        self.assertEqual(type(json_data['saleDevolutionInfo']['stock']), int)

        self.assertIn('totalProductsSelled', item)
        self.assertEqual(type(item['totalProductsSelled']), float)

        self.assertIn('percentAveragePresence', item)
        self.assertEqual(type(item['percentAveragePresence']), float)

        self.assertIn('actionsProfitability', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['actionsProfitability']), float)

        self.assertIn('totalShareCapital', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['totalShareCapital']), float)

        self.assertIn('productionGoal', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['productionGoal']), float)

        self.assertIn('saleGoal', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['saleGoal']), float)

        self.assertIn('provider', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['provider']), float)

        self.assertIn('income', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['income']), float)

        self.assertIn('sales', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['sales']), float)

        self.assertIn('rent', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['rent']), float)

        self.assertIn('taxForSales', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['taxForSales']), float)

        self.assertIn('socialCompanyCharges', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['socialEmployeeCharges']), float)

        self.assertIn('comissions', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['comissions']), float)

        self.assertIn('netProfit', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['netProfit']), float)

        self.assertIn('taxes', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['taxes']), float)

        self.assertIn('finalProfit', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['finalProfit']), float)

        self.assertIn('finalProfit', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['finalProfit']), float)

        self.assertIn('provider', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['provider']), float)

        self.assertIn('income', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['income']), float)

        self.assertIn('sales', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['sales']), float)

        self.assertIn('rent', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['rent']), float)

        self.assertIn('taxForSales', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['taxForSales']), float)

        self.assertIn('socialCompanyCharges', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['socialEmployeeCharges']), float)

        self.assertIn('comissions', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['comissions']), float)

        self.assertIn('netProfit', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['netProfit']), float)

        self.assertIn('taxes', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['taxes']), float)

        self.assertIn('finalProfit', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['finalProfit']), float)

        self.assertIn('finalProfit', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['finalProfit']), float)









