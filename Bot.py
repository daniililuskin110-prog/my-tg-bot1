import asyncio
import logging
import os
import socket

from aiogram import Bot, Dispatcher, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = "http://USER:PASS@HOST:PORT"
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Напиши мне что-нибудь, и я повторю."
    )


@dp.message(F.text)
async def echo_text(message: Message):
    await message.answer(message.text)


async def main():
    if not TOKEN:
        raise ValueError("Не найден BOT_TOKEN в файле .env")

    session = AiohttpSession(proxy=PROXY_URL)
    session._connector_init["family"] = socket.AF_INET

    bot = Bot(token=TOKEN, session=session)
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())