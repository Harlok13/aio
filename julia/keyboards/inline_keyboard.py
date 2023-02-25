from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOOK_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Бьюли - изучаем SQL', callback_data='Бьюли'),
         InlineKeyboardButton('Фаулер - конкурентное программирование', callback_data='Фаулер')]
    ]
)
