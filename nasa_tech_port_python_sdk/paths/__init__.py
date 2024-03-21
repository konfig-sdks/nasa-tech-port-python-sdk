# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nasa_tech_port_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API = "/api"
    API_PROJECTS = "/api/projects"
    API_PROJECTS_SEARCH = "/api/projects/search"
    API_PROJECTS_PROJECT_ID = "/api/projects/{projectId}"
    API_ORGANIZATIONS = "/api/organizations"
    API_ORGANIZATIONS_TYPES = "/api/organizations/types"
    API_ORGANIZATIONS_ORGANIZATION_ID = "/api/organizations/{organizationId}"
