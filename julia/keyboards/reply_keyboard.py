from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

MENU_BOARD = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton('/info')],
        # [KeyboardButton('location', request_location=True)],
        # [KeyboardButton('contacts', request_contact=True)]
    ]
)
