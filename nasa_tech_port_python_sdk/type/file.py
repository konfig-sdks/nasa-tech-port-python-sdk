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


class RequiredFile(TypedDict):
    pass

class OptionalFile(TypedDict, total=False):
    # Unique identifier for the file.
    fileId: int

    # The TechPort URL at which the file is accessible for download.
    url: str

    # The size of the file in bytes.
    fileSize: int

    # The file extension for the file.
    fileExtension: str

    # The file name.
    fileName: str

class File(RequiredFile, OptionalFile):
    pass
