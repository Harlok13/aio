import aiohttp

from aiogram import types, F
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

redis_prev = None


async def get_prev(callback: types.CallbackQuery):
    # или hset с айди пользователя?
    global redis_prev
    await redis.set('back', callback.data)
    redis_prev = await redis.get('back', callback.data)


def book_filter(callback: types.CallbackQuery):
    """Фильтр книг для redis."""
    try:
        return True if int(callback.data) else 'да что угодно'
    except ValueError:
        return False


async def callback_get_prev(callback: types.CallbackQuery):
    """Кнопка назад."""
    # prev = await redis.get('back')
    await callback.message.edit_text(text='Выберите категорию:',
                                     reply_markup=CAT_CHOICE_MENU)


async def callback_back_to_menu(callback: types.CallbackQuery):
    """Кнопка вернуться в меню."""
    await callback.message.edit_text(text='Выберите категорию:',
                                     reply_markup=CAT_CHOICE_MENU)


async def callback_python_cat_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории PYTHON."""
    logger = logging.getLogger(__name__)
    await callback.message.edit_text(text='Выберите категорию Python',
                                     reply_markup=PYTHON_CHOICE_MENU)


async def callback_db_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории БАЗЫ ДАННЫХ"""
    logger = logging.getLogger(__name__)
    await callback.message.edit_text(text='Выберите категорию баз данных',
                                     reply_markup=DB_MENU)


async def callback_nosql_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории NoSQL."""
    await callback.message.edit_text(text='Выберите книгу по NoSQL',
                                     reply_markup=NOSQL_MENU)


async def callback_sql_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории SQL."""
    await callback.message.edit_text(text='Выберите книгу по SQL',
                                     reply_markup=SQL_MENU)


async def callback_back_to_db(callback: types.CallbackQuery):
    """Кнопка возврата к категории БАЗЫ ДАННЫХ."""
    await callback.message.edit_text(text='Выберите категорию баз данных',
                                     reply_markup=DB_MENU)


async def callback_back_to_pyhon(callback: types.CallbackQuery):
    """Кнопка возврата к категории КНИГИ ПО PYTHON."""
    await callback.message.edit_text(text='Выберите категорию Python',
                                     reply_markup=PYTHON_CHOICE_MENU)


async def callback_git_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории GIT."""
    await callback.message.edit_text(text='Выберите книгу по GIT',
                                     reply_markup=GIT_MENU)


async def callback_start_book_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории КНИГИ ДЛЯ СТАРТА."""
    await callback.message.edit_text(text='Выберите книгу для начинающих',
                                     reply_markup=START_BOOKS_MENU)


async def callback_algorithms_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории АЛГОРИТМЫ."""
    await callback.message.edit_text(text='Выберите книгу по алгоритмам',
                                     reply_markup=ALGORITHMS_MENU)


async def callback_linux_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории LINUX."""
    await callback.message.edit_text(text='Выберите книгу по LINUX',
                                     reply_markup=LINUX_MENU)


async def callback_python_books_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории КНИГИ ПО PYTHON."""
    await callback.message.edit_text(text='Выберите книгу по PYTHON',
                                     reply_markup=PYTHON_MENU)


async def callback_kids_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории ДЛЯ САМЫХ МАЛЕНЬКИХ."""
    await callback.message.edit_text(text='Выберите книгу для самых начинающих',
                                     reply_markup=KIDS_MENU)


async def callback_async_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории АСИНХРОННЫЙ PYTHON."""
    await callback.message.edit_text(text='Выберите книгу по async',
                                     reply_markup=ASYNC_MENU)


async def callback_django_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории DJANGO."""
    await callback.message.edit_text(text='Выберите книгу по DJANGO',
                                     reply_markup=DJANGO_MENU)


async def callback_tests_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории ТЕСТИРОВАНИЕ."""
    await callback.message.edit_text(text='Выберите книгу по тестированию',
                                     reply_markup=TESTS_MENU)


async def callback_pandas_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории PANDAS."""
    await callback.message.edit_text(text='Выберите книгу по PANDAS',
                                     reply_markup=PANDAS_MENU)


