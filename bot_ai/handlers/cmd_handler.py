import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot_ai.keyboards.inline_keyboard import main_menu
from bot_ai.lexicon.menu_lexicon import MENU_LEXICON

logger = logging.getLogger(__name__)


async def cmd_start(message: Message) -> None:
    await message.answer(
        '<b>📌 Используя бота вы соглашаетесь с нашими правилами (Нажмите кнопку ниже, чтобы прочитать)</b>\n',
    )
    await message.answer(
        '<b>Добро пожаловать! Напишите свой вопрос, задачу или код.</b>\n',
    )
    await message.answer(
        text=MENU_LEXICON['cat_menu'](),
        reply_markup=main_menu('cat_menu'),
    )


async def cmd_help(message: Message) -> None:
    await message.answer(
        text=MENU_LEXICON['cat_help'](),
    )


def register_cmd_handlers(router: Router) -> None:
    router.message.register(cmd_start, CommandStart())
    router.message.register(cmd_help, Command(commands='help'))
