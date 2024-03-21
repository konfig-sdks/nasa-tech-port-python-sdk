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


class File(BaseModel):
    # Unique identifier for the file.
    file_id: typing.Optional[int] = Field(None, alias='fileId')

    # The TechPort URL at which the file is accessible for download.
    url: typing.Optional[str] = Field(None, alias='url')

    # The size of the file in bytes.
    file_size: typing.Optional[int] = Field(None, alias='fileSize')

    # The file extension for the file.
    file_extension: typing.Optional[str] = Field(None, alias='fileExtension')

    # The file name.
    file_name: typing.Optional[str] = Field(None, alias='fileName')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
