import inspect
from confobo.config import SEPARATOR

bindings = {}


class Command:
    def __init__(self, f, cmd, desc=None):
        self.f = f
        self.cmd = cmd
        self.desc = desc
        bindings[cmd] = self
        sig = inspect.signature(f)
        self.max_args = len(sig.parameters)
        self.min_args = len([p for p in sig.parameters.values() if p.default is inspect._empty])
        self.args = list(sig.parameters.keys())

    def info(self):
        sep = SEPARATOR
        if sep != ' ':
            sep += ' '
        args = ' [{}]'.format(sep.join(self.args)) if self.args else ''
        return '{cmd}{args}: {desc}'.format(cmd=self.cmd, args=args, desc=self.desc)

    def __str__(self):
        return '<Command \'{}\'>'.format(self.cmd)

    def __repr__(self):
        return str(self)

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)


def command(cmd, desc=None):
    def decorator(func):
        return Command(func, cmd, desc)
    return decorator


def execute_command(text):
    cmd_text, *params = text.split(' ', 1)
    args = [p.strip() for p in params[0].split(SEPARATOR)] if params else []
    if cmd_text in bindings:
        cmd = bindings[cmd_text]
    else:
        # TODO: handle this stuff somehow
        raise Exception('No such command')
    if not cmd.min_args <= len(args) <= cmd.max_args:
        # TODO: handle this too
        raise Exception('Wrong number of arguments')
    return cmd(*args)