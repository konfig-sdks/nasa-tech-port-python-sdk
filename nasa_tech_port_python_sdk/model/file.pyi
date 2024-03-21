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


class File(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Represents a file associated with a library item.
    """


    class MetaOapg:
        
        class properties:
            fileId = schemas.Int64Schema
            url = schemas.StrSchema
            fileSize = schemas.Int64Schema
            fileExtension = schemas.StrSchema
            fileName = schemas.StrSchema
            __annotations__ = {
                "fileId": fileId,
                "url": url,
                "fileSize": fileSize,
                "fileExtension": fileExtension,
                "fileName": fileName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileId"]) -> MetaOapg.properties.fileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSize"]) -> MetaOapg.properties.fileSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileExtension"]) -> MetaOapg.properties.fileExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileId", "url", "fileSize", "fileExtension", "fileName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileId"]) -> typing.Union[MetaOapg.properties.fileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSize"]) -> typing.Union[MetaOapg.properties.fileSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileExtension"]) -> typing.Union[MetaOapg.properties.fileExtension, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileId", "url", "fileSize", "fileExtension", "fileName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fileId: typing.Union[MetaOapg.properties.fileId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        fileSize: typing.Union[MetaOapg.properties.fileSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fileExtension: typing.Union[MetaOapg.properties.fileExtension, str, schemas.Unset] = schemas.unset,
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'File':
        return super().__new__(
            cls,
            *args,
            fileId=fileId,
            url=url,
            fileSize=fileSize,
            fileExtension=fileExtension,
            fileName=fileName,
            _configuration=_configuration,
            **kwargs,
        )
