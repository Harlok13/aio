from aiogram import types
from aiogram.utils.exceptions import BadRequest

from julia.dispatcher import *

BOOKS = {'Бьюли': 91, 'Фаулер': 93}
ERROR_FIND_BOOK = 'Ой, такой книги тут нет:('


async def callback_book_info(callback: types.CallbackQuery):
    logger = logging.getLogger(__name__)
    logger.info(callback)
    if callback.data == 'Бьюли':
        try:
            await bot.send_message(callback.message.chat.id,
                                   text='вот книга Бьюли',
                                   reply_to_message_id=BOOKS.get(callback.data, ERROR_FIND_BOOK))
            await callback.answer('')
        except BadRequest:
            await callback.message.answer(ERROR_FIND_BOOK)

    elif callback.data == 'Фаулер':
        await bot.send_message(callback.message.chat.id,
                               text='вот книга Фаулера',
                               reply_to_message_id=BOOKS.get(callback.data, ERROR_FIND_BOOK))
        await callback.answer('')


def register_callback_cmd(dp: Dispatcher):
    dp.register_callback_query_handler(callback_book_info)
