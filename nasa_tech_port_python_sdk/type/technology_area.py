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


class RequiredTechnologyArea(TypedDict):
    pass

class OptionalTechnologyArea(TypedDict, total=False):
    # The title of the Technology Area.
    title: str

    # Unique identifier for the Technology Area.
    id: int

    # The code identifier for the Technology Area.
    code: str

class TechnologyArea(RequiredTechnologyArea, OptionalTechnologyArea):
    pass
