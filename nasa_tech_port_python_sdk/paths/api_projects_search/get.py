# coding: utf-8

"""
    TechPort

    TechPort RESTful API

    The version of the OpenAPI document: 3.13.2
    Contact: hq-techport@mail.nasa.gov
    Created by: https://techport.nasa.gov
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from nasa_tech_port_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from nasa_tech_port_python_sdk.api_response import AsyncGeneratorResponse
from nasa_tech_port_python_sdk import api_client, exceptions
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

from nasa_tech_port_python_sdk.model.project_find_matching_projects_response import ProjectFindMatchingProjectsResponse as ProjectFindMatchingProjectsResponseSchema

from nasa_tech_port_python_sdk.type.project_find_matching_projects_response import ProjectFindMatchingProjectsResponse

from ...api_client import Dictionary
from nasa_tech_port_python_sdk.pydantic.project_find_matching_projects_response import ProjectFindMatchingProjectsResponse as ProjectFindMatchingProjectsResponsePydantic

from . import path

# Query params
ProjectIdSchema = schemas.Int64Schema
SearchQuerySchema = schemas.StrSchema
MissionDirectorateSchema = schemas.StrSchema
ProgramSchema = schemas.StrSchema
TitleSearchSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'projectId': typing.Union[ProjectIdSchema, decimal.Decimal, int, ],
        'searchQuery': typing.Union[SearchQuerySchema, str, ],
        'missionDirectorate': typing.Union[MissionDirectorateSchema, str, ],
        'program': typing.Union[ProgramSchema, str, ],
        'titleSearch': typing.Union[TitleSearchSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_project_id = api_client.QueryParameter(
    name="projectId",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectIdSchema,
    explode=True,
)
request_query_search_query = api_client.QueryParameter(
    name="searchQuery",
    style=api_client.ParameterStyle.FORM,
    schema=SearchQuerySchema,
    explode=True,
)
request_query_mission_directorate = api_client.QueryParameter(
    name="missionDirectorate",
    style=api_client.ParameterStyle.FORM,
    schema=MissionDirectorateSchema,
    explode=True,
)
request_query_program = api_client.QueryParameter(
    name="program",
    style=api_client.ParameterStyle.FORM,
    schema=ProgramSchema,
    explode=True,
)
request_query_title_search = api_client.QueryParameter(
    name="titleSearch",
    style=api_client.ParameterStyle.FORM,
    schema=TitleSearchSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ProjectFindMatchingProjectsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProjectFindMatchingProjectsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProjectFindMatchingProjectsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _find_matching_projects_mapped_args(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if project_id is not None:
            _query_params["projectId"] = project_id
        if search_query is not None:
            _query_params["searchQuery"] = search_query
        if mission_directorate is not None:
            _query_params["missionDirectorate"] = mission_directorate
        if program is not None:
            _query_params["program"] = program
        if title_search is not None:
            _query_params["titleSearch"] = title_search
        args.query = _query_params
        return args

    async def _afind_matching_projects_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_id,
            request_query_search_query,
            request_query_mission_directorate,
            request_query_program,
            request_query_title_search,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/projects/search',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _find_matching_projects_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_id,
            request_query_search_query,
            request_query_mission_directorate,
            request_query_program,
            request_query_title_search,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/projects/search',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class FindMatchingProjectsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_matching_projects(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_matching_projects_mapped_args(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
        )
        return await self._afind_matching_projects_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def find_matching_projects(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_matching_projects_mapped_args(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
        )
        return self._find_matching_projects_oapg(
            query_params=args.query,
        )

class FindMatchingProjects(BaseApi):

    async def afind_matching_projects(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectFindMatchingProjectsResponsePydantic:
        raw_response = await self.raw.afind_matching_projects(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
            **kwargs,
        )
        if validate:
            return RootModel[ProjectFindMatchingProjectsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ProjectFindMatchingProjectsResponsePydantic, raw_response.body)
    
    
    def find_matching_projects(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ProjectFindMatchingProjectsResponsePydantic:
        raw_response = self.raw.find_matching_projects(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
        )
        if validate:
            return RootModel[ProjectFindMatchingProjectsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ProjectFindMatchingProjectsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_matching_projects_mapped_args(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
        )
        return await self._afind_matching_projects_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        project_id: typing.Optional[int] = None,
        search_query: typing.Optional[str] = None,
        mission_directorate: typing.Optional[str] = None,
        program: typing.Optional[str] = None,
        title_search: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_matching_projects_mapped_args(
            project_id=project_id,
            search_query=search_query,
            mission_directorate=mission_directorate,
            program=program,
            title_search=title_search,
        )
        return self._find_matching_projects_oapg(
            query_params=args.query,
        )

