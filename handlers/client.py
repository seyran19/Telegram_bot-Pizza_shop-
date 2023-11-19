from aiogram import types, Dispatcher

from create_bot import bot
from data_base.sqlite_db import sql_read
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Доброго времени суток!', reply_markup=kb_client)
        await message.delete()
    except Exception:
        await message.reply('Общение с ботом через лс, напишите ему:\nhttps://t.me/Baku_pizza_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Пн-Вс с 9:00 до 20:00')
    except Exception:
        await message.reply('Пн-Вс с 9:00 до 20:00\nЧтобы общаться с ботом напишите ему!\nhttps://t.me/Baku_pizza_bot')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Ул. Низами 19')
    except Exception:
        await message.reply('Ул. Низами 19\nЧтобы общаться с ботом напишите ему!\nhttps://t.me/Baku_pizza_bot')


# @dp.message_handler(commands=['Меню'])
async def pizza_menu(message: types.Message):
    await sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu, commands=['Меню'])
