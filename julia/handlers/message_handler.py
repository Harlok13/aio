import json
import logging
import random
import string

from julia.dispatcher import *
from aiogram import types


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


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(photo_reply, content_types=types.ContentTypes.PHOTO)
