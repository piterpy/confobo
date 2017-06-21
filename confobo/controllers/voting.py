from confobo.models.event import Event
from confobo.models.user import User
from confobo.persistence import voting


LOWEST_VOTE = 1
HIGHEST_VOTE = 5


class BadVoteValueError(Exception):
    pass


def vote(user: User, choice: int, event: Event) -> bool:
    """
    Save user's vote for the current event

    :param user: User object
    :param choice: "stars" amount from 1 to 5
    :param event: Event object

    :return: True if the vote was saved, False otherwise
    """
    if LOWEST_VOTE <= choice <= HIGHEST_VOTE:
        return voting.save_vote(user, choice, event)
    else:
        raise BadVoteValueError('You can give from {} to {} stars, not {}'.format(LOWEST_VOTE, HIGHEST_VOTE, choice))
