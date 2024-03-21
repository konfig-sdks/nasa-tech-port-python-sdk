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

from nasa_tech_port_python_sdk.type.location import Location
from nasa_tech_port_python_sdk.type.organization import Organization

class RequiredContact(TypedDict):
    pass

class OptionalContact(TypedDict, total=False):
    # Title for the contact
    title: str

    # Unique ID for this contact
    contactId: int

    # Display order
    displayOrder: int

    # Fax number for the contact
    fax: str

    # First name for the contact
    firstName: str

    # Last name for the contact
    lastName: str

    # Full name for the contact, first middle initial last
    fullName: str

    # Full name for the contact but inverted, last first middle initial
    fullNameInverted: str

    location: Location

    # Unique ID representing the contacts location
    locationId: int

    # Middle initial for the contact
    middleInitial: str

    organization: Organization

    # Prefix for the contact
    prefix: str

    # Primary email for the contact
    primaryEmail: str

    # Secondary email for the contact
    secondaryEmail: str

    # Suffix for the contact
    suffix: str

    # Extension for contacts work phone number
    workPhoneExtension: str

    # Phone number for the contact
    workPhone: str

    # 1 if the contact is signed up to receive TechPort emails
    receiveEmail: int

    # True if the contacts email is available to be shown to the public
    isPublicEmail: bool

class Contact(RequiredContact, OptionalContact):
    pass
