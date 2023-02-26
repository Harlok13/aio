from aiogram import types
from aiogram.types import InputFile
from aiogram.utils.exceptions import BadRequest

from julia.dispatcher import *

# хардкод вариант
BOOKS = {'sql': {'id_book': 91, 'remote_book': 'handlers/sql.pdf'},
         'fauler': {'id_book': 93, 'remote_book': 'handlers/fauler.pdf'}}
ERROR_FIND_BOOK = 'Ой, такой книги тут нет:('

MY_CHAT_ID = -1001835718066
MY_ID = 5485747686


# реализовать бд с помощью redis. сохранять словарь с id чата, сообщения, чтобы потом по ним искать книгу
async def callback_book_info(callback: types.CallbackQuery):
    logger = logging.getLogger(__name__)
    logger.info(callback.data)
    call = await redis.hget(callback.message.chat.id, callback.data)

    try:
        await bot.send_message(callback.message.chat.id,
                               text=f'Вот Ваша книга',
                               reply_to_message_id=int(call))
    except Exception as exc:
        logger.info(exc)
        await bot.send_message(callback.message.chat.id,
                               ERROR_FIND_BOOK + '\nСейчас я поищу ее у себя')
        await bot.send_document(callback.message.chat.id,
                                InputFile(BOOKS.get(callback.data).get('remote_book')))
        await redis.hset(callback.message.chat.id, callback.data, callback.message.message_id)
        await callback.message.answer('Вот, нашел для тебя!')


def register_callback_cmd(dp: Dispatcher):
    dp.register_callback_query_handler(callback_book_info)
