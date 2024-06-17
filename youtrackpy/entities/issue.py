from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class IssueEntity:
    """
    Issue Entity according to Youtrack docs.

    See more info here:
    - https://www.jetbrains.com/help/youtrack/devportal/api-entity-Issue.html

    """

    idReadable: str
    id: str | None = None
    attachments: list[Any] | None = None  # TODO: change Any with IssueAttachments
    comments: list[Any] | None = None  # TODO change Any with IssueComments
    commentsCount: int | None = None
    created: int | None = None
    customFields: list[Any] | None = None  # TODO: change Any with IssueCustomFields
    description: str | None = None
    draftOwner: Any | None = None  # TODO: change Any with User
    externalIssue: Any | None = None  # TODO: change Any with ExternalIssue
    isDraft: bool | None = None
    links: list[Any] | None = None  # TODO: change Any with IssueLink
    numberInProject: int | None = None
    parent: Any | None = None  # TODO change Any with IssueLink
    pinnedComments: list[Any] | None = None  # TODO change Any with IssueComment
    project: Any | None = None  # TODO: change Any with Project
    reporter: Any | None = None  # TODO: change Any with User
    resolved: int | None = None
    subtasks: Any | None = None  # TODO: change Any with IssueLink
    summary: str | None = None
    tags: list[Any] | None = None  # TODO: change Any with Tag
    updated: int | None = None
    updater: Any | None = None  # TODO: change Any with User
    visibility: Any | None = None  # TODO: change Any with Visibility
    voters: list[Any] | None = None  # TODO: change Any with IssueVoter
    votes: int | None = None
    watchers: list[Any] | None = None  # TODO: change Any with IssueWatcher
    wikifiedDescription: str | None = None

    dict = asdict

    def __repr__(self):
        return f"IssueEntity(idReadable={self.idReadable!r})"
