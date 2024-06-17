from typing import Any
from dataclasses import asdict, dataclass

from .issue import IssueEntity


@dataclass
class ProjectEntity:
    """
    Project Entity according to Youtrack docs.

    See more info here:
    - https://www.jetbrains.com/help/youtrack/devportal/resource-api-admin-projects.html#e7a311ac

    """

    shortName: str | None = None
    name: str | None = None
    id: str | None = None
    archived: bool | None = None
    createdBy: Any | None = None  # TODO: change with User
    # customFields: list[Any] | None = None  # TODO change with list[ProjectCustomField]
    description: str | None = None
    fromEmail: str | None = None
    iconUrl: str | None = None
    # issues: list[IssueEntity] | None = None  # TODO change with list[Issue]
    leader: Any | None = None  # TODO change with User
    replyToEmail: str | None = None
    team: Any | None = None  # TODO change with list[User]
    template: bool | None = None

    dict = asdict

    @property
    def fields(self) -> list[str]:
        # TODO: fields like issues or customFields are special
        # for issues we need -> issues(idReadable)
        # for customFields we need -> customFields(field(name))
        # leader and team also
        return [field for field in self.__annotations__]
