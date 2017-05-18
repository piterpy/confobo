import pytest
from unittest.mock import Mock

from confobo.models.event import Event
from confobo.models.user import User
from confobo import controllers
from confobo import persistence


@pytest.fixture(scope="module")
def fixture_user():
    return User(1)


@pytest.fixture(scope="module")
def fixture_event():
    return Event(1)


def test_vote(fixture_user, fixture_event):
    persistence.save_vote = Mock(return_value=True)
    vote_acceptable = 4
    vote_unacceptable = 6

    assert controllers.voting.vote(fixture_user, vote_acceptable, fixture_event) is True
    assert controllers.voting.vote(fixture_user, vote_unacceptable, fixture_event) is False
