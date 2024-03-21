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

from nasa_tech_port_python_sdk.pydantic.tree_node import TreeNode

class Taxonomy(BaseModel):
    # Title for this taxonomy
    title: typing.Optional[str] = Field(None, alias='title')

    # Unique ID for this taxonomy
    taxonomy_root_id: typing.Optional[int] = Field(None, alias='taxonomyRootId')

    # ID for this taxonomy roots release status
    release_status_id: typing.Optional[int] = Field(None, alias='releaseStatusId')

    # Definition for this taxonomy
    definition: typing.Optional[str] = Field(None, alias='definition')

    # The last user to modify this taxonomy
    modified_by: typing.Optional[str] = Field(None, alias='modifiedBy')

    # The date this taxonomy was last modified
    modified_date: typing.Optional[date] = Field(None, alias='modifiedDate')

    children: typing.Optional[typing.List[TreeNode]] = Field(None, alias='children')

    # The release status of this taxonomy
    release_status: typing.Optional[str] = Field(None, alias='releaseStatus')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
