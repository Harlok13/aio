import logging

import openai

from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def ai_answer(message: Message) -> None:
    logger = logging.getLogger(__name__)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.6,
        max_tokens=1000,
    )
    logger.info(message.text)
    logger.info(message.from_user.first_name)
    logger.info(response.choices[0].text)
    await message.answer(response.choices[0].text)
