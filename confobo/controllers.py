from confobo.event import Event
from confobo.user import User
from confobo import persistence


LOWEST_VOTE = 1
HIGHEST_VOTE = 5


def vote(user: User, choice: int, event: Event) -> bool:
    """
    Save user's vote for the current event

    :param user: User object
    :param choice: "stars" amount from 1 to 5
    :param event: Event object

    :return: True if the vote was saved, False otherwise
    """
    if LOWEST_VOTE <= choice <= HIGHEST_VOTE:
        return persistence.save_vote(user, choice, event)
    else:
        return False
