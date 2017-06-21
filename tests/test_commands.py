import pytest
from confobo.config import SEPARATOR
from confobo.command import command, execute_command, pass_user_data
from confobo.command.errors import WrongArgsNumberError, NoSuchCommandError

msg_example = {'message_id': 1,
               'from': {'id': 0, 'first_name': 'John', 'last_name': 'Doe',
                        'username': 'johndoe', 'language_code': 'en'},
               'chat': {'id': 0, 'first_name': 'John', 'last_name': 'Doe',
                        'username': 'johndoe', 'type': 'private'},
               'date': 1497567785, 'text': '',
               'entities': [{'type': 'bot_command', 'offset': 0, 'length': 2}]}


def make_msg(text):
    m = msg_example.copy()
    m['text'] = text
    return m


def test_basic():

    @command('/cmd', desc='Description')
    def f_simple(one, two):
        return 'Reply'

    assert f_simple.info == '/cmd [one, two]: Description'

    m_good = make_msg('/cmd one{}two'.format(SEPARATOR))
    m_bad_args = make_msg('/cmd')
    m_bad_command = make_msg('/bad')

    assert execute_command(m_good) == 'Reply'
    with pytest.raises(WrongArgsNumberError):
        execute_command(m_bad_args)
    with pytest.raises(NoSuchCommandError):
        execute_command(m_bad_command)


def test_passing_user_data():

    @pass_user_data
    @command('/whoami', desc='This should take user data')
    def f_with_user_data(user_data):
        assert user_data == msg_example.get('from')
        return user_data.get('username')

    @command('/whatever', desc='@pass_user_data must not work for this')
    def f_no_user_data():
        return

    execute_command(make_msg('/whoami'))

    with pytest.raises(TypeError):
        pass_user_data(f_no_user_data)


