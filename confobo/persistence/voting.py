from confobo.models.event import Event
from confobo.models.user import User


def save_vote(user: User, choice: int, event: Event) -> bool:
    return True
