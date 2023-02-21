from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Инлайн клавиатура для kayf_command
ikb = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='кайф',
                           url='https://www.youtube.com/results?search_query=%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B5+%D0%BF%D0%B5%D0%BB%D1%8C%D0%BC%D0%B5%D0%BD%D0%B8')
ib2 = InlineKeyboardButton(text='КАЙФ',
                           url='https://www.youtube.com/watch?v=fueQTjD0980&ab_channel=%D0%9E%D0%BB%D1%8F%D0%91%D0%B5%D0%BB%D0%BE%D1%81%D0%BB%D1%83%D0%B4%D1%86%D0%B5%D0%B2%D0%B0')
ikb.add(ib1, ib2)


# Клавиатура для open_main_menu, start_command
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=False)  # убирает клавиатуру, после выбранного действия
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/count')
b4 = KeyboardButton('/give')
b5 = KeyboardButton('/picture')
b6 = KeyboardButton('/location')
b7 = KeyboardButton('/❤️')
b8 = KeyboardButton('/кайф')
b9 = KeyboardButton('/botfather')
b10 = KeyboardButton('/phrase')
b11 = KeyboardButton('Random photo')
kb.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7).insert(b8).add(b9).insert(b10)
kb.add(b11)

# клавиатура для open_kb_photo
kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton('Рандом фото')
bp2 = KeyboardButton('Главное меню')
kb_photo.add(bp1, bp2)

# инлайн клавиатура для
ikb_photo = InlineKeyboardMarkup(row_width=2)
ikbp1 = InlineKeyboardButton(text='',
                             callback_data='like')
ikbp2 = InlineKeyboardButton(text='',
                             callback_data='dislike')
ikbp3 = InlineKeyboardButton(text='',
                             callback_data='next')
