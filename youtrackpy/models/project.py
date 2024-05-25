from typing import Any
from youtrackpy.client import Client


class YoutrackProject:

    INITIAL_PROJECT_FIELDS = [
        "id",
        "archived",
        "createdBy",
        # TODO: create customField models to format response depending of which customField type
        "customFields(id,bundle(values(name)),defaultValues(name),field(name),project,canBeEmpty,emptyFieldText,ordinal,isPublic,hasRunningJob,condition)",
        "description",
        "fromEmail",
        "iconUrl",
        "issues",
        "leader",
        "name",
        "replyToEmail",
        "shortName",
        "team",
        "template",
    ]

    def __init__(self, client: Client, short_name: str) -> None:
        self._client = client
        self._short_name = short_name

    def __repr__(self) -> str:
        return f"YoutrackProject({self._client!r}, {self._short_name!r})"

    def get_info(self, fields: list[str] | None = None) -> dict[str, Any]:

        if fields is None:
            fields = self.INITIAL_PROJECT_FIELDS

        project = self._client.get(
            endpoint=f"admin/projects/{self._short_name}",
            fields=fields,
        )

        if project["status"] != 200:
            # raise ValueError(f"Project {self._short_name.upper()} does not exist")
            return {}

        return project["body"]
