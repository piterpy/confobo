from .model import Command

bindings = {}


def command(text, desc=None):
    def decorator(func):
        c = Command(func, text, desc)
        bindings[text] = c
        return c
    return decorator


def pass_user_data(c: Command):
    c.needs_user_data = True

    def wrapper(*args, **kwargs):
        r = c(*args, **kwargs)
        return r

    return wrapper