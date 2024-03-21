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

from nasa_tech_port_python_sdk.type.tree_node import TreeNode

class RequiredTaxonomy(TypedDict):
    pass

class OptionalTaxonomy(TypedDict, total=False):
    # Title for this taxonomy
    title: str

    # Unique ID for this taxonomy
    taxonomyRootId: int

    # ID for this taxonomy roots release status
    releaseStatusId: int

    # Definition for this taxonomy
    definition: str

    # The last user to modify this taxonomy
    modifiedBy: str

    # The date this taxonomy was last modified
    modifiedDate: date

    children: typing.List[TreeNode]

    # The release status of this taxonomy
    releaseStatus: str

class Taxonomy(RequiredTaxonomy, OptionalTaxonomy):
    pass
