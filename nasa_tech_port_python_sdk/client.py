# coding: utf-8
"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

import typing
import inspect
from datetime import date, datetime
from nasa_tech_port_python_sdk.client_custom import ClientCustom
from nasa_tech_port_python_sdk.configuration import Configuration
from nasa_tech_port_python_sdk.api_client import ApiClient
from nasa_tech_port_python_sdk.type_util import copy_signature
from nasa_tech_port_python_sdk.apis.tags.organization_api import OrganizationApi
from nasa_tech_port_python_sdk.apis.tags.project_api import ProjectApi
from nasa_tech_port_python_sdk.apis.tags.resource_api import ResourceApi



class NasaTechPort(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.organization: OrganizationApi = OrganizationApi(api_client)
        self.project: ProjectApi = ProjectApi(api_client)
        self.resource: ResourceApi = ResourceApi(api_client)
