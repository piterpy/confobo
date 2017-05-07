from confobo.event import Event
from confobo.user import User


def save_vote(user: User, choice: int, event: Event) -> bool:
    return True