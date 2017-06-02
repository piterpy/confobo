import telepot
from telepot.loop import MessageLoop
from .command import command, bindings, execute_command
from .secret import API_KEY

bot = telepot.Bot(API_KEY)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, execute_command(msg['text']))
        return
    raise NotImplemented()


def on_callback_query(msg):
    raise NotImplemented()


loop = MessageLoop(bot, {'chat': on_chat_message,
                         'callback_query': on_callback_query})

