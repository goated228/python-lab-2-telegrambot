import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN
from weather import get_weather
from playlists import sad_playlist, happy_playlist

bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "hello!\n"
        "let's get started\n"
    )

@dp.message()
async def send_music(message: Message):
    city = message.text

    weather = get_weather(city)

    if weather in ["Clouds", "Rain", "Snow"]:

        songs = "\n".join(sad_playlist)

        await message.answer(
            f"weather right now: {weather}\n\n"
            f"sad playlist:\n{songs}"
        )

    else:

        songs = "\n".join(happy_playlist)

        await message.answer(
            f"weather right now: {weather}\n\n"
            f"happy playlist:\n{songs}"
        )

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())