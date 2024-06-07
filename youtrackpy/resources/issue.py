from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class IssueEntity:
    """
    Issue Entity according to Youtrack docs.
    
    See more info here:
    - https://www.jetbrains.com/help/youtrack/devportal/api-entity-Issue.html

    """
    id: str
    attachments: list[Any]  # TODO: change Any with IssueAttachments
    comments: list[Any]  # TODO change Any with IssueComments
    commentsCount: int
    created: int
    customFields: list[Any]  # TODO: change Any with IssueCustomFields
    description: str
    draftOwner: Any  # TODO: change Any with User
    externalIssue: Any  # TODO: change Any with ExternalIssue
    idReadable: str
    isDraft: bool
    links: list[Any]  # TODO: change Any with IssueLink
    numberInProject: int
    parent: Any  # TODO change Any with IssueLink
    pinnedComments: list[Any]  # TODO change Any with IssueComment
    project: Any  # TODO: change Any with Project
    reporter: Any  # TODO: change Any with User
    resolved: int
    subtasks: Any  # TODO: change Any with IssueLink
    summary: str
    tags: list[Any]  # TODO: change Any with Tag
    updated: int
    updater: Any  # TODO: change Any with User
    visibility: Any # TODO: change Any with Visibility
    voters: list[Any] #TODO: change Any with IssueVoter
    votes: int
    watchers: list[Any] # TODO: change Any with IssueWatcher
    wikifiedDescription: str

    dict = asdict
