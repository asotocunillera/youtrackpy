from typing import Any, Protocol, TypedDict

from requests.structures import CaseInsensitiveDict


class Response(TypedDict):
    body: Any
    headers: CaseInsensitiveDict
    reason: str
    status: int


class Client(Protocol):

    def get(
        self,
        endpoint: str,
        query: dict[str, Any] | None = None,
        fields: list[str] | None = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Response:
        """
        GET HTTP Method

        Parameters
        ----------
        endpoint: str
            endpoint to do the http request
        query: dict[str, Any] | None (default `None`)
        fields: list[str] | None (default `None`)
        limit: int (default `0`)
        skip: int (default `0`)
        """
        ...
