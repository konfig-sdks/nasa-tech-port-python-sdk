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

from nasa_tech_port_python_sdk.pydantic.file import File

class LibraryItem(BaseModel):
    # Title of the library item
    title: typing.Optional[str] = Field(None, alias='title')

    # Description of the library item.
    description: typing.Optional[str] = Field(None, alias='description')

    # Unique identifier for the library item.
    id: typing.Optional[int] = Field(None, alias='id')

    content_type: typing.Optional[LkuCode] = Field(None, alias='contentType')

    # List of files associated with the library item.
    files: typing.Optional[typing.List[File]] = Field(None, alias='files')

    # External URL for the library item.
    url: typing.Optional[str] = Field(None, alias='url')

    # Date the library item was published.
    published_date_string: typing.Optional[str] = Field(None, alias='publishedDateString')

    # Publisher of the library item.
    published_by: typing.Optional[str] = Field(None, alias='publishedBy')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
