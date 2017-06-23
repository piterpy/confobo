from .model import Command


class NoSuchCommandError(Exception):

    message = 'Sorry, didn\'t get that. Command \'{cmd_text}\' is not something I know of.' \
                              ' Use /help to list available commands.'

    def __init__(self, cmd_text: str):
        self.cmd_text = cmd_text

    def __str__(self):
        return self.message.format(cmd_text=self.cmd_text)

    def __repr__(self):
        return str(self)


class WrongArgsNumberError(Exception):

    message = 'Sorry, you passed a wrong number of arguments to {cmd}. See /help for reference.'

    def __init__(self, cmd: Command, n: int):
        self.cmd = cmd
        self.n = n

    def __str__(self):
        return self.message.format(n=self.n, cmd=self.cmd.text)

    def __repr__(self):
        return str(self)
