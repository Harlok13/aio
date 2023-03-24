from typing import Tuple

import openai
from aiogram.types import Message
from openai.openai_object import OpenAIObject


def standard_bot_model(message: Message) -> OpenAIObject:
    response: OpenAIObject = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=1,
        max_tokens=3500,
    )
    return response


def artist_bot_model():
    ...


def coder_bot_model():
    ...


def companion_bot_model(message: Message) -> Tuple[OpenAIObject, str]:
    response: OpenAIObject = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{message.text}"}],
    )
    msg: str = response.choices[0].message.content
    return response, msg


def translator_bot_model():
    ...
