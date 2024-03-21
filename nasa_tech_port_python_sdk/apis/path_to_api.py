import typing_extensions

from nasa_tech_port_python_sdk.paths import PathValues
from nasa_tech_port_python_sdk.apis.paths.api import Api
from nasa_tech_port_python_sdk.apis.paths.api_projects import ApiProjects
from nasa_tech_port_python_sdk.apis.paths.api_projects_search import ApiProjectsSearch
from nasa_tech_port_python_sdk.apis.paths.api_projects_project_id import ApiProjectsProjectId
from nasa_tech_port_python_sdk.apis.paths.api_organizations import ApiOrganizations
from nasa_tech_port_python_sdk.apis.paths.api_organizations_types import ApiOrganizationsTypes
from nasa_tech_port_python_sdk.apis.paths.api_organizations_organization_id import ApiOrganizationsOrganizationId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API: Api,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_PROJECTS_SEARCH: ApiProjectsSearch,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_ORGANIZATIONS: ApiOrganizations,
        PathValues.API_ORGANIZATIONS_TYPES: ApiOrganizationsTypes,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID: ApiOrganizationsOrganizationId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API: Api,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_PROJECTS_SEARCH: ApiProjectsSearch,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_ORGANIZATIONS: ApiOrganizations,
        PathValues.API_ORGANIZATIONS_TYPES: ApiOrganizationsTypes,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID: ApiOrganizationsOrganizationId,
    }
)
