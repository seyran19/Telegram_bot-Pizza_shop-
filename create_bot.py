from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage # хранить данные в оперативной памяти

storage = MemoryStorage()

bot = Bot('6756296533:AAHDzJLii2gmt-Vm1NzFuDjerOS4l15a_7o')
dp = Dispatcher(bot, storage=storage)