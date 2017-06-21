import time
from confobo import loop
from confobo.command import command, bindings, pass_user_data
from confobo.controllers.voting import vote, BadVoteValueError
from confobo.controllers.schedule import get_schedule, NoSuchDayError
from confobo.controllers.subscriptions import unsubscribe_user
from confobo.models.user import User
from confobo.models.event import Event


@command('/start', desc='Provides initial info about the bot')
def start():
    return 'Info about the bot'


@pass_user_data
@command('/stop', desc='Unsubscribe from all news')
def stop(user_data):
    if unsubscribe_user(user_data.get('id')):
        return 'You have been unsubscribed.'


@command('/schedule', desc='Returns schedule for a given day')
def view_schedule(day):
    try:
        return get_schedule(day)
    except NoSuchDayError as e:
        return str(e)


@pass_user_data
@command('/vote', desc='Voting for an event')
def do_vote(stream_id, rate, user_data):
    user = User(user_data.get('id'))
    event = Event(stream_id)

    try:
        rate = int(rate)
    except ValueError:
        return 'Error: `rate` should be an integer.'

    try:
        vote(user, rate, event)
        return 'You voted {} for {}'.format(rate, stream_id)
    except BadVoteValueError as e:
        return str(e)


@command('/helpdesk', desc='Contact helpdesk')
def send_to_helpdesk(msg):
    return 'Sending `{}` to helpdesk'.format(msg)


@command('/help', desc='Lists all available commands')
def help_me():
    m = map(lambda x: x.info, bindings.values())
    return '\n'.join(m)


if __name__ == '__main__':
    loop.run_as_thread()

    while True:
        time.sleep(1)
