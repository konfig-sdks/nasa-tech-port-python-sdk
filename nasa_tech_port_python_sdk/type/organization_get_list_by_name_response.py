# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from nasa_tech_port_python_sdk.type.organization import Organization

class RequiredOrganizationGetListByNameResponse(TypedDict):
    pass

class OptionalOrganizationGetListByNameResponse(TypedDict, total=False):
    organizations: typing.List[Organization]

class OrganizationGetListByNameResponse(RequiredOrganizationGetListByNameResponse, OptionalOrganizationGetListByNameResponse):
    pass
