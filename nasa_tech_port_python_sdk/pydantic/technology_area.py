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


class TechnologyArea(BaseModel):
    # The title of the Technology Area.
    title: typing.Optional[str] = Field(None, alias='title')

    # Unique identifier for the Technology Area.
    id: typing.Optional[int] = Field(None, alias='id')

    # The code identifier for the Technology Area.
    code: typing.Optional[str] = Field(None, alias='code')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
