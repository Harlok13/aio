from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
