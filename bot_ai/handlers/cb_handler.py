import asyncio
import logging
from typing import Dict, Callable, Awaitable, Optional, List
from collections import deque

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from bot_ai.keyboards.inline_keyboard import main_menu, change_model_menu
from bot_ai.lexicon.menu_lexicon import MENU_LEXICON, get_models_info
from bot_ai.states.states import FSMOpenaiModel
from bot_ai.utils.current_state_info import get_current_state_info
from bot_ai.utils.user_requsts import UserRequest

logger: logging.Logger = logging.getLogger(__name__)

# initialize deque for set_openai_model_state_cb
_set_model_deque: deque = deque()


async def _get_exit(callback: CallbackQuery):
    if callback.data == 'cat_exit':
        return await callback.message.delete()


async def _get_cat_models(callback: CallbackQuery, current_state: str):
    if current_state and callback.data == 'cat_models':
        return await callback.message.edit_text(
            text=get_models_info(get_current_state_info(current_state)),
            reply_markup=main_menu(callback.data),
        )




# ref
async def get_main_menu_cb(callback: CallbackQuery, request: UserRequest, state: FSMContext) -> Optional[bool]:
    logger.info(callback.data)

    action_menu: Dict[str, Callable] = {
        'cat_profile': request.get_profile_info,
    }
    current_state: str = await state.get_state()

    if await _get_cat_models(callback, current_state):
        return

    await _get_cat_help(callback)

    await _get_exit(callback)

    if callback.data in action_menu:
        info = await action_menu.get(callback.data)(callback.message.chat.id)
    else:
        info = False
    await callback.message.edit_text(
        text=MENU_LEXICON[callback.data](info),
        reply_markup=main_menu(callback.data)
    )


####################### test #######################
async def set_openai_model_state_cb(callback: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    """

    """
    global _set_model_deque
    logger.info(callback.data)
    m = {
        'set_standard': FSMOpenaiModel.set_standard,
        'set_companion': FSMOpenaiModel.set_companion,
        'set_artist': FSMOpenaiModel.set_artist,
        'set_coder': FSMOpenaiModel.set_coder,
        'set_translator': FSMOpenaiModel.set_translator,
    }
    await state.set_state(m.get(callback.data))

    current_state: str = await state.get_state()

    await callback.message.edit_text(
        get_models_info(current_state.split(':')[-1]),
        reply_markup=main_menu('cat_models')
    )

    model_choice: Message = await callback.message.answer(
        text='Выбрана модель: ' + current_state,
    )
    _set_model_deque.append(model_choice.message_id)

    await asyncio.sleep(3)
    await bot.delete_message(callback.message.chat.id, _set_model_deque.popleft())


standard_settings = {
    'model': 'text-davinci-003',
    'temperature': 1.0,
    'max_tokens': 3500
}


async def _change_temperature(callback: CallbackQuery):
    global standard_settings
    param = standard_settings['temperature']
    if callback.data == 'get_temperature_plus' and param < 1.0:
        standard_settings['temperature'] = (param * 10 + 1) / 10
    elif callback.data == 'get_temperature_minus' and param > 0:
        standard_settings['temperature'] = (param * 10 - 1) / 10
    else:
        await callback.answer('Нельзя изменить')


async def _change_tokens(callback: CallbackQuery):
    global standard_settings
    param = standard_settings['max_tokens']
    if callback.data == 'get_tokens_minus' and param > 0:
        standard_settings['max_tokens'] = param - 500
    elif callback.data == 'get_tokens_plus' and param < 4000:
        standard_settings['max_tokens'] = param + 500
    else:
        await callback.answer('Нельзя изменить')


async def change_openai_model_cb(callback: CallbackQuery, state: FSMContext) -> None:
    global standard_settings
    current_state: str = await state.get_state()
    await _change_temperature(callback)
    await _change_tokens(callback)

    current_temperature: float = standard_settings['temperature']
    current_tokens: int = standard_settings['max_tokens']
    await callback.message.edit_text(
        text=MENU_LEXICON.get('change_models')(current_state, current_temperature, current_tokens),
        reply_markup=change_model_menu(callback.data)
    )


async def set_parameters_cb(callback: CallbackQuery, state: FSMContext) -> None:
    global standard_settings
    current_state: str = await state.get_state()
    await _change_temperature(callback)
    await _change_tokens(callback)

    current_temperature: float = standard_settings['temperature']
    current_tokens: int = standard_settings['max_tokens']
    await callback.message.edit_text(
        text=MENU_LEXICON.get('change_models')(current_state, current_temperature, current_tokens),
        reply_markup=change_model_menu('change_standard')
    )
######################## end test #######################

def register_cb_handlers(router: Router) -> None:
    router.callback_query.register(get_main_menu_cb, F.data.startswith('cat'))
    router.callback_query.register(set_openai_model_state_cb, F.data.startswith('set'))
    router.callback_query.register(change_openai_model_cb, F.data.startswith('change'))
    router.callback_query.register(set_parameters_cb, F.data.startswith('get'))
