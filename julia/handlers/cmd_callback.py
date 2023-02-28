import aiohttp

from aiogram import types
from aiogram.filters import Command

from julia.keyboards.inline_keyboard import *

from julia.dispatcher import *

# хардкод вариант
BOOKS = {'sql': {'id_book': 91, 'remote_book': 'handlers/sql.pdf'},
         'fauler': {'id_book': 93, 'remote_book': 'handlers/fauler.pdf'}}
ERROR_FIND_BOOK = 'Ой, такой книги тут нет:('

MY_CHAT_ID = -1001835718066
MY_ID = 5485747686
CHAT_ED = -1001889081173



# реализовать бд с помощью redis. сохранять словарь с id чата, сообщения, чтобы потом по ним искать книгу
async def callback_book_info(callback: types.CallbackQuery):
    logger = logging.getLogger(__name__)
    logger.info(callback.data)
    call = await redis.get(callback.data)
    logger.info(call)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as resp:
            res: dict = await resp.json()
            print(res['file'])
    if callback.data == 'get_cat':
        await callback.message.delete()
        await bot.send_photo(callback.message.chat.id,
                             photo=res['file'],
                             reply_markup=GET_CAT)
        # await bot.edit_message_media(res['file'],
        #                              callback.message.chat.id,
        #                              message_id=callback.message.message_id
        #                              )
    else:
        try:
            await bot.edit_message_text(text=f"Вот ссылка на вашу книгу:\n{str(call).lstrip('b')}".replace("'", ""),
                                        chat_id=callback.message.chat.id,
                                        message_id=callback.message.message_id)
        except Exception as exc:
            logger.info(exc)
            print(f'error {exc}')


def register_callback_cmd(dp: Dispatcher):
    dp.callback_query.register(callback_book_info)
    dp.callback_query.register(callback_get_prev, Command(commands='get_prev'))
