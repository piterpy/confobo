from confobo.models.user import User
from confobo.persistence import subscriptions


def remove_all(user: User) -> bool:
    """
    Remove user from all subscription lists

    :param user: User object

    :return: True if the vote was saved, False otherwise
    """

    return subscriptions.remove_all(user)
