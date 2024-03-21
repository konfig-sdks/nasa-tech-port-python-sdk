# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

import unittest
from unittest.mock import patch

import urllib3

import nasa_tech_port_python_sdk
from nasa_tech_port_python_sdk.paths.api_projects_search import get
from nasa_tech_port_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProjectsSearch(ApiTestMixin, unittest.TestCase):
    """
    ApiProjectsSearch unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
