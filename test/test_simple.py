# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

import unittest

import os
from pprint import pprint
from nasa_tech_port_python_sdk import NasaTechPort

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        nasatechport = NasaTechPort(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(nasatechport)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
