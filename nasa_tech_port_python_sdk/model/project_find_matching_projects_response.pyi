# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nasa_tech_port_python_sdk import schemas  # noqa: F401


class ProjectFindMatchingProjectsResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of projects that match the criteria.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ProjectFindMatchingProjectsResponseItem']:
            return ProjectFindMatchingProjectsResponseItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ProjectFindMatchingProjectsResponseItem'], typing.List['ProjectFindMatchingProjectsResponseItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProjectFindMatchingProjectsResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ProjectFindMatchingProjectsResponseItem':
        return super().__getitem__(i)

from nasa_tech_port_python_sdk.model.project_find_matching_projects_response_item import ProjectFindMatchingProjectsResponseItem
