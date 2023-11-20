import json
import string

from aiogram import types, Dispatcher
from Logger import my_log


# @dp.message_handler()
async def swear_words_filter(message: types.Message):
    with open('swear_words.json', 'r', encoding='utf-8') as file:
        words_file = json.load(file)

    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(words_file)) != set():
        await message.reply('Маты запрещены!')
        await message.delete()
        my_log.info('Пользователь ругается матом, сообщение удалено!')


def register_swear_words_filter(dp: Dispatcher):
    dp.register_message_handler(swear_words_filter)
