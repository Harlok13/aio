import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot_ai.keyboards.inline_keyboard import main_menu
from bot_ai.lexicon.menu_lexicon import MENU_LEXICON

logger = logging.getLogger(__name__)


async def main_menu_cb(callback: CallbackQuery) -> None:
    print(callback.data)
    logger.info(callback.data)
    await callback.message.edit_text(
        text=MENU_LEXICON[callback.data](),
        reply_markup=main_menu(callback.data)
    )


def register_cb_handlers(router: Router) -> None:
    router.callback_query.register(main_menu_cb, F.data.startswith('cat'))
