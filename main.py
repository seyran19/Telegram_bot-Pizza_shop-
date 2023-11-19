from aiogram.utils import executor
from handlers import client, admin, others
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вышел в онлайн!')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
others.register_swear_words_filter(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
