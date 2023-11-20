from aiogram.utils import executor

from Logger import my_log
from create_bot import dp
from data_base import sqlite_db
from handlers import client, admin, others


async def on_startup(_):
    my_log.info('Бот вышел в онлайн!')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
others.register_swear_words_filter(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
