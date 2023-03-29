from collections import namedtuple
from typing import NamedTuple, Type, Dict

from aiogram.types import Message

TokenPay: Type['TokenPay'] = namedtuple('TokenPay', ['title', 'description', 'payload'])

TokenLabel: Type['TokenLabel'] = namedtuple('TokenLabel', ['label', 'amount'])


class TokenPayInfo(object):
    error_message: str = 'У вас безлимитная подписка, вам не нужно покупать токены'
    something_wrong_message: str = 'Что-то пошло не так. Сообщите, пожалуйста, об ошибке администратору.' \
                                   'Контакты можно найти, вызвав команду /help'

    TOKEN_PAY: Dict[str, Dict[str, str]] = {
        'tokens_100k': {
            'title': '100,000 токенов',
            'description': 'Вы можете получить 100,000 токенов прямо сейчас',
            'payload': 'tokens_100k',
        },
        'tokens_200k': {
            'title': '200,000 токенов',
            'description': 'Вы можете получить 200,000 токенов прямо сейчас',
            'payload': 'tokens_200k',
        },
        'tokens_500k': {
            'title': '500,000 токенов',
            'description': 'Вы можете получить 500,000 токенов прямо сейчас',
            'payload': 'tokens_500k',
        },
        'tokens_1000k': {
            'title': '1,000,000 токенов',
            'description': 'Вы можете получить 1,000,000 токенов прямо сейчас',
            'payload': 'tokens_1000k',
        }
    }

    TOKEN_PAY_INFO: Dict[str, TokenPay] = {
        'tokens_100k': TokenPay(**TOKEN_PAY['tokens_100k']),
        'tokens_200k': TokenPay(**TOKEN_PAY['tokens_200k']),
        'tokens_500k': TokenPay(**TOKEN_PAY['tokens_500k']),
        'tokens_1000k': TokenPay(**TOKEN_PAY['tokens_1000k']),
    }

    TOKEN_PAY_LABELS: Dict[str, TokenLabel] = {
        'tokens_100k': TokenLabel(
            label='100,000 токенов',
            amount=6_000
        ),
        'tokens_200k': TokenLabel(
            label='200,000 токенов',
            amount=9_500
        ),
        'tokens_500k': TokenLabel(
            label='500,000 токенов',
            amount=20_000
        ),
        'tokens_1000k': TokenLabel(
            label='1,000,000 токенов',
            amount=35_000
        )
    }

    TOKENS = {
        'tokens_100k': 100_000,
        'tokens_200k': 200_000,
        'tokens_500k': 500_000,
        'tokens_1000k': 1_000_000
    }
    def __init__(self):
        pass

    @staticmethod
    def get_successful_payment_message(message: Message) -> str:
        """
        Get successful payment message - amount and currency
        :param message: Message object with successful payment
        :return: message about successful payment
        """
        return f'Вы оплатили {message.successful_payment.total_amount // 100} {message.successful_payment.currency}\n' \
               f'Спасибо за покупку! Ваш заказ отправлен на обработку. Пожалуйста, подождите немного.' \
               f'Токены'  # TODO: перенести в отдельный класс

