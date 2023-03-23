from typing import List

from aiogram import Bot
from aiogram.types import BotCommand

from bot_ai.lexicon.commands_lexicon import COMMANDS


async def set_menu(bot: Bot):
    menu_commands: List[BotCommand] = [BotCommand(
        command=command,
        description=description
    ) for command, description in COMMANDS.items()]
    await bot.set_my_commands(menu_commands)
