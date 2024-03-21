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

from nasa_tech_port_python_sdk.type.lku_code import LkuCode

class RequiredLocation(TypedDict):
    pass

class OptionalLocation(TypedDict, total=False):
    # Unique ID for this location
    locationId: int

    # First line of address for location
    addressLine1: str

    # Second line of address for location
    addressLine2: str

    # City for location
    city: str

    locationType: LkuCode

    # Unique ID for the lookup code representing the location type
    locationTypeId: int

    # State for location
    state: str

    # State Territory name for location
    stateTerritoryName: str

    # ZIP code for location
    zip: str

    # Secondary ZIP code for location
    zip2: str

    # True if this location is located in North America
    NALocation: str

    country: LkuCode

    # Unique ID for the lookup code representing the location country
    countryId: int

    # A string representing the full location
    shortLocationString: str

class Location(RequiredLocation, OptionalLocation):
    pass
