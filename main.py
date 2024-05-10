import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, ErrorEvent

from config import Config

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello! Tap /get_exchange_rate')


@dp.message(Command("get_exchange_rate"))
async def get_exchange_rate(message: Message):
    excel_file = FSInputFile('exchange_rates.xlsx')
    await message.answer_document(excel_file)


@dp.error()
async def error_handler(event: ErrorEvent):
    logging.critical("Critical error caused by %s", event.exception, exc_info=True)
    await event.update.message.answer("Error, please try again /start")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
