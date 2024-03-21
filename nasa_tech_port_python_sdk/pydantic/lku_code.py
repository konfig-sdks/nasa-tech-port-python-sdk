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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from nasa_tech_port_python_sdk.pydantic.lku_code_type import LkuCodeType

class LkuCode(BaseModel):
    # Description of the LKU Code
    description: typing.Optional[str] = Field(None, alias='description')

    # Unique ID for this LKU Code
    lku_code_id: typing.Optional[int] = Field(None, alias='lkuCodeId')

    # Unique text code that represents this LKU Code
    code: typing.Optional[str] = Field(None, alias='code')

    # Unique ID for the LKU Code Type
    lku_code_type_id: typing.Optional[int] = Field(None, alias='lkuCodeTypeId')

    lku_code_type: typing.Optional[LkuCodeType] = Field(None, alias='lkuCodeType')

    # Display order
    display_order: typing.Optional[int] = Field(None, alias='displayOrder')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
