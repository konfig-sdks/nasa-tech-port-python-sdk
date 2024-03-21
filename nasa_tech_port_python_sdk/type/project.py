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

from nasa_tech_port_python_sdk.type.contact import Contact
from nasa_tech_port_python_sdk.type.library_item import LibraryItem
from nasa_tech_port_python_sdk.type.lku_code import LkuCode
from nasa_tech_port_python_sdk.type.location import Location
from nasa_tech_port_python_sdk.type.organization import Organization
from nasa_tech_port_python_sdk.type.taxonomy_node import TaxonomyNode

class RequiredProject(TypedDict):
    pass

class OptionalProject(TypedDict, total=False):
    # Title of the project.
    title: str

    # A detailed description of the project.
    description: str

    # Unique identifier for the project.
    projectId: int

    # ISO 8601 full-date in the format YYYY-MM-DD describing the last time this project was updated.
    lastUpdated: date

    # Abbreviated name of the project.
    acronym: str

    # Indicates whether the project is currently active, completed, or canceled.
    statusDescription: str

    # Describes the benefits offered to NASA funded and planned missions, unfunded or planned missions, commercial space industry, and to the nation.
    benefits: str

    # The month and year the project was authorized to proceed.
    startDateString: str

    # The month and year the project is expected to complete its work.
    endDateString: str

    # The technology maturity (technology readiness level) of the project at its beginning.
    startTrl: int

    # The current technology maturity (technology readiness level) of the project.
    currentTrl: int

    # The estimated technology maturity (technology readiness level) of the project at its end.
    endTrl: int

    # List of primary taxonomy nodes (from the NASA Technology Roadmap) associated with the project.
    primaryTaxonomyNodes: typing.List[TaxonomyNode]

    # List of additional and cross-cutting taxonomy nodes associated with the project.
    additionalTaxonomyNodes: typing.List[TaxonomyNode]

    # List of the NASA destinations the technology on this project helps achieve.
    destinations: typing.List[LkuCode]

    program: Program

    responsibleMd: Program

    leadOrganization: Organization

    # The supporting organizations for this project that are conducting work on the project.
    supportingOrganizations: typing.List[Organization]

    # Other government agencies, NASA Mission Directoratres, universities, or commercial entities performing contributing resources to this project.
    coFundingPartners: typing.List[Organization]

    # States and territories with people performing work on this project.
    statesWithWork: typing.List[Location]

    # Names of the Program Directors responsible for the management of this project.
    programDirectors: typing.List[Contact]

    # Names of the Program Managers responsible for the management of this project.
    programManagers: typing.List[Contact]

    # Names of the Project Managers responsible for the management of this project.
    projectManagers: typing.List[Contact]

    # Names of the Principal Investigators who are the lead scientists or engineers for this project.
    principalInvestigators: typing.List[Contact]

    # Names of the additional investigators who are scientists or engineers for this project.
    coInvestigators: typing.List[Contact]

    # The URL for the associated website.
    website: str

    # List of library items in the project library.
    libraryItems: typing.List[LibraryItem]

    # List of STI DAAs in the project library.
    stiDaas: typing.List[LibraryItem]

    # The project closeout summary excerpt.
    closeoutSummary: str

    # List of document files or links to the project final report closeout documentation.
    closeoutDocuments: typing.List[LibraryItem]

    primaryImage: LibraryItem

    # The number of views for the project.
    viewCount: int

class Project(RequiredProject, OptionalProject):
    pass
