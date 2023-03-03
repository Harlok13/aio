import json
import logging
import random
import string
from aiogram import Router

from aiogram import types, F

from julia.keyboards.inline_keyboard import CAT_CHOICE_MENU

r = Router()

async def animation_info(message: types.Animation):
    logger = logging.getLogger(__name__)
    logger.info(message)
    print(message)
    mes = random.choice(['Как чудесно!',
                         'Ну что за милота',
                         'Красивенько 😍'])
    # await message.reply(mes)


async def photo_reply(message: types.Message):
    logger = logging.getLogger(__name__)
    logger.info(message)
    mes = random.choice(['Как чудесно!',
                         'Ну что за милота',
                         'Красивенько 😍'])
    await message.reply(mes)


async def get_library(message: types.Message):
    await message.answer(text='Выберите категорию:',
                         reply_markup=CAT_CHOICE_MENU)
    await message.delete()


async def echo(message: types.Message):
    logger = logging.getLogger(__name__)
    logger.info(message)
    print(message)
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        mes = ['Ну к чему этот мат, господа',
               'Выбирайте выражения, товарищи',
               'Попрошу без мата, милорды',
               'Почему вы ругаетесь, мисье']
        await message.reply(random.choice(mes))
        return await message.delete()
    else:
        if message.from_user.id == 5485747686:
            await message.reply('все молчу')
        elif message.from_user.id == 384745640:
            await message.reply(random.choice(['пристально слежу за тобой',
                                               'я все вижу']))
    # await bot.send_message(message.chat.id, message.text)


def register_message_handler(r: Router):
    r.message.register(photo_reply, F.photo)
    r.message.register(get_library, F.text == 'БИБЛИОТЕКА')
    # r.message.register(animation_info, F.animation)
    # r.message.register(echo)
