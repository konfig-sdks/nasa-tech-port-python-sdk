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


class Contact(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Represents an individual and their details.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            contactId = schemas.Int64Schema
            displayOrder = schemas.Int64Schema
            fax = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            fullName = schemas.StrSchema
            fullNameInverted = schemas.StrSchema
        
            @staticmethod
            def location() -> typing.Type['Location']:
                return Location
            locationId = schemas.Int64Schema
            middleInitial = schemas.StrSchema
        
            @staticmethod
            def organization() -> typing.Type['Organization']:
                return Organization
            prefix = schemas.StrSchema
            primaryEmail = schemas.StrSchema
            secondaryEmail = schemas.StrSchema
            suffix = schemas.StrSchema
            workPhoneExtension = schemas.StrSchema
            workPhone = schemas.StrSchema
            receiveEmail = schemas.Int64Schema
            isPublicEmail = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "contactId": contactId,
                "displayOrder": displayOrder,
                "fax": fax,
                "firstName": firstName,
                "lastName": lastName,
                "fullName": fullName,
                "fullNameInverted": fullNameInverted,
                "location": location,
                "locationId": locationId,
                "middleInitial": middleInitial,
                "organization": organization,
                "prefix": prefix,
                "primaryEmail": primaryEmail,
                "secondaryEmail": secondaryEmail,
                "suffix": suffix,
                "workPhoneExtension": workPhoneExtension,
                "workPhone": workPhone,
                "receiveEmail": receiveEmail,
                "isPublicEmail": isPublicEmail,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayOrder"]) -> MetaOapg.properties.displayOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fax"]) -> MetaOapg.properties.fax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullName"]) -> MetaOapg.properties.fullName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullNameInverted"]) -> MetaOapg.properties.fullNameInverted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'Location': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationId"]) -> MetaOapg.properties.locationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleInitial"]) -> MetaOapg.properties.middleInitial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> 'Organization': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> MetaOapg.properties.prefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryEmail"]) -> MetaOapg.properties.primaryEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryEmail"]) -> MetaOapg.properties.secondaryEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workPhoneExtension"]) -> MetaOapg.properties.workPhoneExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workPhone"]) -> MetaOapg.properties.workPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiveEmail"]) -> MetaOapg.properties.receiveEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublicEmail"]) -> MetaOapg.properties.isPublicEmail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "contactId", "displayOrder", "fax", "firstName", "lastName", "fullName", "fullNameInverted", "location", "locationId", "middleInitial", "organization", "prefix", "primaryEmail", "secondaryEmail", "suffix", "workPhoneExtension", "workPhone", "receiveEmail", "isPublicEmail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayOrder"]) -> typing.Union[MetaOapg.properties.displayOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fax"]) -> typing.Union[MetaOapg.properties.fax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullName"]) -> typing.Union[MetaOapg.properties.fullName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullNameInverted"]) -> typing.Union[MetaOapg.properties.fullNameInverted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union['Location', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationId"]) -> typing.Union[MetaOapg.properties.locationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleInitial"]) -> typing.Union[MetaOapg.properties.middleInitial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union['Organization', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union[MetaOapg.properties.prefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryEmail"]) -> typing.Union[MetaOapg.properties.primaryEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryEmail"]) -> typing.Union[MetaOapg.properties.secondaryEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workPhoneExtension"]) -> typing.Union[MetaOapg.properties.workPhoneExtension, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workPhone"]) -> typing.Union[MetaOapg.properties.workPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiveEmail"]) -> typing.Union[MetaOapg.properties.receiveEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublicEmail"]) -> typing.Union[MetaOapg.properties.isPublicEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "contactId", "displayOrder", "fax", "firstName", "lastName", "fullName", "fullNameInverted", "location", "locationId", "middleInitial", "organization", "prefix", "primaryEmail", "secondaryEmail", "suffix", "workPhoneExtension", "workPhone", "receiveEmail", "isPublicEmail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        displayOrder: typing.Union[MetaOapg.properties.displayOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fax: typing.Union[MetaOapg.properties.fax, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        fullName: typing.Union[MetaOapg.properties.fullName, str, schemas.Unset] = schemas.unset,
        fullNameInverted: typing.Union[MetaOapg.properties.fullNameInverted, str, schemas.Unset] = schemas.unset,
        location: typing.Union['Location', schemas.Unset] = schemas.unset,
        locationId: typing.Union[MetaOapg.properties.locationId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        middleInitial: typing.Union[MetaOapg.properties.middleInitial, str, schemas.Unset] = schemas.unset,
        organization: typing.Union['Organization', schemas.Unset] = schemas.unset,
        prefix: typing.Union[MetaOapg.properties.prefix, str, schemas.Unset] = schemas.unset,
        primaryEmail: typing.Union[MetaOapg.properties.primaryEmail, str, schemas.Unset] = schemas.unset,
        secondaryEmail: typing.Union[MetaOapg.properties.secondaryEmail, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        workPhoneExtension: typing.Union[MetaOapg.properties.workPhoneExtension, str, schemas.Unset] = schemas.unset,
        workPhone: typing.Union[MetaOapg.properties.workPhone, str, schemas.Unset] = schemas.unset,
        receiveEmail: typing.Union[MetaOapg.properties.receiveEmail, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isPublicEmail: typing.Union[MetaOapg.properties.isPublicEmail, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contact':
        return super().__new__(
            cls,
            *args,
            title=title,
            contactId=contactId,
            displayOrder=displayOrder,
            fax=fax,
            firstName=firstName,
            lastName=lastName,
            fullName=fullName,
            fullNameInverted=fullNameInverted,
            location=location,
            locationId=locationId,
            middleInitial=middleInitial,
            organization=organization,
            prefix=prefix,
            primaryEmail=primaryEmail,
            secondaryEmail=secondaryEmail,
            suffix=suffix,
            workPhoneExtension=workPhoneExtension,
            workPhone=workPhone,
            receiveEmail=receiveEmail,
            isPublicEmail=isPublicEmail,
            _configuration=_configuration,
            **kwargs,
        )

from nasa_tech_port_python_sdk.model.location import Location
from nasa_tech_port_python_sdk.model.organization import Organization
