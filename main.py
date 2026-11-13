import asyncio
import os
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()


def get_greeting():
    """Returns a greeting that depends on the time of day."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 18:
        return "Good afternoon"
    return "Good evening"


@dp.message(CommandStart())
async def start(message: Message):
    """Greets the user and asks what to study."""
    await message.answer(
        f"{get_greeting()}, {message.from_user.first_name}! 👋\n"
        "What are we studying today?"
    )


@dp.message(Command("about"))
async def about(message: Message):
    """Tells what the bot does and where the content comes from."""
    await message.answer(
        "DevQuiz Bot helps you practise programming: Python, JavaScript, React, "
        "SQL and Node.js.\n\n"
        "The questions are inspired by DevLovers (https://www.devlovers.net)."
    )


async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN is not set. Create a .env file with BOT_TOKEN=your_token")

    bot = Bot(token=token)
    print("Bot is running. Press Ctrl+C to stop.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
