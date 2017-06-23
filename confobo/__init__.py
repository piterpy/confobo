import telepot
from telepot.loop import MessageLoop
from functools import partial

from .command.handlers import on_chat_message, on_callback_query
from .secret import API_KEY

bot = telepot.Bot(API_KEY)

loop = MessageLoop(bot, {'chat': partial(on_chat_message, bot=bot),
                         'callback_query': partial(on_callback_query, bot=bot)})

