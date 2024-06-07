from typing import Any
from dataclasses import asdict, dataclass


@dataclass
class ProjectEntity:
    """
    Project Entity according to Youtrack docs.

    See more info here:
    - https://www.jetbrains.com/help/youtrack/devportal/resource-api-admin-projects.html#e7a311ac

    """

    shortName: str
    name: str | None = None
    id: str | None = None
    archived: bool | None = None
    createdBy: Any | None = None  # TODO: change with User
    customFields: list[Any] | None = None  # TODO change with list[ProjectCustomField]
    description: str | None = None
    fromEmail: str | None = None
    iconUrl: str | None = None
    issues: list[Any] | None = None  # TODO change with list[Issue]
    leader: Any | None = None  # TODO change with User
    replyToEmail: str | None = None
    startingNumber: int | None = None
    team: Any | None = None  # TODO change with list[User]
    template: bool | None = None

    dict = asdict
