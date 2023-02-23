from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инлайн клавиатура для kayf_command
ikb = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='кайф',
                           url='https://www.youtube.com/results?search_query=%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B5+%D0%BF%D0%B5%D0%BB%D1%8C%D0%BC%D0%B5%D0%BD%D0%B8')
ib2 = InlineKeyboardButton(text='КАЙФ',
                           url='https://www.youtube.com/watch?v=fueQTjD0980&ab_channel=%D0%9E%D0%BB%D1%8F%D0%91%D0%B5%D0%BB%D0%BE%D1%81%D0%BB%D1%83%D0%B4%D1%86%D0%B5%D0%B2%D0%B0')
ikb.add(ib1, ib2)

# инлайн клавиатура для send_random_photo
ikb_photo = InlineKeyboardMarkup(row_width=2)
ikbp1 = InlineKeyboardButton(text='❤',
                             callback_data='like')
ikbp2 = InlineKeyboardButton(text='👎',
                             callback_data='dislike')
ikbp3 = InlineKeyboardButton(text='Следующее фото',
                             callback_data='next')
ikb_photo.add(ikbp1, ikbp2).add(ikbp3)
