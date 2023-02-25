from aiogram import types
from aiogram.utils.exceptions import BadRequest

from julia.dispatcher import *

BOOKS = {'Бьюли': 91, 'Фаулер': 93}
ERROR_FIND_BOOK = 'Ой, такой книги тут нет:('


async def callback_book_info(callback: types.CallbackQuery):
    logger = logging.getLogger(__name__)
    logger.info(callback)
    try:
        await bot.send_message(callback.message.chat.id,
                               text=f'Вот книга {callback.data}(a)',
                               reply_to_message_id=BOOKS.get(callback.data, ERROR_FIND_BOOK))
    except BadRequest:
        await callback.message.answer(ERROR_FIND_BOOK)


def register_callback_cmd(dp: Dispatcher):
    dp.register_callback_query_handler(callback_book_info)
