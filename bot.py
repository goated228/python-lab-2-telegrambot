from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN
from weather import get_weather
from playlists import sad_playlist, happy_playlist


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(
        "hello!\n"
        "let's get started\n"
    )


@dp.message_handler()
async def send_music(message: types.Message):
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


if __name__ == "__main__":
    executor.start_polling(dp)