import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from aiogram.filters.state import State, StatesGroup
from aiogram.filters.command import Command

from constants import SEARCH_MODE_IN_PROGRESS, GREETING_TEXT

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


class Form(StatesGroup):
    waiting_for_username = State()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(GREETING_TEXT)


@dp.message(Command('search'))
async def tg_name(message: types.Message):
    await message.answer(SEARCH_MODE_IN_PROGRESS)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exited')
