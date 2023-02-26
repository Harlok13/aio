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
    call = await redis.get(callback.data)
    try:
        await bot.edit_message_text(text=f"Вот ссылка на вашу книгу:\n{str(call).lstrip('b')}".replace("'", ""),
                                    chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id)
    except Exception as exc:
        logger.info(exc)
        print(f'error {exc}')


def register_callback_cmd(dp: Dispatcher):
    dp.register_callback_query_handler(callback_book_info)
