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

from nasa_tech_port_python_sdk.pydantic.lku_code import LkuCode

class Location(BaseModel):
    # Unique ID for this location
    location_id: typing.Optional[int] = Field(None, alias='locationId')

    # First line of address for location
    address_line1: typing.Optional[str] = Field(None, alias='addressLine1')

    # Second line of address for location
    address_line2: typing.Optional[str] = Field(None, alias='addressLine2')

    # City for location
    city: typing.Optional[str] = Field(None, alias='city')

    location_type: typing.Optional[LkuCode] = Field(None, alias='locationType')

    # Unique ID for the lookup code representing the location type
    location_type_id: typing.Optional[int] = Field(None, alias='locationTypeId')

    # State for location
    state: typing.Optional[str] = Field(None, alias='state')

    # State Territory name for location
    state_territory_name: typing.Optional[str] = Field(None, alias='stateTerritoryName')

    # ZIP code for location
    zip: typing.Optional[str] = Field(None, alias='zip')

    # Secondary ZIP code for location
    zip2: typing.Optional[str] = Field(None, alias='zip2')

    # True if this location is located in North America
    n_a_location: typing.Optional[str] = Field(None, alias='NALocation')

    country: typing.Optional[LkuCode] = Field(None, alias='country')

    # Unique ID for the lookup code representing the location country
    country_id: typing.Optional[int] = Field(None, alias='countryId')

    # A string representing the full location
    short_location_string: typing.Optional[str] = Field(None, alias='shortLocationString')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
