import logging
from typing import Tuple, Callable

import openai

from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message
from openai.openai_object import OpenAIObject

from bot_ai.utils.bot_models import companion_bot_model
from bot_ai.utils.user_requsts import UserRequest

router = Router()
logger = logging.getLogger(__name__)

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


@router.message()
async def companion_bot_answer(message: Message, request: UserRequest, model: Callable) -> None:
    await message.reply('sec')
    check_user_tokes = await request.check_user_tokens(message.from_user.id)
    if check_user_tokes:
        response, msg = model(message)
        await request.increase_question_count(user_id=message.from_user.id)

        logger.info(message.text)
        logger.info(message.from_user.first_name)
        print(response)

        total_openai_spent_tokens: int = response.usage.total_tokens
        await request.decrease_user_tokens(
            user_id=message.from_user.id, openai_spent_tokens=total_openai_spent_tokens
        )
        await message.answer(msg)
    else:
        await message.answer('У вас недостаточно токенов')
