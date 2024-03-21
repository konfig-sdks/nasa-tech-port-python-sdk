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


class OrganizationType(BaseModel):
    # Unique ID for this organization type.
    organization_type_id: typing.Optional[int] = Field(None, alias='organizationTypeId')

    # The name of the organization type.
    name: typing.Optional[str] = Field(None, alias='name')

    # Whether or not the type has child types.
    has_children: typing.Optional[bool] = Field(None, alias='hasChildren')

    # The relative level of the organization type in the heirarchy.
    level: typing.Optional[str] = Field(None, alias='level')

    # Unique ID for the parent type in the heriarchy.
    parent_id: typing.Optional[int] = Field(None, alias='parentId')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
