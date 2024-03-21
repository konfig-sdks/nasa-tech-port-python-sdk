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

from nasa_tech_port_python_sdk.pydantic.location import Location
from nasa_tech_port_python_sdk.pydantic.organization import Organization

class Contact(BaseModel):
    # Title for the contact
    title: typing.Optional[str] = Field(None, alias='title')

    # Unique ID for this contact
    contact_id: typing.Optional[int] = Field(None, alias='contactId')

    # Display order
    display_order: typing.Optional[int] = Field(None, alias='displayOrder')

    # Fax number for the contact
    fax: typing.Optional[str] = Field(None, alias='fax')

    # First name for the contact
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # Last name for the contact
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # Full name for the contact, first middle initial last
    full_name: typing.Optional[str] = Field(None, alias='fullName')

    # Full name for the contact but inverted, last first middle initial
    full_name_inverted: typing.Optional[str] = Field(None, alias='fullNameInverted')

    location: typing.Optional[Location] = Field(None, alias='location')

    # Unique ID representing the contacts location
    location_id: typing.Optional[int] = Field(None, alias='locationId')

    # Middle initial for the contact
    middle_initial: typing.Optional[str] = Field(None, alias='middleInitial')

    organization: typing.Optional[Organization] = Field(None, alias='organization')

    # Prefix for the contact
    prefix: typing.Optional[str] = Field(None, alias='prefix')

    # Primary email for the contact
    primary_email: typing.Optional[str] = Field(None, alias='primaryEmail')

    # Secondary email for the contact
    secondary_email: typing.Optional[str] = Field(None, alias='secondaryEmail')

    # Suffix for the contact
    suffix: typing.Optional[str] = Field(None, alias='suffix')

    # Extension for contacts work phone number
    work_phone_extension: typing.Optional[str] = Field(None, alias='workPhoneExtension')

    # Phone number for the contact
    work_phone: typing.Optional[str] = Field(None, alias='workPhone')

    # 1 if the contact is signed up to receive TechPort emails
    receive_email: typing.Optional[int] = Field(None, alias='receiveEmail')

    # True if the contacts email is available to be shown to the public
    is_public_email: typing.Optional[bool] = Field(None, alias='isPublicEmail')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
