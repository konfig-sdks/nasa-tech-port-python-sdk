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

from nasa_tech_port_python_sdk.pydantic.contact import Contact
from nasa_tech_port_python_sdk.pydantic.library_item import LibraryItem
from nasa_tech_port_python_sdk.pydantic.lku_code import LkuCode
from nasa_tech_port_python_sdk.pydantic.location import Location
from nasa_tech_port_python_sdk.pydantic.organization import Organization
from nasa_tech_port_python_sdk.pydantic.taxonomy_node import TaxonomyNode

class Project(BaseModel):
    # Title of the project.
    title: typing.Optional[str] = Field(None, alias='title')

    # A detailed description of the project.
    description: typing.Optional[str] = Field(None, alias='description')

    # Unique identifier for the project.
    project_id: typing.Optional[int] = Field(None, alias='projectId')

    # ISO 8601 full-date in the format YYYY-MM-DD describing the last time this project was updated.
    last_updated: typing.Optional[date] = Field(None, alias='lastUpdated')

    # Abbreviated name of the project.
    acronym: typing.Optional[str] = Field(None, alias='acronym')

    # Indicates whether the project is currently active, completed, or canceled.
    status_description: typing.Optional[str] = Field(None, alias='statusDescription')

    # Describes the benefits offered to NASA funded and planned missions, unfunded or planned missions, commercial space industry, and to the nation.
    benefits: typing.Optional[str] = Field(None, alias='benefits')

    # The month and year the project was authorized to proceed.
    start_date_string: typing.Optional[str] = Field(None, alias='startDateString')

    # The month and year the project is expected to complete its work.
    end_date_string: typing.Optional[str] = Field(None, alias='endDateString')

    # The technology maturity (technology readiness level) of the project at its beginning.
    start_trl: typing.Optional[int] = Field(None, alias='startTrl')

    # The current technology maturity (technology readiness level) of the project.
    current_trl: typing.Optional[int] = Field(None, alias='currentTrl')

    # The estimated technology maturity (technology readiness level) of the project at its end.
    end_trl: typing.Optional[int] = Field(None, alias='endTrl')

    # List of primary taxonomy nodes (from the NASA Technology Roadmap) associated with the project.
    primary_taxonomy_nodes: typing.Optional[typing.List[TaxonomyNode]] = Field(None, alias='primaryTaxonomyNodes')

    # List of additional and cross-cutting taxonomy nodes associated with the project.
    additional_taxonomy_nodes: typing.Optional[typing.List[TaxonomyNode]] = Field(None, alias='additionalTaxonomyNodes')

    # List of the NASA destinations the technology on this project helps achieve.
    destinations: typing.Optional[typing.List[LkuCode]] = Field(None, alias='destinations')

    program: typing.Optional[Program] = Field(None, alias='program')

    responsible_md: typing.Optional[Program] = Field(None, alias='responsibleMd')

    lead_organization: typing.Optional[Organization] = Field(None, alias='leadOrganization')

    # The supporting organizations for this project that are conducting work on the project.
    supporting_organizations: typing.Optional[typing.List[Organization]] = Field(None, alias='supportingOrganizations')

    # Other government agencies, NASA Mission Directoratres, universities, or commercial entities performing contributing resources to this project.
    co_funding_partners: typing.Optional[typing.List[Organization]] = Field(None, alias='coFundingPartners')

    # States and territories with people performing work on this project.
    states_with_work: typing.Optional[typing.List[Location]] = Field(None, alias='statesWithWork')

    # Names of the Program Directors responsible for the management of this project.
    program_directors: typing.Optional[typing.List[Contact]] = Field(None, alias='programDirectors')

    # Names of the Program Managers responsible for the management of this project.
    program_managers: typing.Optional[typing.List[Contact]] = Field(None, alias='programManagers')

    # Names of the Project Managers responsible for the management of this project.
    project_managers: typing.Optional[typing.List[Contact]] = Field(None, alias='projectManagers')

    # Names of the Principal Investigators who are the lead scientists or engineers for this project.
    principal_investigators: typing.Optional[typing.List[Contact]] = Field(None, alias='principalInvestigators')

    # Names of the additional investigators who are scientists or engineers for this project.
    co_investigators: typing.Optional[typing.List[Contact]] = Field(None, alias='coInvestigators')

    # The URL for the associated website.
    website: typing.Optional[str] = Field(None, alias='website')

    # List of library items in the project library.
    library_items: typing.Optional[typing.List[LibraryItem]] = Field(None, alias='libraryItems')

    # List of STI DAAs in the project library.
    sti_daas: typing.Optional[typing.List[LibraryItem]] = Field(None, alias='stiDaas')

    # The project closeout summary excerpt.
    closeout_summary: typing.Optional[str] = Field(None, alias='closeoutSummary')

    # List of document files or links to the project final report closeout documentation.
    closeout_documents: typing.Optional[typing.List[LibraryItem]] = Field(None, alias='closeoutDocuments')

    primary_image: typing.Optional[LibraryItem] = Field(None, alias='primaryImage')

    # The number of views for the project.
    view_count: typing.Optional[int] = Field(None, alias='viewCount')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
