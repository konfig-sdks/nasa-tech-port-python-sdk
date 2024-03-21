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

from nasa_tech_port_python_sdk.type.organization import Organization
from nasa_tech_port_python_sdk.type.program import Program

class RequiredProgram(TypedDict):
    pass

class OptionalProgram(TypedDict, total=False):
    # Title for the program
    title: str

    # Description for the program
    description: str

    # Unique ID for this program
    programId: int

    # Acronym for this program
    acronym: str

    # True if the program is still active
    active: bool

    parentProgram: "Program"

    # Unique ID for the parent program
    parentProgramId: int

    responsibleMd: Organization

    # Unique ID for the parent responsible mission directorate
    responsibleMdId: int

class Program(RequiredProgram, OptionalProgram):
    pass
