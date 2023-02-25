import json
import random
import string

from julia.dispatcher import *
from aiogram import types


async def photo_reply(message: types.Message):
    mes = random.choice(['Как чудесно!',
                         'Ну что за милота',
                         'Красивенько 😍'])
    await message.reply(mes)


async def echo(message: types.Message):
    print(message)
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split()} \
        .intersection(set(json.load(open('cenz.json')))) != set():
        mes = ['Ну к чему этот мат, господа', 'Выбирайте выражения, товарищи', 'Попрошу без мата, милорды', 'Почему вы ругаетесь, мисье']
        await message.reply(random.choice(mes))
        return await message.delete()

    await bot.send_message(message.chat.id, message.text)


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(photo_reply, content_types=types.ContentTypes.PHOTO)
