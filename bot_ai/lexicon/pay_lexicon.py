from collections import namedtuple
from typing import Dict, Type

SubPay: Type['SubPay'] = namedtuple('SubPay', 'title description payload')

SubLabel: Type['SubLabel'] = namedtuple('SubLabel', 'label amount')

SuccessfulPayment = namedtuple('SuccessfulPayment', 'answer')

SUB_PAY: Dict[str, Dict[str, str]] = {
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

# sub_info
SUB_PAY_INFO: Dict[str, SubPay] = {
    'pay_default_sub': SubPay(**SUB_PAY['default_sub']),
    'pay_premium_sub': SubPay(**SUB_PAY['premium_sub']),
    'pay_unlimited_sub': SubPay(**SUB_PAY['unlimited_sub'])

}
# sub_labels
SUB_PAY_LABELS: Dict[str, SubLabel] = {
    'pay_default_sub': SubLabel(
        label='Обычная подписка',
        amount=25_000
    ),
    'pay_premium_sub': SubLabel(
        label='Премиум подписка',
        # amount=112_500
        amount=50_000
    ),
    'pay_unlimited_sub': SubLabel(
        label='Безлимитная подписка',
        # amount=225_000
        amount=75_000
    )
}


payment = SuccessfulPayment(f'Спасибо за покупку! Ваш заказ отправлен на обработку. Пожалуйста, подождите немного.\n')

print(payment.answer)
