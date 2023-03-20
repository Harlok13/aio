import logging

import openai

from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

router = Router()


# @router.message(Text(contains="бот"))
# async def ai_answer(message: Message) -> None:
#     await message.reply('sec')
#     logger = logging.getLogger(__name__)
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=message.text,
#         temperature=1,
#         max_tokens=3500,
#     )
#     logger.info(message.text)
#     logger.info(message.from_user.first_name)
#     logger.info(response.choices[0].text)
#     print(response)
#     await message.answer(response.choices[0].text)


@router.message(Text(contains="бот"))
async def ai_answer(message: Message) -> None:
    await message.reply('sec')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{message.text}"}],
    )
    logger = logging.getLogger(__name__)
    logger.info(message.text)
    logger.info(message.from_user.first_name)
    await message.answer(response.choices[0].message.content)
