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


class RequiredLkuCodeType(TypedDict):
    pass

class OptionalLkuCodeType(TypedDict, total=False):
    # Description of the LKU Code Type
    description: str

    # Unique ID for this LKU Code Type
    lkuCodeTypeId: int

    # Unique text code type that represents this LKU Code
    codeType: str

class LkuCodeType(RequiredLkuCodeType, OptionalLkuCodeType):
    pass
