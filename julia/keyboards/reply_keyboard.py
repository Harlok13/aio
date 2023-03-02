from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

MENU_BOARD = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text='/info')],

    ]
)
# [KeyboardButton(text='/cat')],
# [KeyboardButton(text='/gif')]
