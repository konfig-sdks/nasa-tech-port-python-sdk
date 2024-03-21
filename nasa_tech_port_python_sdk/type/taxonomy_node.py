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


class RequiredTaxonomyNode(TypedDict):
    pass

class OptionalTaxonomyNode(TypedDict, total=False):
    # Title of the taxonomy node
    title: str

    # Unique identifier for the taxonomy node
    taxonomyNodeId: int

    # Unique identifier for the root of this taxonomy node
    taxonomyRootId: int

    # Unique identifier for the taxonomy node/root that is the direct parent of this taxonomy node
    parentNodeId: int

    # The level of this node on the tree (0 being the root)
    level: int

    # Code of the taxonomy node
    code: str

    # Definition of the taxonomy node
    definition: str

    # Defines whether this node has children
    hasChildren: bool

    # Published URL of the taxonomy node
    publishedUrl: str

class TaxonomyNode(RequiredTaxonomyNode, OptionalTaxonomyNode):
    pass
