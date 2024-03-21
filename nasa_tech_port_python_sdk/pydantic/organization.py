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
from nasa_tech_port_python_sdk.pydantic.location import Location
from nasa_tech_port_python_sdk.pydantic.organization_msi_data import OrganizationMsiData
from nasa_tech_port_python_sdk.pydantic.organization_set_aside_data import OrganizationSetAsideData

class Organization(BaseModel):
    # Unique ID for this organization
    organization_id: typing.Optional[int] = Field(None, alias='organizationId')

    # The acronym of the organization
    acronym: typing.Optional[str] = Field(None, alias='acronym')

    # Fax number of the organization
    fax: typing.Optional[str] = Field(None, alias='fax')

    # True if the organization is an active organization
    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    location: typing.Optional[Location] = Field(None, alias='location')

    # Unique ID representing the organizations location
    location_id: typing.Optional[int] = Field(None, alias='locationId')

    # The name of the organization
    organization_name: typing.Optional[str] = Field(None, alias='organizationName')

    organization_type: typing.Optional[LkuCode] = Field(None, alias='organizationType')

    # Unique ID for the lookup code representing the organization type
    organization_type_id: typing.Optional[int] = Field(None, alias='organizationTypeId')

    # Unique ID for the parent organization
    parent_organization_id: typing.Optional[int] = Field(None, alias='parentOrganizationId')

    # The phone number for the organization
    phone: typing.Optional[str] = Field(None, alias='phone')

    # Unique ID for the replacement organization
    replacement_organization_id: typing.Optional[int] = Field(None, alias='replacementOrganizationId')

    # The URL for the organization
    url: typing.Optional[str] = Field(None, alias='url')

    # True if the organization is in North America
    n_a_organization: typing.Optional[bool] = Field(None, alias='NAOrganization')

    # True if the organization is external to NASA
    external: typing.Optional[bool] = Field(None, alias='external')

    # Amount of links this organization has
    link_count: typing.Optional[int] = Field(None, alias='linkCount')

    # Unique identifier assigned to U.S. academic institutions by MUREP.
    murep_unit_id: typing.Optional[int] = Field(None, alias='murepUnitId')

    # The employer identification number (EIN) of the entity.
    ein: typing.Optional[str] = Field(None, alias='ein')

    # The unique entity identifier (UEI) of the entity.
    uei: typing.Optional[str] = Field(None, alias='uei')

    # The DUNS number assigned to the organization.
    duns_number: typing.Optional[str] = Field(None, alias='dunsNumber')

    msi_data: typing.Optional[OrganizationMsiData] = Field(None, alias='msiData')

    set_aside_data: typing.Optional[OrganizationSetAsideData] = Field(None, alias='setAsideData')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
