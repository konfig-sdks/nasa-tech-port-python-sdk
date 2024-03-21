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

from nasa_tech_port_python_sdk.type.file import File

class RequiredLibraryItem(TypedDict):
    pass

class OptionalLibraryItem(TypedDict, total=False):
    # Title of the library item
    title: str

    # Description of the library item.
    description: str

    # Unique identifier for the library item.
    id: int

    contentType: LkuCode

    # List of files associated with the library item.
    files: typing.List[File]

    # External URL for the library item.
    url: str

    # Date the library item was published.
    publishedDateString: str

    # Publisher of the library item.
    publishedBy: str

class LibraryItem(RequiredLibraryItem, OptionalLibraryItem):
    pass
