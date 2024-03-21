# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

import typing
from urllib3._collections import HTTPHeaderDict
from nasa_tech_port_python_sdk.configuration import Configuration

def request_before_hook(
        resource_path: str,
        method: str,
        configuration: Configuration,
        path_template: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Any = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any
):
    pass