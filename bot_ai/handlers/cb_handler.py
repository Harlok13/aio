import logging
from typing import Dict, Callable, Awaitable

from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot_ai.keyboards.inline_keyboard import main_menu
from bot_ai.utils.user_requsts import UserRequest
from feature_test.menu_lexicon_test import MENU_LEXICON
from bot_ai.utils.user_requsts import UserRequest

logger = logging.getLogger(__name__)



async def main_menu_cb(callback: CallbackQuery, request: UserRequest) -> None:
    print(callback.data)
    logger.info(callback.data)
    action_menu: Dict[str, Callable] = {
        'cat_profile': request.get_profile_info
    }
    if callback.data in action_menu:
        info = await action_menu.get(callback.data)(callback.message.chat.id)
    else:
        info = False
    await callback.message.edit_text(
        text=MENU_LEXICON[callback.data](info),
        reply_markup=main_menu(callback.data)
    )


def register_cb_handlers(router: Router) -> None:
    router.callback_query.register(main_menu_cb, F.data.startswith('cat'))
