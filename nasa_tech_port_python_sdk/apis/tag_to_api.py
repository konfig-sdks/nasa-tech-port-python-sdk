import typing_extensions

from nasa_tech_port_python_sdk.apis.tags import TagValues
from nasa_tech_port_python_sdk.apis.tags.project_api import ProjectApi
from nasa_tech_port_python_sdk.apis.tags.organization_api import OrganizationApi
from nasa_tech_port_python_sdk.apis.tags.resource_api import ResourceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.RESOURCE: ResourceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.RESOURCE: ResourceApi,
    }
)
