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

from nasa_tech_port_python_sdk.pydantic.organization import Organization
from nasa_tech_port_python_sdk.pydantic.program import Program

class Program(BaseModel):
    # Title for the program
    title: typing.Optional[str] = Field(None, alias='title')

    # Description for the program
    description: typing.Optional[str] = Field(None, alias='description')

    # Unique ID for this program
    program_id: typing.Optional[int] = Field(None, alias='programId')

    # Acronym for this program
    acronym: typing.Optional[str] = Field(None, alias='acronym')

    # True if the program is still active
    active: typing.Optional[bool] = Field(None, alias='active')

    parent_program: typing.Optional["Program"] = Field(None, alias='parentProgram')

    # Unique ID for the parent program
    parent_program_id: typing.Optional[int] = Field(None, alias='parentProgramId')

    responsible_md: typing.Optional[Organization] = Field(None, alias='responsibleMd')

    # Unique ID for the parent responsible mission directorate
    responsible_md_id: typing.Optional[int] = Field(None, alias='responsibleMdId')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
