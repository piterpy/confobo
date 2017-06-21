from .errors import NoSuchCommandError, WrongArgsNumberError
from .decorators import bindings
from confobo.config import SEPARATOR


def execute_command(msg):
    text = msg.get('text')
    cmd_text, *params = text.split(' ', 1)
    args = [p.strip() for p in params[0].split(SEPARATOR)] if params else []
    kwargs = {}
    cmd = bindings.get(cmd_text)
    if not cmd:
        raise NoSuchCommandError(cmd_text)
    if not cmd.min_args <= len(args) <= cmd.max_args:
        print(cmd.min_args, cmd.max_args)
        raise WrongArgsNumberError(cmd, len(args))
    if cmd.needs_user_data:
        kwargs['user_data'] = msg.get('from')
    return cmd(*args, **kwargs)
