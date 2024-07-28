from os import getenv

from aiogram import Router, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand
from aiogram.utils.markdown import hbold

from dotenv import load_dotenv

from .routes import film_router, check_commands

load_dotenv()

root_router = Router()
root_router.include_router(film_router)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/films", description="Get list of films"),
        BotCommand(command="/create_film", description="Create film"),
        BotCommand(command="/delete_film", description="Delete film"),
        BotCommand(command="/update_film", description="Update film"),
        BotCommand(command="/find_film", description="Find film"),
        BotCommand(command="/start", description="Start Bot"),
        BotCommand(command="/help", description="Show this menu")
    ]
    await bot.set_my_commands(commands)

@root_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    await set_commands(message.bot)
    await message.answer(f"Hi : {hbold(message.from_user.full_name)}!")

@root_router.message(lambda message: message.text == '/help')
async def command_help_handler(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    help_text = (
        "All commands:\n"
        "/films - Get all films\n"
        "/create_film - Create film\n"
        "/delete_film - Delete film\n"
        "/update_film - Update film\n"
        "/find_film - Find film\n"
        "/start - Start Bot\n"
        "/help - Get all commands\n"
    )
    await message.answer(help_text)

async def main() -> None:
    TOKEN = getenv("BOT_TOKEN")
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)

    await dp.start_polling(bot)