async def callback_ml_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории НЕЙРОСЕТИ."""
    await callback.message.edit_text(text='Выберите книгу по нейросетям',
                                     reply_markup=ML_MENU)


async def callback_recommendations_info(callback: types.CallbackQuery):
    """Кнопка для выбора категории РЕКОМЕНДАЦИИ."""
    await callback.message.edit_text(text='ой, это раздел пуст:( \n давайте добавим в него что-нибудь?',
                                     reply_markup=RECOMMEND_MENU)
    # await callback.message.edit_text(text='Выберите книгу из рекомендаций',
    #                                  reply_markup=RECOMMEND_MENU)


async def callback_get_kitty(callback: types.CallbackQuery):
    logger = logging.getLogger(__name__)
    logger.info(callback.data)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as resp:
            res: dict = await resp.json()

    await callback.message.delete()
    await bot.send_photo(callback.message.chat.id,
                         photo=res['file'],
                         reply_markup=GET_CAT)


async def callback_get_book(callback: types.CallbackQuery):
    """Получить книгу из redis."""
    call = await redis.get(callback.data)
    await callback.message.edit_text(text=f'{callback.data} Ваша книга:)\n{str(call).strip("b")}'.replace("'", ''),
                                     reply_markup=BOOK_MENU)


async def callback_grandfa_reviews(callback: types.CallbackQuery):
    """Получить отзыв от дедов."""
    # call = await redis.get(callback.data)
    await callback.message.answer(text='деды явно знают больше\nждем от них ревью :)',
                                  reply_markup=TY_MENU)


async def callback_about_book(callback: types.CallbackQuery):
    """Получить описание книги."""
    # call = await redis.get(callback.data)
    await callback.message.answer(text='описание в процессе)',
                                  reply_markup=ABOUT_BOOK_MENU)


async def callback_say_ty(callback: types.CallbackQuery):
    """Сказать спасибо и удалить сообщение."""
    await callback.message.delete()


async def close_menu(callback: types.CallbackQuery):
    """Закрыть меню."""
    await callback.message.answer(text='надеюсь я смог помочь', reply_markup=MENU_BOARD)
    await callback.message.delete()


async def callback_go_to_cat(callback: types.CallbackQuery):
    """
    Назад к категориям (из ссылки на книгу).
    хардкод вариант
    """
    print(callback.message.text)
    # if callback.data == '2':
    if callback.message.text.split()[0] in ('2', ):
        await callback_nosql_info(callback)
    elif callback.message.text.split()[0] in ('11', '31', '9'):
        await callback_sql_info(callback)
    elif callback.message.text.split()[0] in ('5', ):
        await callback_git_info(callback)
    elif callback.message.text.split()[0] in ('6', '21', '22', '23'):
        await callback_start_book_info(callback)
    elif callback.message.text.split()[0] in ('10', ):
        await callback_algorithms_info(callback)
    elif callback.message.text.split()[0] in ('17', '20'):
        await callback_linux_info(callback)
    elif callback.message.text.split()[0] in ('3', '7', '16', '15', '18', '27',
                                              '28', '29', '36', '37'):
        await callback_python_books_info(callback)
    elif callback.message.text.split()[0] in ('4', ):
        await callback_kids_info(callback)
    elif callback.message.text.split()[0] in ('1', ):
        await callback_async_info(callback)
    elif callback.message.text.split()[0] in ('8', '12'):
        await callback_django_info(callback)
    elif callback.message.text.split()[0] in ('13', ):
        await callback_tests_info(callback)
    elif callback.message.text.split()[0] in ('14', ):
        await callback_pandas_info(callback)
    elif callback.message.text.split()[0] in ('32', '33', '30'):
        await callback_ml_info(callback)


def register_callback_cmd(dp: Dispatcher):
    dp.callback_query.register(callback_db_info, F.data == 'db_cat')
    dp.callback_query.register(callback_nosql_info, F.data == 'nosql_cat')
    dp.callback_query.register(callback_sql_info, F.data == 'sql_cat')
    dp.callback_query.register(callback_git_info, F.data == 'git_cat')
    dp.callback_query.register(callback_start_book_info, F.data == 'start_cat')
    dp.callback_query.register(callback_algorithms_info, F.data == 'algorithms_cat')
    dp.callback_query.register(callback_linux_info, F.data == 'linux_cat')
    dp.callback_query.register(callback_python_cat_info, F.data == 'python_cat')
    dp.callback_query.register(callback_python_books_info, F.data == 'pybook_cat')
    dp.callback_query.register(callback_kids_info, F.data == 'kids_cat')
    dp.callback_query.register(callback_async_info, F.data == 'async_cat')
    dp.callback_query.register(callback_tests_info, F.data == 'tests_cat')
    dp.callback_query.register(callback_django_info, F.data == 'django_cat')
    dp.callback_query.register(callback_pandas_info, F.data == 'pandas_cat')
    dp.callback_query.register(callback_ml_info, F.data == 'ml_cat')
    dp.callback_query.register(close_menu, F.data == 'close')

    dp.callback_query.register(callback_recommendations_info, F.data == 'recommendations_cat')

    dp.callback_query.register(callback_get_prev, F.data == GET_PREV_DATA)
    dp.callback_query.register(callback_back_to_menu, F.data == TO_MENU_DATA)

    dp.callback_query.register(callback_back_to_db, F.data == 'go_db')
    dp.callback_query.register(callback_back_to_pyhon, F.data == 'go_python')

    dp.callback_query.register(callback_grandfa_reviews, F.data == 'grandfa_cmd')
    dp.callback_query.register(callback_about_book, F.data == 'about_cmd')
    dp.callback_query.register(callback_say_ty, F.data == 'ty')
    dp.callback_query.register(callback_go_to_cat, F.data == 'go_to_cat')

    dp.callback_query.register(callback_get_kitty, F.data == 'get_kitty')

    dp.callback_query.register(callback_get_book, book_filter)  # должен быть последним
