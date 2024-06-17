from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, TYPE_CHECKING

from youtrackpy.entities import IssueEntity, ProjectEntity


if TYPE_CHECKING:
    from youtrackpy.client import YoutrackClient

PROJECT_ENDPOINT = "admin/projects"

# TODO: create User, ProjectCustomField and Issue Models
@dataclass
class Project:
    _client: YoutrackClient
    shortName: str
    name: str | None = None

    fields: list[str] =field(default_factory=lambda: ProjectEntity().fields) 

    def __repr__(self) -> str:
        if self.name is None:
            return f"Project({self._client!r},shortName={self.shortName!r})"
        return (
            f"Project({self._client!r},name={self.name!r},shortName={self.shortName!r})"
        )

    def get_info(self) -> ProjectEntity:

        project = self._client.get(
            endpoint=f"{PROJECT_ENDPOINT}/{self.shortName}",
            fields=self.fields,
            limit=0,
        )

        if project["status"] != 200:
            # TODO: if error return something different
            return ProjectEntity(shortName=self.shortName)

        project = project["body"]

        return ProjectEntity(
            shortName=self.shortName,
            name=project.get("name"),
            id=project.get("id"),
            archived=project.get("archived"),
            createdBy=project.get("createdBy"),
            # customFields=project.get("customFields"),
            description=project.get("description"),
            fromEmail=project.get("fromEmail"),
            iconUrl=project.get("iconUrl"),
            # issues=self._format_issues(project.get("issues")),
            leader=project.get("leader"),
            replyToEmail=project.get("replyToEmail"),
            team=project.get("team"),
            template=project.get("template"),
        )

    def _format_issues(self, issues: list[dict[str, Any]] | None) -> list[IssueEntity]:
        if issues is None:
            return []

        return [
            IssueEntity(
                idReadable=issue.get(
                    "idReadable", "Not found"
                ),  # TODO: idReadable always must be in issue
            )
            for issue in issues
        ]
