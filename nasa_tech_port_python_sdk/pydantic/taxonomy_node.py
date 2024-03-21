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


class TaxonomyNode(BaseModel):
    # Title of the taxonomy node
    title: typing.Optional[str] = Field(None, alias='title')

    # Unique identifier for the taxonomy node
    taxonomy_node_id: typing.Optional[int] = Field(None, alias='taxonomyNodeId')

    # Unique identifier for the root of this taxonomy node
    taxonomy_root_id: typing.Optional[int] = Field(None, alias='taxonomyRootId')

    # Unique identifier for the taxonomy node/root that is the direct parent of this taxonomy node
    parent_node_id: typing.Optional[int] = Field(None, alias='parentNodeId')

    # The level of this node on the tree (0 being the root)
    level: typing.Optional[int] = Field(None, alias='level')

    # Code of the taxonomy node
    code: typing.Optional[str] = Field(None, alias='code')

    # Definition of the taxonomy node
    definition: typing.Optional[str] = Field(None, alias='definition')

    # Defines whether this node has children
    has_children: typing.Optional[bool] = Field(None, alias='hasChildren')

    # Published URL of the taxonomy node
    published_url: typing.Optional[str] = Field(None, alias='publishedUrl')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
