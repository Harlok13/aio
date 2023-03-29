from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_ai.lexicon.ikb_lexicon import MAIN_MENU, MODEL_MENU


def main_menu(category: str) -> InlineKeyboardMarkup:
    """
    Create a keyboard for the main menu
    :param category: the category of the menu
    :return:
    """
    main_meny_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    main_menu_cat, button_settings = MAIN_MENU[category][:-1], MAIN_MENU[category][-1]
    menu_buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=text,
            callback_data=callback_data
        ) for text, callback_data in main_menu_cat
    ]
    main_meny_builder.add(*menu_buttons)
    main_meny_builder.adjust(*button_settings)
    return main_meny_builder.as_markup(resize_keyboard=True)
