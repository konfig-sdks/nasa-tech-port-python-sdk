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

from nasa_tech_port_python_sdk.model.organization_get_information_response import OrganizationGetInformationResponse as OrganizationGetInformationResponseSchema

from nasa_tech_port_python_sdk.type.organization_get_information_response import OrganizationGetInformationResponse

from ...api_client import Dictionary
from nasa_tech_port_python_sdk.pydantic.organization_get_information_response import OrganizationGetInformationResponse as OrganizationGetInformationResponsePydantic

from . import path

# Path params
OrganizationIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'organizationId': typing.Union[OrganizationIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_organization_id = api_client.PathParameter(
    name="organizationId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrganizationIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = OrganizationGetInformationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OrganizationGetInformationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OrganizationGetInformationResponse


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

    def _get_information_mapped_args(
        self,
        organization_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if organization_id is not None:
            _path_params["organizationId"] = organization_id
        args.path = _path_params
        return args

    async def _aget_information_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_organization_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/api/organizations/{organizationId}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_information_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_organization_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/api/organizations/{organizationId}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetInformationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_information(
        self,
        organization_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_information_mapped_args(
            organization_id=organization_id,
        )
        return await self._aget_information_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_information(
        self,
        organization_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_information_mapped_args(
            organization_id=organization_id,
        )
        return self._get_information_oapg(
            path_params=args.path,
        )

class GetInformation(BaseApi):

    async def aget_information(
        self,
        organization_id: int,
        validate: bool = False,
        **kwargs,
    ) -> OrganizationGetInformationResponsePydantic:
        raw_response = await self.raw.aget_information(
            organization_id=organization_id,
            **kwargs,
        )
        if validate:
            return OrganizationGetInformationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrganizationGetInformationResponsePydantic, raw_response.body)
    
    
    def get_information(
        self,
        organization_id: int,
        validate: bool = False,
    ) -> OrganizationGetInformationResponsePydantic:
        raw_response = self.raw.get_information(
            organization_id=organization_id,
        )
        if validate:
            return OrganizationGetInformationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrganizationGetInformationResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        organization_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_information_mapped_args(
            organization_id=organization_id,
        )
        return await self._aget_information_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        organization_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_information_mapped_args(
            organization_id=organization_id,
        )
        return self._get_information_oapg(
            path_params=args.path,
        )

