from collections import namedtuple
from typing import Dict, Type, Tuple

from aiogram.types import Message

SubPay: Type['SubPay'] = namedtuple('SubPay', 'title description payload')

SubLabel: Type['SubLabel'] = namedtuple('SubLabel', 'label amount')


class SubPayInfo:
    """
    Get all info about payment
    """

    _label1: str = 'Обычная подписка'
    _label2: str = 'Премиум подписка'
    _label3: str = 'Безлимитная подписка'

    _1_month: int = 30
    _3_month: int = 90
    _6_month: int = 180

    _default_cost_1: int = 15_000
    _default_cost_3: int = 40_000
    _default_cost_6: int = 75_000

    _premium_cost_1: int = 30_000
    _premium_cost_3: int = 78_000
    # _premium_cost_6: int = 145_000
    _premium_cost_6: int = 90_000  # test value

    _unlimited_cost_1: int = 65_000
    # _unlimited_cost_3: int = 175_000
    _unlimited_cost_3: int = 75_000  # test value
    # _unlimited_cost_6: int = 320_000
    _unlimited_cost_6: int = 85_000  # test value

    error_message: str = 'Вы собираетесь купить подписку ниже уровнем'
    something_wrong_message: str = 'Что-то пошло не так. Сообщите, пожалуйста, об ошибке администратору.' \
                                   'Контакты администратора можно найти, вызвав команду /help'

    _SUB_PAY: Dict[str, Dict[str, str]] = {
        'default_sub': {
            'title': 'Обычная подписка',
            'description': 'Данная подписка включает в себя 1,500,000 токенов каждую неделю',
            'payload': 'default_sub',
        },
        'premium_sub': {
            'title': 'Премиум подписка',
            'description': 'Данная подписка включает в себя 10,000,000 токенов каждую неделю',
            'payload': 'premium_sub',
        },
        'unlimited_sub': {
            'title': 'Безлимитная подписка',
            'description': 'Данная подписка включает в себя бесконечное количество токенов',
            'payload': 'unlimited_sub',
        }
    }

    _SUB_PAY_INFO: Dict[str, SubPay] = {
        'pay_default_sub': SubPay(**_SUB_PAY['default_sub']),
        'pay_premium_sub': SubPay(**_SUB_PAY['premium_sub']),
        'pay_unlimited_sub': SubPay(**_SUB_PAY['unlimited_sub'])
    }

    _SUB_PAY_LABELS: Dict[str, Dict[str, Tuple[int, str]]] = {
        'pay_default_sub': {
            '1': (_label1, _default_cost_1),
            '3': (_label1, _default_cost_3),
            '6': (_label1, _default_cost_6),
        },
        'pay_premium_sub': {
            '1': (_label2, _premium_cost_1),
            '3': (_label2, _premium_cost_3),
            '6': (_label2, _premium_cost_6),
        },
        'pay_unlimited_sub': {
            '1': (_label3, _unlimited_cost_1),
            '3': (_label3, _unlimited_cost_3),
            '6': (_label3, _unlimited_cost_6),
        }
    }

    _DAYS_SUB: Dict[str, Dict[int, int]] = {
        'default_sub': {
            _default_cost_1: _1_month,
            _default_cost_3: _3_month,
            _default_cost_6: _6_month,
        },
        'premium_sub': {
            _premium_cost_1: _1_month,
            _premium_cost_3: _3_month,
            _premium_cost_6: _6_month,
        },
        'unlimited_sub': {
            _unlimited_cost_1: _1_month,
            _unlimited_cost_3: _3_month,
            _unlimited_cost_6: _6_month,
        }
    }

    _PURCHASED_TOKENS: Dict[str, int] = {
        'default_sub': 1_500_000,
        'premium_sub': 10_000_000,
        'unlimited_sub': 999_999_999
    }

    def __init__(self):
        pass

    def get_labels(self, data_sub: str, months: str) -> SubLabel:
        """
        Get payment details - amount and label
        :param data_sub: subscription name (purchased user status)
        :param months: purchased number of months
        :return: SubLabel
        """
        return SubLabel(*self._SUB_PAY_LABELS[data_sub][months])

    def get_info(self, data_sub: str) -> SubPay:
        """
        Get info about payment - title, description, payload
        :param data_sub: subscription name (purchased user status)
        :return: SubPay
        """
        return self._SUB_PAY_INFO[data_sub]

    def get_days(self, data_sub: str, sub_amount: int) -> int:
        """
        Get days of subscription
        :param data_sub: subscription name (purchased user status)
        :param sub_amount: subscription amount
        :return: purchased days of sub
        """
        return self._DAYS_SUB[data_sub][sub_amount]

    def get_tokens(self, data_sub: str) -> int:
        """
        Get number of purchased tokens
        :param data_sub: subscription name (purchased user status)
        :return: purchased tokens
        """
        return self._PURCHASED_TOKENS[data_sub]

    @staticmethod
    def get_successful_payment_msg(message: Message) -> str:
        """
        Get successful payment message - amount and currency
        :param message: Message object with successful payment
        :return: message about successful payment
        """
        return f'Вы оплатили {message.successful_payment.total_amount // 100} {message.successful_payment.currency}\n' \
               f'Спасибо за покупку! Ваш заказ отправлен на обработку. Пожалуйста, подождите немного.'
