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


class LkuCodeType(BaseModel):
    # Description of the LKU Code Type
    description: typing.Optional[str] = Field(None, alias='description')

    # Unique ID for this LKU Code Type
    lku_code_type_id: typing.Optional[int] = Field(None, alias='lkuCodeTypeId')

    # Unique text code type that represents this LKU Code
    code_type: typing.Optional[str] = Field(None, alias='codeType')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
