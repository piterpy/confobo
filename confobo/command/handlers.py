from telepot import glance

from .execution import execute_command
from .errors import NoSuchCommandError, WrongArgsNumberError


def on_chat_message(msg, bot):
    content_type, chat_type, chat_id = glance(msg)
    if content_type == 'text':
        try:
            reply = execute_command(msg)
        except (NoSuchCommandError, WrongArgsNumberError) as e:
            reply = str(e)
        except Exception as e:
            print(e)
            reply = 'An error happened.'
        bot.sendMessage(chat_id, reply)
        return
    raise NotImplemented()


def on_callback_query(msg, bot):
    raise NotImplemented()
