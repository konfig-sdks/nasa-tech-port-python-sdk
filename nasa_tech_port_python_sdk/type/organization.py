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
from nasa_tech_port_python_sdk.type.location import Location
from nasa_tech_port_python_sdk.type.organization_msi_data import OrganizationMsiData
from nasa_tech_port_python_sdk.type.organization_set_aside_data import OrganizationSetAsideData

class RequiredOrganization(TypedDict):
    pass

class OptionalOrganization(TypedDict, total=False):
    # Unique ID for this organization
    organizationId: int

    # The acronym of the organization
    acronym: str

    # Fax number of the organization
    fax: str

    # True if the organization is an active organization
    isActive: bool

    location: Location

    # Unique ID representing the organizations location
    locationId: int

    # The name of the organization
    organizationName: str

    organizationType: LkuCode

    # Unique ID for the lookup code representing the organization type
    organizationTypeId: int

    # Unique ID for the parent organization
    parentOrganizationId: int

    # The phone number for the organization
    phone: str

    # Unique ID for the replacement organization
    replacementOrganizationId: int

    # The URL for the organization
    url: str

    # True if the organization is in North America
    NAOrganization: bool

    # True if the organization is external to NASA
    external: bool

    # Amount of links this organization has
    linkCount: int

    # Unique identifier assigned to U.S. academic institutions by MUREP.
    murepUnitId: int

    # The employer identification number (EIN) of the entity.
    ein: str

    # The unique entity identifier (UEI) of the entity.
    uei: str

    # The DUNS number assigned to the organization.
    dunsNumber: str

    msiData: OrganizationMsiData

    setAsideData: OrganizationSetAsideData

class Organization(RequiredOrganization, OptionalOrganization):
    pass
