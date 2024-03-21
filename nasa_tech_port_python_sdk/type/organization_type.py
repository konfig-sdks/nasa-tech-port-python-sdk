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


class RequiredOrganizationType(TypedDict):
    pass

class OptionalOrganizationType(TypedDict, total=False):
    # Unique ID for this organization type.
    organizationTypeId: int

    # The name of the organization type.
    name: str

    # Whether or not the type has child types.
    hasChildren: bool

    # The relative level of the organization type in the heirarchy.
    level: str

    # Unique ID for the parent type in the heriarchy.
    parentId: int

class OrganizationType(RequiredOrganizationType, OptionalOrganizationType):
    pass
