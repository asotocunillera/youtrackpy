from typing import Any, Literal, TypedDict

import requests
from requests.structures import CaseInsensitiveDict

from youtrackpy.resources import Project, PROJECT_ENDPOINT


class Response(TypedDict):
    body: Any
    headers: CaseInsensitiveDict
    reason: str
    status: int


class YoutrackClient():

    DEFAULT_SCHEME = "https"

    def __init__(
        self,
        host: str,
        port: int,
        auth: str,
        scheme: Literal["http", "https"] | None = None,
        disable_ssl_certificate_validation: bool | None = True,
    ) -> None:
        self.__host = host
        self.__port = port
        self.__scheme = self.DEFAULT_SCHEME if scheme is None else scheme
        self._base_url = f"{self.__scheme}://{self.__host}:{self.__port}/api"
        self._headers = {
            "Authorization": auth,
            "Accept": "application/json",
            "Cache-Control": "no-cache",
        }
        self._verify = not disable_ssl_certificate_validation

        self._projects = None

    def __repr__(self) -> str:
        host = f"{self.__host}:{self.__port}"
        return f"YoutrackClient(host='{host}')"

    def __getattr__(self, name: str):
        return self.__getitem__(name)

    def __getitem__(self, name: str):
        return Project(self, name)

    def get(
        self,
        endpoint: str,
        query: dict[str, Any] | None = None,
        fields: list[str] | None = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Response:
        return self._get(endpoint, query, fields, limit, skip)

    def _get(
        self,
        endpoint: str,
        query: dict[str, Any] | None = None,
        fields: list[str] | None = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Response:

        endpoint = f"{self._base_url}/{endpoint}"
        if fields is not None:
            endpoint = f"{endpoint}?fields={','.join(fields)}"

        # TODO: add query, limit and skip variables to endpoint
        response = requests.get(endpoint, headers=self._headers, verify=self._verify)
        return {
            "body": response.json(),
            "headers": response.headers,
            "reason": response.reason,
            "status": response.status_code,
        }

    @property
    def projects(self) -> list[Project]:
        """
        Retrieve a list of projects

        Return
        ------
         - list[Project(name,shortName)]

        """
        if self._projects is not None:
            return self._projects

        INITIAL_PROJECT_FIELDS = ["name", "shortName"]

        response = self.get(endpoint=PROJECT_ENDPOINT, fields=INITIAL_PROJECT_FIELDS)

        if response["status"] != 200:
            return []

        self._projects = [
            Project(
                _client=self,
                name=project["name"],
                shortName=project["shortName"],
            )
            for project in response["body"]
        ]

        return self._projects
