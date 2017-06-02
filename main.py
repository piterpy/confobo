import time
from confobo import loop
from confobo.command import command, bindings


@command('/start', desc='Provides initial info about the bot')
def start():
    return 'Info about the bot'


@command('/stop', desc='Unsubscribes you from everything')
def stop():
    return 'You have been unsubscribed'


@command('/schedule', desc='Returns schedule for a given day')
def get_schedule(day):
    return 'Schedule for {}'.format(day)


@command('/vote', desc='Voting for an event')
def vote(stream_id, n):
    return 'Voting {} for {}'.format(n, stream_id)


@command('/helpdesk', desc='Contact helpdesk')
def send_to_helpdesk(msg):
    return 'Sending "{}" to helpdesk'.format(msg)


@command('/help', desc='Lists all available commands')
def help_me():
    t = ''
    for c in bindings.values():
        t += c.info() + '\n'
    return t


if __name__ == '__main__':
    loop.run_as_thread()

    while True:
        time.sleep(1)
