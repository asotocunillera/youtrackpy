from youtrackpy.client import Client


from dataclasses import dataclass

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
    "issues",
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
    id: str | None = None
    archived: bool | None = None
    # createdBy: User | None = None
    # customFields: ProjectCustomField | None = None
    description: str | None = None
    fromEmail: str | None = None
    iconUrl: str | None = None
    # issues: list[Issue] | None = None
    # leader: User | None = None
    replyToEmail: str | None = None
    startingNumber: int | None = None
    # team: list[User] | None = None
    template: bool | None = None

    def __repr__(self) -> str:
        if self.name is None:
            return f"Project({self._client!r},shortName={self.shortName!r})"

        return (
            f"Project({self._client!r},name={self.name!r},shortName={self.shortName!r})"
        )
