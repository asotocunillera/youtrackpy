from dataclasses import dataclass
from typing import Any

from youtrackpy.client import Client
from youtrackpy.entities import ProjectEntity, IssueEntity

INITIAL_PROJECT_FIELDS = ["id", "name", "shortName"]
PROJECT_ENDPOINT = "admin/projects"
PROJECT_FIELDS = [
    "id",
    "archived",
    "createdBy",
    "customFields(id,bundle(values(name)),defaultValues(name),field(name),canBeEmpty,emptyFieldText,ordinal,isPublic,hasRunningJob,condition)",
    "description",
    "fromEmail",
    "iconUrl",
    "issues(idReadable)",
    "leader",
    "name",
    "replyToEmail",
    "shortName",
    "team",
    "template",
]


# TODO: create User, ProjectCustomField and Issue Models
@dataclass
class Project:
    _client: Client
    shortName: str
    name: str | None = None

    _info: ProjectEntity | None = None

    def __repr__(self) -> str:
        if self.name is None:
            return f"Project({self._client!r},shortName={self.shortName!r})"
        return (
            f"Project({self._client!r},name={self.name!r},shortName={self.shortName!r})"
        )

    @property
    def info(self) -> ProjectEntity:

        if self._info is not None:
            return self._info

        project = self._client.get(
            endpoint=f"{PROJECT_ENDPOINT}/{self.shortName}",
            fields=PROJECT_FIELDS,
            limit=0,
        )

        if project["status"] != 200:
            # TODO: if error return something different
            return ProjectEntity(shortName=self.shortName)

        project = project["body"]

        self._info = self.__update_info(project)

        return self._info

    def __update_info(self, project_info: dict[str, Any]) -> ProjectEntity:
        # TODO add rest of values
        return ProjectEntity(
            shortName=self.shortName,
            name=project_info.get("name"),
            id=project_info.get("id"),
            archived=project_info.get("archived"),
            createdBy=project_info.get("createdBy"),
            customFields=project_info.get("customFields"),
            description=project_info.get("description"),
            fromEmail=project_info.get("fromEmail"),
            iconUrl=project_info.get("iconUrl"),
            issues=self._save_issues(project_info.get("issues")),
            leader=project_info.get("leader"),
            replyToEmail=project_info.get("replyToEmail"),
            startingNumber=project_info.get("startingNumber"),
            team=project_info.get("team"),
            template=project_info.get("template"),
        )

    def _save_issues(self, issues: list[dict[str, Any]] | None) -> list[IssueEntity]:
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