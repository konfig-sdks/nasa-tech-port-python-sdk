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


class RequiredProjectFindMatchingProjectsResponseItem(TypedDict):
    pass

class OptionalProjectFindMatchingProjectsResponseItem(TypedDict, total=False):
    title: str

    description: str

    id: int

class ProjectFindMatchingProjectsResponseItem(RequiredProjectFindMatchingProjectsResponseItem, OptionalProjectFindMatchingProjectsResponseItem):
    pass
