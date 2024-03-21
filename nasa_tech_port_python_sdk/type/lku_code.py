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

from nasa_tech_port_python_sdk.type.lku_code_type import LkuCodeType

class RequiredLkuCode(TypedDict):
    pass

class OptionalLkuCode(TypedDict, total=False):
    # Description of the LKU Code
    description: str

    # Unique ID for this LKU Code
    lkuCodeId: int

    # Unique text code that represents this LKU Code
    code: str

    # Unique ID for the LKU Code Type
    lkuCodeTypeId: int

    lkuCodeType: LkuCodeType

    # Display order
    displayOrder: int

class LkuCode(RequiredLkuCode, OptionalLkuCode):
    pass
