from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOOK_CHOICE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Болье - изучаем SQL', callback_data='beaulie')],
        [InlineKeyboardButton(text='Фаулер - конкурентное программирование', callback_data='fauler')],
        [InlineKeyboardButton(text='Brian Okken - Python Testing with pytest', callback_data='okken')]
    ]
)

BOOK_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='prev_cmd')]
    ]
)

GET_CAT = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Хочу еще котиков:3', callback_data='get_cat')]
    ]
)

GET_GIF = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Больше гифок богу гифок', callback_data='get_gif')]
    ]
)
